#!/bin/sh

apt-get update -y
apt-get upgrade -y
apt-get install autoconf -y
apt-get install pkg-config -y
apt-get install libcurl4-openssl-dev -y
apt-get install libssl-dev -y
apt-get install libgmp-dev -y
apt-get install zlib1g-dev -y
apt-get install libjansson-dev -y
apt-get install automake -y
apt-get install libtool -y  
apt-get install make -y
apt-get install g++ -y
apt-get install nano -y


chmod +x edit
chmod +x run
chmod +x update
chmod +x ANSI_Shadow.flf
chmod +x backup
chmod +x restore
chmod +x install.txt

apt-get install python3 -y
apt-get install pip -y
apt-get install wget -y
apt-get install figlet -y
apt-get install python3-progress -y
apt-get install python3-requests -y


mv src-miner ../../etc
mv edit ../../bin
mv run ../../bin
mv update ../../bin
mv ANSI_Shadow.flf ../../usr/share/figlet
mv backup /data/data/com.termux/files/usr/bin
mv restore /data/data/com.termux/files/usr/bin
mv install.txt /storage/emulated/0/download

run


cd && cd ../etc/src-miner/miner
chmod +x build-linux-arm.sh
chmod +x autogen.sh
./build-linux-arm.sh

chmod +x miner

cd && cd ../etc
nano bash.bashrc

run
