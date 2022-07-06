import os
import json
from ai_json.json_files import moves
from ai_json.json_files import enemy_ai_param
from ai_json.json_files import change_trigger

def getjson(rc):

    dir_main = os.path.join(os.getcwd(),"AI unpacked")
    if not os.path.exists(dir_main): os.mkdir(dir_main)

    dir_bosses = os.path.join(os.getcwd(),dir_main,"bosses")
    if not os.path.exists(dir_bosses): os.mkdir(dir_bosses)

    dir_moves = os.path.join(os.getcwd(),dir_main,"moves")
    if not os.path.exists(dir_moves): os.mkdir(dir_moves)

    try: moves.getmoves(rc,dir_moves)
    except:open(dir_moves + "\\" + "h" + ".json","wt")

    w_cmn = open(dir_main + "\\param.json","wt")
    
    cmn = {
        "Game": "Yakuza 0/Kiwami 1/FOTNS",
        "Used AI Count": "",
        "AI Change Trigger Count": "",
        "AI Change Param Count": "",
        "AI IDs": {}
    }

    enemy_ai_param.getbosses(cmn,dir_bosses)
    change_trigger.gettrigger(dir_main,cmn)

    w_cmn.write(json.dumps(cmn,indent=3))