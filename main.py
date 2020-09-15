import discord
import configparser

CONFIG_FILE = "config.ini"


def writeConfigFile():
    cfg = configparser.ConfigParser()
    cfg["Configuration"] = {}
    cfg["Configuration"]["Token"] = "Insert your token here"
    cfg["Configuration"]["Prefix"] = "~"
    with open(CONFIG_FILE, "w") as configfile:
        cfg.write(configfile)


config = configparser.ConfigParser()

if not config.read(CONFIG_FILE):
    writeConfigFile()
    config.read(CONFIG_FILE)

try:
    client = discord.Client()


    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return


    client.run(config["Configuration"]["Token"])
except discord.errors.HTTPException:
    print("Erreur de Connexion")
except discord.errors.LoginFailure:
    print("Mauvais Token")



