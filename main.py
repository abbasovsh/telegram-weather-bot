import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Assalom alaykum va rohmatullohi va barokatuh! If you want to know the weather information of your city, please enter the name of your city: ")


@dp.message_handler()
async def get_weather(message: types.Message):
    

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()


        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        duration_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])


        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%M-%D %H:%M')}***\n"
              f"Weather of today: {city}\nTemperature: {cur_weather} C°\n"
              f"Humidity: {humidity}%\nPressure: {pressure} Pascal\nWind: {wind} m/s\n"
              f"Sunrise time: {sunrise_time}\nSunset time: {sunset_time}\nDuration of day: {duration_of_day}\nGood day!"
            )


    except:
        await message.reply("Please enter correctly: ")
        

if __name__ == "__main__":
    executor.start_polling(dp)
