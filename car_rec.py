from __future__ import print_function
import can


def rec():
    bus = can.interface.Bus(bustype='socketcan_native', channel='can0', bitrate=250000)
    #bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
    #bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=250000)
    #
    # msg = can.Message(arbitration_id=0xc0ffee,
    #                   data=[0, 25, 0, 1, 3, 1, 4, 1],
    #                   extended_id=True)
    # try:
    #     # bus.recv()
    #     bus.send(msg)
    #     print("Message sent on {}".format(bus.channel_info))
    # except can.CanError:
    #     print("Message NOT sent")
    for msg in bus:
        print(msg.data)

if __name__ == "__main__":
    rec()