import requests


base_url = 'https://sjprojectsapi.herokuapp.com/torrent/?query='


async def magnet_link_s(client, message):
    search = message.text
    search = search.split(' ')
    search.remove('/Magnet')
    str1 = ""
    for ele in search:  
        str1 += ele
    await message.reply_text("Searching Magnet...", quote=True)
    r = requests.get(base_url+str1).json()
    for num in r:
        message.reply_text(r[num]['name'])
        message.reply_text(r[num]['magnet'])
        message.reply_text(r[num]['size'])
