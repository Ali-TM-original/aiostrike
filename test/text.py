import asyncio

from aiostrike import Aiostrike
from aiostrike import JsonUtils

aiostrike = Aiostrike()


async def main(some_txt: str):
    x = await aiostrike.GetItemPrice(item_id=some_txt)
    json_o = JsonUtils(x).cvt_json()
    print(json_o)
    await aiostrike.close()


async def check_id():
    x = await aiostrike.GetInventoryValue(1234567890)  # Some Random Steam ID
    json_o = JsonUtils(x).cvt_json()
    print(json_o['success'])
    await aiostrike.close()


async def text_two():
    x = await aiostrike.GetItemList("A key", details=1)  # Some Random KEY
    json_o = JsonUtils(x).cvt_json()
    print(json_o)
    await aiostrike.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(text_two())
