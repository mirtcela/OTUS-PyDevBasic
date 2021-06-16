"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции):
- инициализация бд
- создание таблиц
- загрузка пользователей и постов
- добавление пользователей и постов в базу данных
- закрытие соединения с БД
"""
import asyncio

from homework_03.models import *


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_parents_with_children_opt1():
    async_session = Session

    async with async_session() as session:
        session: Session

        async with session.begin():
            # Пример кода для значений не из заглушек
            parent = Parent(name="John Smith")
            child_1 = Child(name="Sam")
            child_2 = Child(name="Ann")
            parent.children = [child_1, child_2]
            # Окончание примера кода
            session.add(parent)

async def main():
    await create_tables()


if __name__ == "__main__":
    asyncio.run(main())
