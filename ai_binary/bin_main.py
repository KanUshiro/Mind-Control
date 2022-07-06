from ai_binary.bin_files import write_moves
from ai_binary.bin_files.write_trigger import writetrigger
from binary_reader import BinaryReader
from functions.human_sorting import natural_keys
import os
import json
import sys

def getbin(param):
    cwd = os.getcwd()
    dir = os.path.join(cwd,"boot.par_new")
    if not os.path.exists(dir):
        os.mkdir(dir)

    command_table = open(dir + "\\command_table.bin","wb")
    wc = BinaryReader()
    wc.set_endian(True)

    arts_table = open(dir + "\\arts_table.bin","wb")
    wa = BinaryReader()
    wa.set_endian(True)

    enemy_ai_param = open(dir + "\\enemy_ai_param.bin","wb")
    we = BinaryReader()
    we.set_endian(True)

    ai_change_trigger = open(dir + "\\ai_change_trigger.bin","wb")
    wt = BinaryReader()
    wt.set_endian(True)

    ai_change_param = open(dir + "\\ai_change_param.bin","wb")
    wtp = BinaryReader()
    wtp.set_endian(True)

    wc.write_str("cOTB")
    wa.write_str("aRTB")
    we.write_str("eAPB")
    wc.write_uint64(281474976710657)
    wa.write_uint64(281474976710657)
    we.write_uint64(281474976710657)
    wc.pad(8)
    wa.pad(8)
    we.pad(4)

    param_jsonloads = json.loads(param.read())

    # implement game TODO
    moveset_count = param_jsonloads["Used AI Count"]
    we.write_uint32(moveset_count)

    ### enemy_ai_param.bin

    #for x in param_jsonloads["AI IDs"]:
    #    bossfilename = "{}_{}.json"
    #    with open(os.path.join(sys.argv[1],"bosses",bossfilename.format(x,param_jsonloads["AI IDs"][x]))) as h: boss = json.load(h)

    sorted_enemy = os.listdir(sys.argv[1] + "//bosses")
    sorted_enemy.sort(key=natural_keys)

    for file in sorted_enemy:
        with open(os.path.join(sys.argv[1],"bosses",str(file))) as h: boss = json.load(h)

        we.write_uint32(boss["AI ID"])
        we.write_uint32(boss["HP"])
        we.write_uint32(boss["Unk 1"])
        we.write_uint16(boss["Main Attacks IDs"])
        we.write_uint16(boss["Seize Attacks IDs"])
        we.write_uint16(boss["Down Attacks IDs"])
        we.write_uint8(boss["Fly Damage (?)"])
        we.write_float(boss["Float"])
        we.write_uint16(boss["Unk2 (Weapon?)"])
        we.write_uint16(boss["Rise (?)"])
        we.write_uint8(boss["Defense (?)"])
        we.write_uint8(boss["Hact (?)"])
        we.write_uint8(boss["Unk 4"])
        we.write_str_fixed(boss["Moveset Name"],40)

    enemy_ai_param.write(we.buffer())

    ocd = []
    for x in os.listdir(sys.argv[1] + "//moves"): ocd.append(int(x[:-5]))
    ocd.sort()

    for file in ocd:
        with open(os.path.join(sys.argv[1],"moves",str(file) + ".json")) as h: moveset = json.load(h)
        for x in moveset: write_moves.writemoves(file,x[6:],moveset[x],wa,wc)

    wc.seek(16)
    wa.seek(16)
    wc.write_uint32(int(wc.size() / 20 - 1))
    wa.write_uint32(int(wa.size() / 20 - 1))

    command_table.write(wc.buffer())
    arts_table.write(wa.buffer())

    wt.write_str('aCTB')
    wtp.write_str('aCPB')
    wt.write_uint64(281474976710657)
    wtp.write_uint64(281474976710657)
    wt.pad(4)
    wtp.pad(4)
    wt.write_uint32(param_jsonloads["AI Change Trigger Count"])
    wtp.write_uint32(param_jsonloads["AI Change Param Count"])


    sorted_trigger = os.listdir(sys.argv[1] + "//change_trigger")
    sorted_trigger.sort(key=natural_keys)

    for file in sorted_trigger:
        with open(os.path.join(sys.argv[1],"change_trigger",str(file))) as h: trigger = json.load(h)
        writetrigger(trigger,wt,wtp,param_jsonloads)


    ai_change_trigger.write(wt.buffer())
    ai_change_param.write(wtp.buffer())