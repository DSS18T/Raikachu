## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQFXJToAtePUy5I-tP7oTlQrScj3T0sK8i-MlqL_ttpWR-eGOx5yeMZddY9XLTzgQ1lpOBTC6uMfI8pNa3Xy9L9tBUUrk4S-EO69RVrQW15-VBf2Odvb4F_zzfJOzT7RErrul_lIUmzIJHPBQNwEJXoKHPuf7YhTMfJrzRZYZiTmGsXqRWrkZN_7GpVwqfq6EkFyGzLG7u7IqwaVfy6gg4rEdtUkjmpJsVRVdI2JDjcB378Ellq-U72SwCgVkLMb7gIkD7hLbl9IgT-dSGffPaYYzrxpG3RdEW5RivaKD7i3oPjnP_UkKuQy2E7YkFFzbKOpiZfuhLvqpnsTb76h_gEZ0tO0AgAAAAE0SgLcAA")
BOT_TOKEN = getenv("6096504724:AAFQkrzkkDQYn9Poo4EhLyuNqjz7RzJbpeE")
BOT_NAME = getenv("himikoXRobot")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Shubhanshu")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "YurikoPlugin")
BOT_USERNAME = getenv("himikoXRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("GOKUSUPPORTCHAT")
UPDATES_CHANNEL = getenv("GOKUUPADTES")
SUDO_USERS = list(map(int, getenv("5148561602 5148561602").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
