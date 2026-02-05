import time
from brping import Ping1D

DEVICE = "/dev/ttyAMA3"   # no BlueOS geralmente é esse; depois você ajusta se precisar
BAUDRATE = 115200

def main():
    ping = Ping1D()
    ping.connect_serial(DEVICE, BAUDRATE)
    print(f"Ping1D connected on {DEVICE} @ {BAUDRATE}")

    while True:
        data = ping.get_distance()
        if data:
            dist = data.get("distance")
            conf = data.get("confidence")
            print(f"distance={dist} mm | confidence={conf}")
        else:
            print("No data received")
        time.sleep(0.2)

if __name__ == "__main__":
    main()