import asyncio
from util import delay
from util import async_timed
from asyncio import Future
import requests

#first comment

@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(10000000):
        counter += 1
    return counter

async def main() -> None:
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = 0.500
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


asyncio.run(main())








#
# import subprocess
# import json
# import yt_dlp
# import pprint
#
#
# URL = 'https://www.youtube.com/watch?v=eEvhaZTz-sk'
#
# # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
# ydl_opts = {}
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(URL, download=True)
#
#     # ℹ️ ydl.sanitize_info makes the info json-serializable
#     pprint.pprint(json.dumps(ydl.sanitize_info(info)))
#
#     print()
#     print()
#     print()
#
#
# #
# subprocess.run(["yt-dlp.exe", ""])
#
#
#
#
#






# import socket
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# address = ('', 8000)
# server_socket.bind(address)
#
# server_socket.listen()
#
# connections = []
#
# try:
#     while True:
#         connection, client_address = server_socket.accept()
#         print(f'получен запрос на подключение от {client_address}')
#         connection.sendall('*** напиши мне что нибудь...\n\n'.encode('utf-8'))
#
#         buffer = b''
#
#         while buffer[-2:] != b'\r\n':
#             data = connection.recv(2)
#             if not data:
#                 break
#             else:
#                 print(f'Получены данные: {data}', flush=True)
#                 buffer += data
#
#         print(f'Все данные {buffer}')
#         connection.sendall('чё ты там?\n\n'.encode('utf-8'))
#         connection.close()
#
# finally:
#     server_socket.close()



# @async_timed()
# async def cpu_bound_work() -> int:
#     counter = 0
#     for i in range(100000000):
#         counter += 1
#     return counter
#
#
# @async_timed()
# async def get_example_status() -> int:
#     return requests.get("https://www.google.com").status_code
#
#
# @async_timed()
# async def main():
#     task_1 = asyncio.create_task(get_example_status())
#     task_2 = asyncio.create_task(get_example_status())
#     task_3 = asyncio.create_task(get_example_status())
#
#     await task_1
#     await task_2
#     await task_3
#
#
# asyncio.run(main())
