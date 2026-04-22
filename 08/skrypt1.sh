MY_X=83

for Y in $(seq 71 90); do
    if [ "$Y" -ne "$MY_X"]; then
        sudo ip route add 10.192.$Y.0/30 via 192.168.48.$Y
    fi
done