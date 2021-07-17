import pythonping as pp
import sys
import time
import sched
import PLDfunctions

"""
Usage: PacketLossDetector.py <server IP>(optional) <testDuration> (optional) <packetsPerSecond>(optional)
"""


if __name__ == "__main__":
    # pingScheduler = sched.scheduler(time.time, time.sleep)
    server, packetTimeout, packetPayload, packetCount, packetInterval = PLDfunctions.getInput(sys.argv)

    results = pp.ping(server, timeout=packetTimeout, count=packetCount, interval=packetInterval, payload=packetPayload)

    # pingScheduler.enter(0, 1, PLDfunctions.pingAndAppend, (server, packetTimeout, packetPayload, results))
    # for i in range(packetCount - 1):
    #     pingScheduler.enter(packetInterval, 1, PLDfunctions.pingAndAppend, (server, packetTimeout, packetPayload, results))
    # pingScheduler.run()

    print(results)
