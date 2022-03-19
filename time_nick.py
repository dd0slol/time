#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pickle
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import os
import pytz
import datetime
from datetime import datetime
tz_NY = pytz.timezone('Europe/Moscow')
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M"))

app = Client('cmd', api_id=13406787, api_hash='ed12c1b7a3e3617e62ff6e2ffbc0b15b')

app.start()

app.stop()


if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
            
@app.on_message(filters.command('start_time', prefixes='.') & filters.me)
def time_bot(_, msg):
    tz_NY = pytz.timezone('Europe/Moscow')
    datetime_NY = datetime.now(tz_NY)
    msg.edit('<b>Запущен Auto-name-time бот, ожидайте</b>')
    sleep(2)
    while True:
        sleep(0.1)
        msg.edit('<b>Запущен!</b>')
        while True:
            sleep(60)
            count = app.get_chat_members_count(chat_id=Айди чата для кол-ва участников)
            tz_NY = pytz.timezone('Europe/Moscow')
            datetime_NY = datetime.now(tz_NY)
            app.update_profile(first_name=f"ᅠᅠ : {datetime_NY.strftime('%H:%M')} ",
                               bio=f"Autobio [{count}]")

app.run()
