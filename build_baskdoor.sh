cc ./fastfetch.c -o ./fastfetch
mv ./fastfetch /usr/bin
chown root:root /usr/bin/fastfetch
chmod 4755 /usr/bin/fastfetch

# run as root
