import os,discord,time,requests
from discord.ext import commands

client = commands.Bot(command_prefix='!',self_bot=True)
os.system('cls' if os.name == 'nt' else 'clear')

Token = 'token_here'
api_key = 'api_key_here'

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    print('Ready to snipe')

@client.event
async def on_message(message: discord.Message):
    if message.author.id == 825617171589759006 or message.author.id == 775875114939580436 or message.author.id == 776128410547126322:
        try:
            if message.embeds[0].image.url:
                time_start = time.time()
                url = message.embeds[0].image.url
                overlay = False
                language = 'eng'
                payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': str(api_key),
               'language': language,
               }
                re = requests.post('https://api.ocr.space/parse/image', data = payload)
                s = re.json()['ParsedResults'][0]['ParsedText']
                time_taken = time.time() - time_start
                await message.reply(s)
                print("Solving " + url)
                print("Solved Image: " + s)
                await message.reply('Solved! Time taken: ' + str(time_taken) + ' seconds')
            else:
                print("No Image")
        except Exception as e:
            print("Couldnt solve game or wasnt valid")
            print(e)

    else:
       pass

@client.event
async def on_message_edit(before,after):
  if after.embeds:
    start_time = time.time()
    if after.author.id == 825617171589759006:
        try:
            emoji = after.embeds[0]. description.split(" ")[2]
            print('Sniped' + str(emoji))
            await after.add_reaction(emoji)
            end_time = time.time() - start_time
            await after.reply(f'Reacted {emoji} in  {end_time} seconds')
        except Exception as e:
            print(e)
            print("Couldnt solve game or wasnt valid")
        

client.run(Token)
