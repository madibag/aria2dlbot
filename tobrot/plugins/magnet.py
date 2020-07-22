import requests


base_url = 'https://sjprojectsapi.herokuapp.com/torrent/?query='


async def magnet_link_s(client, message):
    search = message.command
    search = search.remove('Magnet')
    await message.reply_text("Searching Magnet...", quote=True)
    r = requests.get(base_url+search[1]).json()
    for num in r:
        message.reply_text(r[num]['name'])
        message.reply_text(r[num]['magnet'])
        message.reply_text(r[num]['size'])