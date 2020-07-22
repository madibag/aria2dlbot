import requests


base_url = 'https://sjprojectsapi.herokuapp.com/torrent/?query='


async def magnet_link_s(client, message):
    search = message.text
    print(search)
    search = search.split(' ')
    if len(search) > 1:
        search.remove('/Magnet')
        await message.reply_text("Searching Magnet...", quote=True)
        r = requests.get(base_url+str(search)).json()
        num = 0
        while num < 10:
            await message.reply_text(r[num]['name']+'\n'r[num]['size']'\n'+r[num]['magnet'])
            num+=1
    else:
        pass
