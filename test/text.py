import asyncio

from aiostrike import Aiostrike
from aiostrike import JsonUtils

aiostrike = Aiostrike()


async def main(some_txt: str):
    x = await aiostrike.GetItemPrice(item_id=some_txt)
    json_o = JsonUtils(x).cvt_json()
    print(json_o)
    await aiostrike.close()


async def check_id(id: int):
    x = await aiostrike.GetInventoryValue(user_id=id)


loop = asyncio.get_event_loop()
loop.run_until_complete(main("AK-47 | Wasteland Rebel (Battle-Scarred)"))
