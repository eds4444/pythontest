from aiogram import Bot, Dispatcher, executor, types

import python_weather

#boy init
bot = Bot ( token="5534697163:AAFgKVLh0YB8O9R5PEzEcRL-WCWe0NyvbS8")
dp = Dispatcher ( bot )
client = python_weather.Client( format=python_weather.IMPERIAL, locale="ru-RU")

#echo
@dp.message_handler()
async def echo( message: types.Message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = weather.location_name + "\n"
    resp_msg += f"Текущая температура: {celsius}\n"
    resp_msg += f"Состояние погоды: {weather.current.sky_text}"

    if celsius <= 10:
        resp_msg += "\nПрохладно"
    else:
        resp_msg += "\nТепло"

    await message.answer(resp_msg)

# run londg-polling

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)            

    







