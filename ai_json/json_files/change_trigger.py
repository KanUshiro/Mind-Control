from binary_reader import BinaryReader
import json
import sys
import os

def EnsureAIExists(ai_id,cmn):
    if ai_id not in cmn["AI IDs"]:
        cmn["AI IDs"][ai_id] = "Unused"

def gettrigger(dir_main,cmn):
    ai_change_trigger = open(sys.argv[1] + "\\ai_change_trigger.bin","rb")
    rt = BinaryReader(ai_change_trigger.read())
    rt.set_endian(True)

    rt.seek(16)
    t_triggercount = rt.read_uint32()

    ai_change_param = open(sys.argv[1] + "\\ai_change_param.bin","rb")
    rtp = BinaryReader(ai_change_param.read())
    rtp.set_endian(True)
    rtp.seek(16)
    tp_paramcount = rtp.read_uint32()

    
    dir_trigger = os.path.join(os.getcwd(),dir_main,"change_trigger")
    if not os.path.exists(dir_trigger): os.mkdir(dir_trigger)

    for i in range(t_triggercount):

        t_bossid = rt.read_uint32()
        EnsureAIExists(t_bossid,cmn)
        t_changeparamid = rt.read_uint8()
        t_hasparam = rt.read_uint8()
        t_unk1 = rt.read_uint8(2)
        t_triggercondition = rt.read_float()
        t_unk2 = rt.read_float(2)
        t_triggername = rt.read_str(4)
        t_field = rt.read_uint8(28)
        t_param_data = "None"

        if t_hasparam == 0:
            t_hasparam = "True"

            tp_bossid = rtp.read_uint32()
            EnsureAIExists(tp_bossid,cmn)
            tp_changeparamid = rtp.read_uint8()
            tp_unk3 = rtp.read_uint8(3)
            tp_main_arts = rtp.read_uint16(4)
            tp_seize_arts = rtp.read_uint16(2)
            tp_down_arts = rtp.read_uint16(3)
            tp_flydmg = rtp.read_uint8(10)
            tp_float = rtp.read_float(3)
            tp_swapid = rtp.read_uint32(2)
            EnsureAIExists(tp_swapid[0],cmn)
            EnsureAIExists(tp_swapid[1],cmn)
            tp_defense_arts = rtp.read_uint8(4)
            tp_hact = rtp.read_uint8()
            tp_unk4 = rtp.read_uint8(11)

            t_param_data = {
                cmn["AI IDs"][tp_bossid] + " changes to " + cmn["AI IDs"][tp_swapid[0]] + ", AI ID(s):": tp_swapid,
                "Unk 3": tp_unk3,
                "Main Attacks IDs": tp_main_arts,
                "Seize Attacks IDs": tp_seize_arts,
                "Down Attacks IDs": tp_down_arts,
                "Fly Damage (?)": tp_flydmg,
                "Float": tp_float,
                "Defense (?)": tp_defense_arts,
                "Hact (?)": tp_hact,
                "Unk 4": tp_unk4
            }

        elif t_hasparam == 1: t_hasparam = "False" ## sometimes this shit is 2 (shakedown)

        t_buffer = {
            "AI ID": tp_bossid,
            "Change Param ID": t_changeparamid,
            "Has Parameter": t_hasparam,
            "Unk 1": t_unk1,
            "Trigger Condition": t_triggercondition,
            "Unk 2": t_unk2,
            "Weapon Type": t_triggername,
            "Parameters": t_param_data
        }
        
        wt_b = open(dir_trigger + "\\" + str(i) + "_" + cmn["AI IDs"][t_bossid] + ".json","wt")
        wt_b.write(json.dumps(t_buffer,indent=3))

        
        cmn["AI Change Trigger Count"] = t_triggercount
        cmn["AI Change Param Count"] = tp_paramcount