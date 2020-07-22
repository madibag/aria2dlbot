import requests


base_url = 'https://sjprojectsapi.herokuapp.com/torrent/?query='


async def magnet_link_s(client, message):
    search = message.text
    print(search)
    search = search.split(' ')
    search.remove('/Magnet')
    await message.reply_text("Searching Magnet...", quote=True)
    r = requests.get(base_url+str(search)).json()
    for num in r:
        message.reply_text(num['name'])
        message.reply_text(num['magnet'])
        message.reply_text(num['size'])
