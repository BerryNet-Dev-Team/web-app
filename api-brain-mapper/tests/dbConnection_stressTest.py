import aiohttp
import asyncio

"""
IMPORTANT: DISABLE the auth decorator in endpoint '/auth/addUser'
"""

URL = "https://devserver.local/api/auth/addUser"

users = [
    {"name": f"User{i}", "lastName": f"Last{i}", "email": f"berry.net{i}@example.com", "passwd": "password123", "roleId": 1}
    for i in range(3)
]

async def add_user(session, user_data):
    async with session.post(URL, json=user_data) as response:
        resp_json = await response.json()
        print(f"User {user_data['email']}: {resp_json}")

async def main():
    connector = aiohttp.TCPConnector(ssl=False)  # Ignore SSL verification 
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [add_user(session, user) for user in users]
        await asyncio.gather(*tasks)

asyncio.run(main())


"""
-----How to check open db connections-----

SELECT pid, usename, state, query 
FROM pg_stat_activity
WHERE datname = 'db_name';
"""