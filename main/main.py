import discord
import os
from discord.ext import commands
# Setup the bot
TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Get token from environment variable
intents = discord.Intents.default()
intents.messages = True  # This ensures the bot can read messages
intents.message_content = True  # This is the key fix!

bot = commands.Bot(command_prefix=".", intents=intents)

# Pre-coded links dictionary
links = {
    "dog":"https://tenor.com/view/treyreloaded-gif-25522323",
    "sad":"https://tenor.com/view/crying-upset-old-man-gif-7407103167577610642",
    "duck":"https://tenor.com/view/klasik-clasik-clasic-gif-25398314",
    "kick":"https://tenor.com/view/jojo-jojo-part5-narancia-abbacchio-mista-gif-13734813",
    "ass":"https://cdn.discordapp.com/attachments/445550268306948096/1359112272118681600/RDT_20250408_1346566179949040092735955.jpg?ex=67f64b70&is=67f4f9f0&hm=0ec7d7047cd87e37e9e86f3fd5165897e274ce79d09d90b03a913bdc5e8fade2&",
    "dontkys2":"https://cdn.discordapp.com/attachments/445550268306948096/1356986746033672292/20250311_183926.jpg?ex=67ee8fe3&is=67ed3e63&hm=8bdce3e6b4b682778536676b930cebd13242dc52c8f91602e29320e99513bc5d&",
    "yoshida":"https://cdn.discordapp.com/attachments/445550268306948096/1356957783072968724/GU5BSETX0AA_4pL.jpg?ex=67ee74ea&is=67ed236a&hm=28ca04ae214787ab807d64eebe9b1267aed788e79929e88ef5fdc14251d1bb1e&",
    "daddy":"https://cdn.discordapp.com/attachments/445550268306948096/1356930534126911558/GbYxiu_WoAAic3R.jpg?ex=67ee5b89&is=67ed0a09&hm=1acf31cb6fc216cadacdb48fc7dc1cafa3483300bbb11b8999c0c19d9444409d&",
    "vomit":"https://tenor.com/view/ken-kaneki-tokyo-ghoul-vomit-burger-food-gif-17905994",
    "bts":
    "https://cdn.discordapp.com/attachments/446620239837265920/1356609214201467125/20250401_180616.jpg?ex=67ed3049&is=67ebdec9&hm=b9f3363d4fbee4f37881114541f6e1e733a6e5f1ad1276691dc940f34cbcdeb6&",
    "gn":
    "https://cdn.discordapp.com/attachments/468063675421294593/1330217988409786511/20250105_064952.jpg?ex=67ecc24a&is=67eb70ca&hm=7de414e045b6fbbefa0b96083121dc451d99632bd05399f5fccc6c546cf2cf64&",
    "cri":"https://cdn.discordapp.com/attachments/445550268306948096/1356636882162679911/20250108_102914.jpg?ex=67ed4a0d&is=67ebf88d&hm=ac104832ca49c7978060236e5711f379d51d2725fb4adf88cd2839dbaaa8e065&",
"cri2":"https://cdn.discordapp.com/attachments/445550268306948096/1356636882473320499/20250106_211852.jpg?ex=67ed4a0d&is=67ebf88d&hm=7690126b29fd8207a17dd154d9d76100131e530127776e4f54507db7364496e9&",
"packwatch":"https://cdn.discordapp.com/attachments/445550268306948096/1356636882758537276/20241228_190125.jpg?ex=67ed4a0d&is=67ebf88d&hm=c13515e4223b1e6b9476d81ea87aba38dd11488a7329571ae51a82abec14c102&",
"cri3":"https://cdn.discordapp.com/attachments/445550268306948096/1356636883211259944/20241224_231931.jpg?ex=67ed4a0e&is=67ebf88e&hm=f1032b1e7b48426d82e5d64d8bbc416d48a30d230d814101db9d1c9469d8381c&",
"smoke":"https://cdn.discordapp.com/attachments/445550268306948096/1356636883467243530/0f35e7cd363ba91870d299f876473bad.jpg?ex=67ed4a0e&is=67ebf88e&hm=0f133caf822242cbc1286916f5fee9a9a0c362de4ab04e1217d01b6cc8118427&",
"shutup":"https://cdn.discordapp.com/attachments/445550268306948096/1356636883710382371/7c088c767861c114a9c719948e1f7127.jpg?ex=67ed4a0e&is=67ebf88e&hm=fdca1256255f3453780263ba51557db4c31d9ede39551f07a3fb2603ca29c69f&",
"dog":"https://cdn.discordapp.com/attachments/445550268306948096/1356636884083933335/20241218_070229.jpg?ex=67ed4a0e&is=67ebf88e&hm=562593aa27c6b4b6ab985e019e1c472a3826e13e42b11caf91e2640436106a8c&",
"free":"https://cdn.discordapp.com/attachments/445550268306948096/1356636884419350659/img_1_1733920143192.jpg?ex=67ed4a0e&is=67ebf88e&hm=0995c5522c5d36348ae477845952a3b941f7c818510765dd49fa2a4ba4ec9789&",
"explode":"https://cdn.discordapp.com/attachments/445550268306948096/1356636884683460832/20241204_075627.jpg?ex=67ed4a0e&is=67ebf88e&hm=a4303c79789adcb373818af6d49c6cf6956f958bd3d947ee93d421b665720eac&",
"dontkys":"https://cdn.discordapp.com/attachments/445550268306948096/1356636884981383218/20241129_201139.jpg?ex=67ed4a0e&is=67ebf88e&hm=5e1487345f189d87bda36b6f9f05436ea2e69b712d80e6005f857ebfce080b2d&",
"postnut":"https://cdn.discordapp.com/attachments/445550268306948096/1356637022433050644/20241013_195925.jpg?ex=67ed4a2f&is=67ebf8af&hm=63205130e766b476031bce18d60f7d0530919157e621cc7471f61322cb911496&",
"gomen":"https://cdn.discordapp.com/attachments/445550268306948096/1356637023049617580/20241104_202250.jpg?ex=67ed4a2f&is=67ebf8af&hm=237c7d38fa6cb6d1b79a5c56a16f3e4c9a15555735f5392b2994cff7e79c19f4&",
}


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def emo(ctx, name: str):
    """Replies with a pre-coded link based on command input."""
    if name in links:
        await ctx.send(links[name])
    else:
        await ctx.send("Link not found! Try: " + ", ".join(links.keys()))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"Received message: {message.content}")
    await bot.process_commands(message)


# Run the bot
if TOKEN is None:
    print("DISCORD_BOT_TOKEN environment variable not set. Exiting.")
    exit(1)
bot.run(TOKEN)
keep_alive()  # Start the web server
bot.run(TOKEN)
