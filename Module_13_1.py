import asyncio


async def start_strongman(name,power):
   max_ball_number = 6
   print(f'{name} начал соревнования')
   for i in range(1,max_ball_number):
       await asyncio.sleep(1/power)
       print(f'Силач {name} поднял шар №{i}')
   print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Vasya', 3))
    task2 = asyncio.create_task(start_strongman('Petya', 4))
    task3 = asyncio.create_task(start_strongman('Kolya', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
