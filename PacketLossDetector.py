import pythonping as pp
import sys
import time
import sched
import PLDfunctions

"""
Usage: PacketLossDetector.py <server IP>(optional) <testDuration> (optional) <packetsPerSecond>(optional)
"""

pingScheduler = sched.scheduler(time.time, time.sleep)

# pp.ping('8.8.8.8', verbose=True)

server, packetTimeout, packetPayload, packetCount, packetInterval = PLDfunctions.getInput(sys.argv)

results = pp.executor.ResponseList()

result = pp.ping(server, timeout=packetTimeout, payload=packetPayload, count=1)._responses[0]

results.append(result)



print(results)
