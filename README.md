Simple python3 script to locally read the DayZ administrator log and announce over RCon when someone is killed on the server.

You can easily use this script on the same server that you are running DayZ with near-zero latency, and it shouldn't cause any issues for other RCon tools.

REQUIREMENTS:
1. python3 programming language (WINDOWS download: https://www.python.org/downloads/release/python-3118/)
2. pip/pip3, for installing python3 libraries (should come with python3 installation)
3. rcon library (COMMAND: pip install rcon)
4. MUST use -adminlog in the args when running DayZServer_x64.exe
5. MUST have RConPassword set, RestrictRCon must be set to 0, and RConPort set. (all in DayZServer/battleye/BEServer_x64.cfg)
6. MUST set the proper information into the script.