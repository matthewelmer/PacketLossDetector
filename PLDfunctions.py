import pythonping as pp

def getInput(inputList):
    # These shouldn't need changing, idk could make a configuration file to read from later
    packetTimeout = 1  # seconds
    packetPayload = bytes(500)  # bytes

    # read these from command line
    server = ''
    if len(inputList) > 1 and inputList[1]:
        server = inputList[1]
    else:
        server = '8.8.8.8'  # Google primary DNS

    testDuration = 0
    if len(inputList) > 2 and inputList[2]:
        testDuration = inputList[2]  # seconds
    else:
        testDuration = 60  # seconds

    packetsPerSecond = 0
    if len(inputList) > 3 and inputList[3]:
        packetsPerSecond = inputList[3]
    else:
        packetsPerSecond = 60

    packetCount = testDuration * packetsPerSecond
    packetInterval = 1 / packetsPerSecond  # inverse of frequency is period ("interval")
    
    return server, packetTimeout, packetPayload, packetCount, packetInterval
