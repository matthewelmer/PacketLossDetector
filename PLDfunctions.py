import pythonping as pp

def getInput(inputList):
    # These shouldn't need changing, idk could make a configuration file to read from later
    packetTimeout = 1  # seconds
    packetPayload = bytes(500)  # bytes

    # read these from command line
    server = ''
    if len(inputList) > 1 and inputList[1]:
        server = inputList[1]
        if server.lower() == 'default':
            server = '8.8.8.8'  # Google primary DNS
    else:
        server = '8.8.8.8'  # Google primary DNS

    testDuration = 0
    if len(inputList) > 2 and inputList[2]:
        try:
            testDuration = int(inputList[2])  # seconds
        except ValueError:
            pass
        if inputList[2] == 'default':
            testDuration = 60  # seconds
    else:
        testDuration = 60  # seconds

    packetsPerSecond = 0
    if len(inputList) > 3 and inputList[3]:
        try:
            packetsPerSecond = int(inputList[3])
        except ValueError:
            pass
        if inputList[3] == 'default':
            packetsPerSecond = 60
    else:
        packetsPerSecond = 60

    packetCount = testDuration * packetsPerSecond
    packetInterval = 1 / packetsPerSecond  # inverse of frequency is period ("interval")
    
    return server, packetTimeout, packetPayload, packetCount, packetInterval
