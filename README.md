# Overview
This Datapack helps you with deciding what advancements to do!
> (Only tested on & made for 1.21.11)
# Version 2
- [ ] TOMAKE
# Version 1
Before dropping in datapack in to the world you'll need to "generate" a [command storage file](https://minecraft.wiki/w/Command_storage_format) using a script in a [/script](https://github.com/Zahar2loshara/AdvancementsRoulette/tree/main/script)
## Python (.py)
### Prerequisites and Setting Up
#### Video
- [ ] TODO
#### Text
0. Install Python itself @ https://www.python.org/downloads/
1. Get Python script on your computer
2. (Optional) Install package [RapidNBT](https://github.com/GlacieTeam/RapidNBT/) via `pip install rapidnbt` in the terminal
3. Get your datapacks you will have on your world/server (If theyre `.zip`, unzip them and put them in a folder) and its best place them alongside Python script (not tested whole paths)
4. Run the script via `python advancements_roulette.py` in the terminal
5. Input as script asks
6. if you're using only text file then scroll further
7. Get your `.dat` file and move it or copy it into your `.minecraft/saves/New world/data/<HERE>` folder
8. And now its done! You can join your world and in-game run `/trigger adv.roll` to, roll for an advancement!


<br/>1. If you decided to use only text file then you'll need to **copy whole text** and either use [NBT Studio](https://github.com/tryashtar/nbt-studio) (Windows), or [Dovetail](https://offroaders123.github.io/Dovetail/) (Web (Windows, Android))\
1.1. If you're using NBT Studio then start by just opening the program (not `.dat` or `.nbt` file, just nothing)\
1.1.1. Press `CTRL + ALT + V` to paste\
1.1.2. Press `CTRL + SHIFT + S` or Flie>Save As, to save as file and name it "command_storage_advancements_roulette.dat"\
1.1.3. Now just select NBT, instead of Uncompressed -> G-Zip, ~~Little-Endian~~, ~~Bedrock Header~~ and OK\
1.2 If you're using Dovetail then start by, open the website\
1.2.1. Throw in absolutely any file\
1.2.2. Open "Format Options..." and select as followed, Root Name:Disable, Endian:Big, Compression:gzip, Bedrock Level:off\
1.2.3. Paste inside generated text and Save file as "command_storage_advancements_roulette.dat"\
2. Now that you have the `.dat` file, go back to Step 7

# TODO List
- [ ] version 2 datapack\
its supposed to be utilize command block's `LastOutput` field for getting the advancement's display information (or something of that sorts i dunno)
- [ ] video of how to setup
- [ ] add pictures to the text python
- [ ] support multiple datapacks per instance of script
- [ ] some kind of menu for the 1v script
- [ ] a web version of setting up the 1v
- [ ] detect when the advancement is completed
- [ ] "collect" more info \
like how much player rerolled and how many time did player actually complete given advacements
- [ ] maybe support weights in advancements so more hard advancements are rarer? idunno

# Why?
just cuz i cant myself play without BaC and cant decide what advancements to do and i dont want to have it only for myself
