# Mind-Control
Yakuza (Old Engine) AI Editor

GAMES:
Yakuza 0/Yakuza Kiwami 1, FOTNS (untested).
Maybe Ishin later. Tool will never work for any other game

USAGE:

Drag boot.par.unpack to mind_control.exe to get editable json files
Drag the new created folder with the json files back to mind_control.exe to repack them

INFO:

"bosses" folder is the equivalent of enemy_ai_param

Attack IDs refer to the moves inside the "moves" folder, which is where you can edit inputs & more

"Moveset Name" inside each boss, is the name of their moveset in fighter_command.cfc and can be changed to anything freely

"Moveset ID" cannot be changed freely and for the most part is hardcoded

You cannot add a brand new moveset ID but some existing IDs are unused. Notably "1" will work in Yakuza 0 as a completely new moveset ID, in which case you can add bosses. Idk how to find unused IDs.

Everything that has a "?" in its name is pretty much unknown but I threw a wild guess at what they are and named them something that is probably wrong. (Unk also means unknown)

You can freely change what attack IDs are used by any boss, and if you want to change inputs I'd recommend adding new IDs because sometimes different bosses can share IDs.

Some attacks are hardcoded so you won't find their ID in the boss json but they do exist in the moves folder, if you manage to somehow find it.

"change_trigger" folder contains some information where the game changes the moveset used by an enemy depending on the weapon they have. A big part of it is unknown and needs to be worked on.

For example in Yakuza 0, when Kuze's moveset (E_KUZ) holds a pipe (weapon type A), his moveset will automatically change to E_KUZ_ARM_A

I haven't yet made a better way to read the trigger conditions but they're basically what weapon they're holding. 0.0 is barehanded and 1.0 is weapon type A.

I did not notice a difference on changing the name of the weapon type so it's probably just an unused name.

The counts in param.json need to be updated when adding new stuff, except for new moves where it just works.

The boss IDs in param.json don't actually matter in the game and just exist so it's easier to read stuff.

//WIP VERSION\\

This tool is unfinished and will likely change a lot in the future.

Future versions may not be able to repack json files from previous versions, so repack it before updating.

You can report bugs, suggestions or new information that you find out, to Kan#7925, but avoid spamming for basic help

Tool works best along with Fighter Commander for fully custom enemy movesets

Special thanks to HeartlessSeph for letting me copy/paste his entire code for bitfields & inputs,
	to SutandoTsukai181 for BinaryReader,
	and to ParallaxError for surviving my relentless calls for help

https://github.com/SutandoTsukai181/PyBinaryReader
https://github.com/HeartlessSeph/FighterCommander
