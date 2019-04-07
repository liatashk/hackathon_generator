#!/usr/bin/env bash
sh car_files/can_down.sh
sh car_files/setup.sh
sh car_files/can_up.sh
python3 bio_car_auth/auth_server.py 192.168.10.215