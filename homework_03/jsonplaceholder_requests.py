"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_users():
    async with ClientSession() as session:
        result = await fetch_json(session, USERS_DATA_URL)
    return result


async def fetch_posts():
    async with ClientSession() as session:
        result = await fetch_json(session, POSTS_DATA_URL)
    return result


async def main():
    await fetch_users()
    await fetch_posts()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
