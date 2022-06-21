from binary_reader import BinaryReader
import json
import sys
from functions.bitfields import *

def getmoves(rc,dir_moves):
    ### command_table

    rc.seek(16)
    c_commandcount = rc.read_uint32()
    c_combocommandset_list = []
    c_move_data = []
    for i in range(c_commandcount):
        c_commandset_id = rc.read_uint32()
        c_combo_id = rc.read_uint8()
        c_move_id = rc.read_uint8()
        c_unk1 = rc.read_uint16()
        c_inputs = rc.read_uint8(2)
        c_unk2 = rc.read_uint8(2)
        c_unk3 = rc.read_uint16()
        rc.seek(2,1)
        c_float = rc.read_float()

        decodedinputs = bitfieldListMask(bitfield(c_inputs[0]) + bitfield(c_inputs[1]), ButtonPressListOE)

        c_combocommandset_list.append((c_commandset_id,c_combo_id))
        c_move_data.append({"Inputs":decodedinputs,"u16 Unk1":c_unk1,"u8 Unk2":c_unk2,"u16 Unk3":c_unk3,"f32 Unk4":c_float})

    ### arts_table

    arts_table = open(sys.argv[1] + "\\arts_table.bin","rb")
    ra = BinaryReader(arts_table.read())
    ra.set_endian(True)

    ra.seek(16)
    a_artscount = ra.read_uint32()

    a_commandset_list = []
    a_commandset_data = []
    a_comboid_list = []
    for i in range(a_artscount):
        a_commandset_id = ra.read_uint32()
        a_float = ra.read_float()
        a_combo_id = ra.read_uint8()
        a_combo_probability = ra.read_uint8()
        a_unk = ra.read_uint16()

        a_commandset_list.append(a_commandset_id)
        a_comboid_list.append(a_combo_id)
        a_combo = (a_commandset_id,a_combo_id)
        u = 0
        a_move_id = 0
        combo = {}
        for x in c_combocommandset_list:
            if a_combo == x:
                combo.update({"Move " + str(a_move_id): c_move_data[u]})
                a_move_id += 1
            u += 1

        a_commandset_data.append({"Combo Probability":a_combo_probability,"Float":a_float,"Unk":a_unk,"Moves":combo})

        ra.seek(8,1)

    for x in a_commandset_list:
        wa = open(dir_moves + "\\" + str(x) + ".json","wt")
        wa_buffer = {}
        for i in range(a_artscount):
            if a_commandset_list[i] == x:
                wa_buffer["Combo " + str(a_comboid_list[i])] = a_commandset_data[i]
        wa.write(json.dumps(wa_buffer,indent=3))