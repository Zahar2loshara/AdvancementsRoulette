# advancements roulette python script
import json
from pathlib import Path
import os
import re
try:
    from rapidnbt import nbtio,NbtFileFormat
    rapidnbt_installed = True
except ModuleNotFoundError:
    print("\n\033[1m\033[31m\"RapidNBT\" module wasn't found; Please install it for the script to make a .dat file for you\033[0m")
    rapidnbt_installed = False

raw_folder = input("Input the path of datapack's root folder.\n\033[2m(folder with folder named 'data' and file 'pack.mcmeta')\033[0m\n")
read_folder= os.listdir(raw_folder)
print("\n\n")
default_write = "output.txt"
output_file = open(input(f"Input a name \033[4mand extension\033[0m for the output file.\n\033[1m(THIS FILE WILL BE REWRITTEN AND WHATEVER IS IN THAT FILE WILL BE DELETED/REPLACED)\033[0m\033[2m\n(leave empty for default \"{default_write}\")\n\033[0m") or default_write,"wt")
print("\n\n")

root = Path.cwd()
os.chdir(os.path.join(root,raw_folder))
dp_root = Path.cwd()
dp_folder = os.listdir(dp_root)
dp_files = []

try:
    for i, item in enumerate(read_folder):
        #if 'pack.mcmeta' in dp_folder and 'data' in dp_folder:
            #print("\x1b[32mFound the datapack root\x1b[0m")
        if "pack.mcmeta" not in dp_folder and "data" not in dp_folder:
            #print("\x1b[93midunno anymore man, you probably inputted wrong folder but im also getting it and it works and i dont want to break it more\x1b[0m")
            os.chdir(os.path.join(root,raw_folder,item))
            dp_root = Path.cwd()
            deeper_root = True
            dp_folder = os.listdir(dp_root)
        else:
            #print("\x1b[91mI dont know how but something went unexpectedly wrong, somehow\n\x1b[2mthe error is in failsaving datapack's root folder\x1b[22m\x1b[0m")
            deeper_root = False
except NotADirectoryError: # well ignoring the problem seems to be working
    pass

for root, dirs, files in os.walk(dp_root): # inital credit goes to https://www.geeksforgeeks.org/python/python-list-all-files-in-directory-and-subdirectories/ and i modified it
    for file in files:
        dp_files.append(os.path.join(root, file))

advancements_dp_files = [k for k in dp_files if "advancement\\" in k]

###################
def path_to_identifier(path: str): #source: chat gee pee tee
    match = re.search(
        r'\\data\\([^\\]+)\\advancement\\(.+)\.json$',
        path
    )
    if not match:
        return ""

    namespace = match.group(1)
    inner_path = match.group(2).replace('\\', '/')

    return f"\"{namespace}:{inner_path}\""
###################

def the_thing():
    return_value = str()
    for advancement in advancements_dp_files:
        adv_json = dict()
        if advancement.strip():
            adv_json.update(json.load(open(advancement)))
        else:
            #print("Received empty data",file=output_file) # for some reason never does that, probably because "except KeyError" catches it
            pass
        namespace = path_to_identifier(advancement)
        try:
            #print(f"{namespace}:[{str(adv_json["display"]["title"])},{str(adv_json["display"]["description"])}],",file=output_file)
            return_value = return_value + "{" + f"\"name\":{namespace},\"title\":{adv_json["display"]["title"]},\"desc\":{adv_json["display"]["description"]}" + "}\n"
        except KeyError:
            return_value = return_value + "\n"
            #print(file=output_file) #print empty line in the file to indicate that the advancement doesnt have a '"display":{}'
    return return_value

snbt = the_thing()
output_file.write(snbt)

#os.chdir(root)
if rapidnbt_installed is True:
    snbt_form = "{\"DataVersion\":4671,\"data\":{\"contents\":{\"advancements_roulette\":{\"display\":["+snbt+"]}}}}"
    nbt = nbtio.loads_snbt(snbt_form) 
    #nbt_form = CompoundTag({"DataVersion":IntTag(4671),"data":CompoundTag({"contents":CompoundTag({"advancements_roulette":ListTag({"display":ListTag(nbt)})})})})
    if deeper_root is True:
        nbtio.dump(nbt, "../../command_storage_advancements_roulette.dat", NbtFileFormat.BIG_ENDIAN)
    elif deeper_root is False:
        nbtio.dump(nbt, "../command_storage_advancements_roulette.dat", NbtFileFormat.BIG_ENDIAN)

print(f"And im done! \033[2m(i actually dont know im just a script)\033[0m Check \"{output_file.name}\" or \"command_storage_advancements_roulette.dat\" and continue on the guide.") # for text color and effect i wanna credit https://jakob-bagterp.github.io/colorist-for-python/ansi-escape-codes/ and https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
output_file.close()
