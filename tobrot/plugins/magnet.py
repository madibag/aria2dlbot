import requests


base_url = 'https://sjprojectsapi.herokuapp.com/torrent/?query='


async def magnet_link_s(client, message):
    search = message.text
    print(search)
    if len(search) > 1:
        search = search.split(' ')
        search.remove('/Magnet')
        await message.reply_text("Searching Magnet...", quote=True)
        r = requests.get(base_url+str(search)).json()
        for num in r:
            await message.reply_text(num['name'])
            await message.reply_text(num['magnet'])
            await message.reply_text(num['size'])
    else:
        pass
