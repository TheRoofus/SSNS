# -*- coding=utf-8 -*-

import time
from typing import Tuple, Union

import aiohttp
import asyncio


async def main(url: str = None, close_session: bool = False) -> Union[bool, Tuple[int, str]]:
    """
    Method GET returt page after request url.
    After to work properly status is "OK" (200) and DOM.

    :param close_session: Close session.
    :param url: Target URL for request.
    :return: Method is print two state resp.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # session.post(url, data=b'data')
            # session.put(url, data=b'data')
            # session.delete(url)
            # session.head(url)
            # session.options(url)
            # session.patch(url, data=b'data')
            if close_session:
                await session.close()
                return True

            return resp.status, await resp.text()


def _loop(url: str) -> Tuple[int, str]:
    """
    This function will always return the running event loop.

    :param url: Target URL for request.
    :return: Return the Future's result, or raise its exception.
    """
    loop = asyncio.get_event_loop()
    ll = loop.run_until_complete(main(url))
    return ll


async def _close_session(workflow_runtime: bool = False, time_close: int = None) -> str:
    """
    This function will be always close session.

    :param workflow_runtime: This flag will be use for timeout check.
    :param time_close: Is take argument (sec) for timeout.
    :return: status "OK"

    :raise: False
    """
    # ToDo Добавить обертку над ошибками.
    if workflow_runtime:
        if time_close >= 1:
            time.sleep(time_close)
        else:
            return 'Введенное время - неверно.'

    await main(close_session=True)

    return "OK"
