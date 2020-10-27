#!/bin/bash
apt install curl -y
apt install dante-server -y
pip3 install requests
chmod +x /etc/init.d/danted
update-rc.d danted defaults
ip a > setup_proxy/interfase.txt
