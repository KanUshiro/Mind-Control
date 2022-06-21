from binary_reader import BinaryReader

def writetrigger(trigger,wt: BinaryReader,wtp: BinaryReader,param_jsonloads):
    if trigger["Has Parameter"] == "True":
        trigparam = 0
        partrig = trigger["Parameters"]
        wtp.write_uint32(trigger["Boss ID"])
        wtp.write_uint8(trigger["Change Param ID"])
        wtp.write_uint8(partrig["Unk 3"])
        wtp.write_uint16(partrig["Main Attacks IDs"])
        wtp.write_uint16(partrig["Seize Attacks IDs"])
        wtp.write_uint16(partrig["Down Attacks IDs"])
        wtp.write_uint8(partrig["Fly Damage (?)"])
        wtp.write_float(partrig["Float"])

        for z in partrig:
            if "changes to" in z: wtp.write_uint32(partrig[z])

        wtp.write_uint8(partrig["Defense (?)"])
        wtp.write_uint8(partrig["Hact (?)"])
        wtp.write_uint8(partrig["Unk 4"])

    elif trigger["Has Parameter"] == "False": trigparam = 1
    else: trigparam = trigger["Has Parameter"]

    wt.write_uint32(trigger["Boss ID"])
    wt.write_uint8(trigger["Change Param ID"])
    wt.write_uint8(trigparam)
    wt.write_uint8(trigger["Unk 1"])
    wt.write_float(trigger["Trigger Condition"])
    wt.write_float(trigger["Unk 2"])
    wt.write_str_fixed(trigger["Weapon Type"],4)
    wt.pad(28)