import json

import aiohttp

from .errors import ExceptionCheck
from .errors.exceptions import RateLimitted


class Aiostrike:
    def __init__(self):
        self.base_url = "http://csgobackpack.net/api"
        self.get_price_url = "http://csgobackpack.net/api/GetItemPrice"
        self.worth_url = "http://csgobackpack.net/api/GetInventoryValue/"
        self.get_item_list_url = "http://csgobackpack.net/api/GetItemsList/"
        header = {
        }
        self.session = aiohttp.ClientSession(headers=header, timeout=aiohttp.ClientTimeout(total=60))

    async def GetItemPrice(self, item_id: str, time: int = 7, extend: int = 0, full: int = 0,
                           currency: str = "USD", icon: int = 1, key: str = None):
        parameters = {
            "id": item_id,
            "time": time,
            "extend": extend,
            "full": full,
            "currency": currency,
            "icon": icon,
        }
        if key:
            parameters = {
                "id": item_id,
                "time": time,
                "extend": extend,
                "full": full,
                "currency": currency,
                "icon": icon,
                "key": key
            }
        async with self.session.get(self.get_price_url, params=parameters) as resp:
            ExceptionCheck(resp.status)
            data = await resp.read()
        x = json.loads(data.decode())
        try:
            x = x['success']
        except KeyError:
            return data.decode()
        if x != "exceeded maximum number of requests, try again in next hour":
            return data.decode()
        else:
            raise RateLimitted()

    async def GetInventoryValue(self, user_id: int, ref: int = 0, currency: int = "USD", key: str = None):
        parameters = {
            "id": user_id,
            "ref": ref,
            "currency": currency,

        }
        if key:
            parameters = {
                "id": user_id,
                "ref": ref,
                "currency": currency,
                "key": key
            }
        async with self.session.get(self.worth_url, params=parameters) as resp:
            ExceptionCheck(resp.status)
            data = await resp.read()
        x = json.loads(data.decode())
        try:
            x = x['success']
        except KeyError:
            return data.decode()
        if x != "exceeded maximum number of requests, try again in next hour":
            return data.decode()
        else:
            raise RateLimitted()

    async def GetItemList(self, key: str, details: int = None):
        parameters = {
            "key": key,
        }
        if details:
            parameters = {
                "key": key,
                "details": details,
            }
        async with self.session.get(self.get_item_list_url, params=parameters) as resp:
            ExceptionCheck(resp.status)
            data = await resp.read()
        x = json.loads(data.decode())
        try:
            x = x['success']
        except KeyError:
            return data.decode()
        if x != "exceeded maximum number of requests, try again in next hour":
            return data.decode()
        else:
            raise RateLimitted()

    async def close(self):
        return await self.session.close()
