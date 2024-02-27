from rcon.battleye import Client
import time
import re

### REQUIREMENTS:
### 1. python3 programming language (WINDOWS download: https://www.python.org/downloads/release/python-3118/)
### 2. pip/pip3, for installing python3 libraries (should come with python3 installation)
### 3. rcon library (COMMAND: pip install rcon)
### 4. MUST use -adminlog in the args when running DayZServer_x64.exe
### 5. MUST have RConPassword set, RestrictRCon must be set to 0, and RConPort set. (all in DayZServer/battleye/BEServer_x64.cfg)
### 6. MUST set the proper information on the lines below

dayz_ADM_log_path = r"C:\full\path\to\DayZServer\profiles\DayZServer_x64.ADM"
rcon_server_address = "127.0.0.1"
rcon_server_port = "2304"
rcon_server_password = ""

# dayz_ADM_log_path should be set to the ADM file that is written to live by the server.  Mine was DayZServer/profiles/DayZServer_x64.ADM
# rcon_server_address is the IP address of your DayZ server, or 127.0.0.1 if you run this py script on the same IP.
# rcon_server_port is the port specified in DayZserver/battleye/BEServer_x64.cfg as RConPort


already_displayed = [] # leave this alone!
while True:
    time.sleep(0.3) # the max delay when checking for new kills
    with open(dayz_ADM_log_path, 'r') as file:
        lines = file.read().splitlines()
        for line_num, line in enumerate(lines):
            if "killed by Player" in line:
                if line not in already_displayed: # the quickest way i thought of determining if we already displayed this kill
                    victim, killer = re.findall('"([^"]*)"', line)
                    result = re.search(' with (.*) from ', line)
                    weapon = result.group(1)
                    result = re.search(' from (.*) meters', line)
                    distance = result.group(1)
                    with Client(rcon_server_address, int(rcon_server_port), passwd=rcon_server_password) as client:
                        response = client.run(f"say -1 [{killer}] killed [{victim}] using [{weapon}] from {distance} meters.") # the command to be executed
                        print(f"[{killer}] killed [{victim}] using [{weapon}] from {distance} meters.") # output in python window
                    already_displayed.append(line)

