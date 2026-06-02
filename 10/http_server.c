// server.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/types.h>

#define DEFAULT_PORT 80
#define BACKLOG 10
#define BUFFER_SIZE 4096

int main(int argc, char* argv[]) {
    int server_fd;
    int client_fd;

    int port = DEFAULT_PORT;

    if (argc > 1) {
        port = atoi(argv[1]);
    }

    if (getuid() == 0) {
        fprintf(stderr, "Nie uruchamiaj serwera jako root!\n");
        return EXIT_FAILURE;
    }

    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    if (server_fd < 0) {
        perror("socket");
        return EXIT_FAILURE;
    }

    int opt = 1;

    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)) < 0) {
        perror("setsockopt");
        close(server_fd);
        return EXIT_FAILURE;
    }

    struct sockaddr_in addr;
    memset((char*)&addr, 0, sizeof(addr));

    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_ANY);

    // 127.0.0.1:
    // addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);

    addr.sin_port = htons(port);

    if (bind(server_fd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("bind");
        close(server_fd);
        return EXIT_FAILURE;
    }

    if (listen(server_fd, BACKLOG) < 0) {
        perror("listen");
        close(server_fd);
        return EXIT_FAILURE;
    }

    printf("Serwer nasłuchuje na porcie %d...\n", port);

    while (1) {
        struct sockaddr_in client_addr;
        socklen_t client_len = sizeof(client_addr);

        client_fd = accept(server_fd, (struct sockaddr*)&client_addr, &client_len);

        if (client_fd < 0) {
            perror("accept");
            continue;
        }

        printf("Połączenie od %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

        // recv
        char recv_buffer[BUFFER_SIZE];

        ssize_t received = recv(client_fd, recv_buffer, sizeof(recv_buffer) - 1, 0);

        if (received < 0) {
            perror("recv");
            close(client_fd);
            continue;
        }

        recv_buffer[received] = '\0';

        printf("Otrzymano:\n%s\n", recv_buffer);

        FILE* uptime_file = fopen("/proc/uptime", "r");

        if (uptime_file == NULL) {
            perror("fopen");

            close(client_fd);
            continue;
        }

        double uptime;

        if (fscanf(uptime_file, "%lf", &uptime) != 1) {
            fprintf(stderr, "Błąd odczytu /proc/uptime\n");

            fclose(uptime_file);
            close(client_fd);

            continue;
        }

        fclose(uptime_file);

        char body[256];

        int body_length = snprintf(body, sizeof(body), "Uptime: %.2f sekund\n", uptime);

        if (body_length < 0) {
            fprintf(stderr, "snprintf body\n");

            close(client_fd);
            continue;
        }

        char header[512];

        int header_length = snprintf(
            header,
            sizeof(header),
            "HTTP/1.0 200 OK\r\n"
            "Content-Type: text/plain; charset=UTF-8\r\n"
            "Connection: close\r\n"
            "Content-Length: %d\r\n"
            "\r\n",
            body_length
        );

        if (header_length < 0) {
            fprintf(stderr, "snprintf header\n");

            close(client_fd);
            continue;
        }

        ssize_t sent = send(client_fd, header, header_length, 0);

        if (sent < 0) {
            perror("send header");

            close(client_fd);
            continue;
        }

        sent = send(client_fd, body, body_length, 0);

        if (sent < 0) {
            perror("send body");

            close(client_fd);
            continue;
        }

        if (shutdown(client_fd, SHUT_WR) < 0) {
            perror("shutdown");
        }

        if (close(client_fd) < 0) {
            perror("close client");
        }
    }

        if (close(server_fd) < 0) {
            perror("close server");
        }

    return EXIT_SUCCESS;
}