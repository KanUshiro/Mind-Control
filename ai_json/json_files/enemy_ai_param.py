from binary_reader import BinaryReader
import sys
import json

def getbosses(cmn,dir_bosses):

    enemy_ai_param = open(sys.argv[1] + "\\enemy_ai_param.bin","rb")
    re = BinaryReader(enemy_ai_param.read())
    re.set_endian(True)
    re.seek(16)
    e_bosscount = re.read_uint32()

    for i in range(e_bosscount):
        e_id = re.read_uint32()
        e_hp = re.read_uint32()
        e_unk1 = re.read_uint32(2)
        e_main_arts = re.read_uint16(4)
        e_seize_arts = re.read_uint16(2)
        e_down_arts = re.read_uint16(3)
        e_flydmg = re.read_uint8(10)
        e_float = re.read_float(5)
        e_weapon = re.read_uint16()
        e_notfly = re.read_uint16(7)
        e_defense_arts = re.read_uint8(4)
        e_hact = re.read_uint8()
        e_chk = re.read_uint8(3)
        e_setname = re.read_str(40)
        
        e_boss = {
            "Moveset Name": e_setname,
            "Moveset ID": e_id,
            "HP": e_hp,
            "Unk 1": e_unk1,
            "Main Attacks IDs": e_main_arts,
            "Seize Attacks IDs": e_seize_arts,
            "Down Attacks IDs": e_down_arts,
            "Fly Damage (?)": e_flydmg,
            "Float": e_float,
            "Unk2 (Weapon?)": e_weapon,
            "Rise (?)": e_notfly,
            "Defense (?)": e_defense_arts,
            "Hact (?)": e_hact,
            "Unk 4": e_chk
        }

        we_b = open(dir_bosses + "\\" + str(e_id) + "_" + e_setname + ".json","wt")
        we_b.write(json.dumps(e_boss,indent=3))
        cmn["Boss IDs"].update({e_id:e_setname})
        cmn["Boss Count"] = e_bosscount
