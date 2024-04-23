import os
import time
import datetime
from playsound import playsound

### If Responder was not installed to the default location enter log path below ###
##Custom log path:
#log_path = "./Responder-Session.log"

# Test

### No need to modify below this line ########################################
##############################################################################

##Default installation log path:
log_path = "/usr/share/responder/logs/Responder-Session.log"


file_size = os.path.getsize(log_path)
last_pos = file_size
last_password = ""
last_user_name = ""
time_captured = ""


def read_log(log_path, last_pos):
    with open(log_path, "r") as f:
        f.seek(last_pos)
        new_lines = f.readlines()
        last_pos = f.tell()
    return new_lines, last_pos


#### Main loop ###
try:
    while True:
        time.sleep(0.5)
        os.system("clear")
        file_size = os.path.getsize(log_path)

        if file_size != last_pos:
            new_lines, last_pos = read_log(log_path, last_pos)
            for line in new_lines:
                line = line.strip()

                if "NTLMv2-SSP Hash" in line:
                    split_hash = line.split(":")
                    captured_user_name = split_hash[3].strip()

                    if captured_user_name != last_user_name:
                        playsound("./hash_capture.mp3")
                        split_hash = line.split()
                        last_password = split_hash[8]
                        last_user_name = captured_user_name
                        time_captured = datetime.datetime.now()
                        time_captured = time_captured.strftime("%m/%d/%Y %I:%M:%S %p") 
                        break

                last_pos = file_size

        print(f'''\033[0;32m

RespResponder
===================================================================
Log File: {log_path}

Capture Time     : {time_captured}
Captured Username: {last_user_name}
Captured Hash    : {last_password}
==================================================================

Press Ctrl+C to exit.
                ''')

except KeyboardInterrupt:
    print("Exiting program!")

