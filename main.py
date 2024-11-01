import subprocess
import ctypes
import sys
import os

CMD_LINE = ""
SCRIPT_PATH = ""
sys.stderr = ""
if os.path.exists(__file__):
    SCRIPT_PATH = __file__
for i in range(len(sys.argv)):
    if i != 0:
        CMD_LINE = CMD_LINE + sys.argv[i]
        if i != len(sys.argv)-1:
            CMD_LINE = CMD_LINE + " "

if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, SCRIPT_PATH + " " + CMD_LINE, None, 1)
    subprocess.run(CMD_LINE, shell=True, check=True)
