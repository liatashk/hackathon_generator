#!/usr/bin/env bash
cd /home/pi/Hackathon/hackathon_generator
sh car_files/can_down.sh
sh car_files/setup.sh
sh car_files/can_up.sh
cd /home/pi/Hackathon/hackathon_generator/bio_car_auth
sudo python3 auth_server.py 192.168.100.215