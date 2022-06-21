from binary_reader import BinaryReader
import sys
from ai_json import json_main
from ai_binary import bin_main

##############
# BIN > JSON #
##############

try:
    command_table = open(sys.argv[1] + "\\command_table.bin","rb")
    rc = BinaryReader(command_table.read())
    rc.set_endian(True)
    bin_to_json = True

##############
# JSON > BIN #
##############

except:
    try:
        param = open(sys.argv[1] + "\\param.json")
        bin_to_json = False
    except: raise Exception("I couldn't find any files...")

if bin_to_json == True: json_main.getjson(rc)
else: bin_main.getbin(param)