Simple python3 script to get an ingame killfeed in your DayZ server without installing any mods or paying for RCon tools to do it.  This script will locally read the DayZ administrator log and announce over RCon when someone is killed on the server.
You can easily use this script on the same server that you are running DayZ with near-zero latency, and it shouldn't cause any issues for other RCon tools.

REQUIREMENTS:
1. python3 programming language (WINDOWS download: https://www.python.org/downloads/release/python-3118/)
2. rcon library ([from here](https://github.com/conqp/rcon))
3. MUST use -adminlog in the args when running DayZServer_x64.exe
4. MUST have RConPassword set, RestrictRCon must be set to 0, and RConPort set. (all in DayZServer/battleye/BEServer_x64.cfg)
5. MUST set the proper information into the script.

SUPPORT:
Add fugma313 on Discord, you may have to join a server so we have one in common (https://discord.com/invite/PPzdNrZZW2)
