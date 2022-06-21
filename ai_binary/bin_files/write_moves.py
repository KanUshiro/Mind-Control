from binary_reader import BinaryReader
from functions.bitfields import ButtonPressListOE, bitlistToInteger, iterateStringstoBits

def writemoves(f_moveset_key,f_combo_key,f_combo_data,wa: BinaryReader,wc: BinaryReader):

    # write arts_table

	wa.write_uint32(int(f_moveset_key))
	wa.pad(4)
	wa.write_uint8(int(f_combo_key))
	stay = wa.pos()
	try:
		wa.seek(5,2)
		wa.write_float(f_combo_data["Float"])
		wa.seek(1,1)
		wa.write_uint8(f_combo_data["Combo Probability"])
		wa.write_uint16(f_combo_data["Unk"])
		wa.pad(8)
	except:
		print("Error writing Move [{}]".format(f_moveset_key))
		try: wa.seek(stay+11)
		except:
			wa.seek(stay)
			wa.pad(11)


	# write command_table

	moves_dict = f_combo_data["Moves"]
	for x in moves_dict.keys():
		move_string = str(x)
		move_index = int(move_string[5:])
		move_data = moves_dict[move_string]

		wc.write_uint32(int(f_moveset_key))
		wc.write_uint8(int(f_combo_key))
		wc.write_uint8(move_index)
		stay = wc.pos()

		inputs = iterateStringstoBits(ButtonPressListOE,move_data["Inputs"])
		writeinputs = ((bitlistToInteger(inputs[:-8]),bitlistToInteger(inputs[8:])))

		try:
			wc.write_uint16(move_data["u16 Unk1"])
			wc.write_uint8(writeinputs)
			wc.write_uint8(move_data["u8 Unk2"])
			wc.write_uint16(move_data["u16 Unk3"])
			wc.pad(2)
			wc.write_float(move_data["f32 Unk4"])
		except:
			print("Error writing Move [{},{},{}],".format(f_moveset_key,f_combo_key,move_string))
			try:wc.seek(stay+14)
			except:
				wc.seek(stay)
				wc.pad(14)