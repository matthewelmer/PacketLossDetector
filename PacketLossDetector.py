import pythonping as pp
import sys
import PLDfunctions

"""
Usage: PacketLossDetector.py <server IP>(optional) <testDuration> (optional) <packetsPerSecond>(optional)

Todo: Write server address, packet id, size, status, and ping for each packet to file, where packet id is just its index in the list
"""


if __name__ == "__main__":
    server, packetTimeout, packetPayload, packetCount, packetInterval = PLDfunctions.getInput(sys.argv)

    results = pp.ping(server, timeout=packetTimeout, count=packetCount, interval=packetInterval, payload=packetPayload)

    print(results)
