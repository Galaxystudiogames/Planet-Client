import requests


#ModURL = "https://cdn.modrinth.com/data/P7dR8mSH/versions/dQ3p80zK/fabric-api-0.138.3%2B1.21.10.jar"
#MinecraftFolder = "Instances"
#ModName = "asd"


def addMods(modURL, minecraftFolder, modName):
    mod = requests.get(modURL)
    with open(minecraftFolder + "/mods/" + modName + ".jar" ,'wb') as f:
        f.write(mod.content)



#addMods(ModURL, MinecraftFolder, ModName)