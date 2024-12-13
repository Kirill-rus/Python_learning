# Выполнение задания на тему "асинхронность на практике" - "асинхронные силачи".

# Импорт библиотеки асинхронности.
import asyncio


async def start_strongman(name, power):         # Описание поднятие силачом шара.
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():                  # Описание всего турнира.

    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    await task1  # Ожидание выполнения задач.
    await task2
    await task3

asyncio.run(start_tournament()) # Запуск выполнения всех асинхронных задач.
