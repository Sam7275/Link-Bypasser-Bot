# To get values from Environment (True/False)
Get_ENV = False

# Required if Get_ENV == False
Vars = [
    # Bot API Token
    "5637997865:AAFMP7KvewvdutE0mpv8T_YJi3qK4VLVcMY",
    # GdToT Crypt
    "NTdMdEVDOU5tVmJiSWNjS012T2gzQVFGV3Zrc1lsTmNaV20zMVg1Nkx2ST0%3D",
    # Laravel Session
    "eyJpdiI6IjJCWUpqZFI3TEN5MlRxek9MeGhXT0E9PSIsInZhbHVlIjoiS1UxTk5MTElNQm9LT01jY1RPaytPM2JZXC9sOGpZM0xZRU9PK3VMVk9CdTVkUmhueUFWcTJVWDU5ampjczZvU3ciLCJtYWMiOiJiYzJkYjBlNTAzMTc5MTBmMTA3ZTU2MDliMzUwMjA2NzdhNGUzZTFjMDJhYjM5MzA2ZDU2YjdkYmNjYzI3NWNjIn0%3D",
    # XSRF_TOKEN 
    "eyJpdiI6Ilh4T3dyczRKYktuNE81UzJVeldVdnc9PSIsInZhbHVlIjoiZExcL09uUlNqaVpiWWxZXC9hVjVvZHFmTm8wakRqRkpFaEk5VGg0K3hXV2l6UjMrcFhWOFZSVGw5a1ZpNnVPXC8yTiIsIm1hYyI6IjdhNDE0MDhjMTIyM2RkZTQ3MTExNDI3MzRhNTMwNjJkZGQxYzFlYWRiOGVjOGI3NTlmMjQzNTdmZDkyZTQ2MDIifQ%3D%3D",
    # KOLOP_CRYPT
    "YllTcUtiSHNzR0RBSGJoOXZpOGJhUXd3a1lrSTYzRGNhMzA2MExFSFlKYz0%3D",
    # DRIVEFIRE_CRYPT
    "YllTcUtiSHNzR0RBSGJoOXZpOGJhUXd3a1lrSTYzRGNhMzA2MExFSFlKYz0%3D",
    # HUBDRIVE_CRYPT
    "UGEzSmpJeXFvZzhHVU5lUTQrUlBFcnRtSDE3V095YXVwRWVSVHJYb0UxZz0%3D",
    # KATDRIVE_CRYPT
    "a3BMWXAzRXByYm03bXR0dHArN21vcDlRa3JSYXUyTjU0djlFSFdpQkJzST0%3D",
    # UPTOBOX_TOKEN
    ""
]

APIs = [
    "https://us-central1-my-apps-server.cloudfunctions.net/r?shortid=",
    "https://api.emilyx.in/api",
    "https://api.bypass.vip/",
    "https://api.gofile.io"
]

import os
import logging as log

# Setup Logger
log.basicConfig(level=log.INFO, filename='runtime-log.txt',format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8')

def check():
    if not Vars[0]:
        log.error("Bot API Token not found!")
        raise ValueError('Bot API Token cannot be empty!')
    else:
        log.info("Found Bot API Token.")

    if not Vars[1]:
        log.warning("GdToT Crypt not provided!")
    else:
        log.info("Found GdToT Crypt.")

    if not Vars[2]:
        log.warning("Laravel Session not provided!")
    else:
        log.info("Found Laravel Session.")

    if not Vars[3]:
        log.warning("XSRF_TOKEN not provided!")
    else:
        log.info("Found XSRF_TOKEN.")

    if not Vars[4]:
        log.warning("KOLOP_CRYPT not provided!")
    else:
        log.info("Found KOLOP_CRYPT.")

    if not Vars[5]:
        log.warning("DRIVEFIRE_CRYPT not provided!")
    else:
        log.info("Found DRIVEFIRE_CRYPT.")

    if not Vars[6]:
        log.warning("HUBDRIVE_CRYPT not provided!")
    else:
        log.info("Found HUBDRIVE_CRYPT.")

    if not Vars[7]:
        log.warning("KATDRIVE_CRYPT not provided!")
    else:
        log.info("Found KATDRIVE_CRYPT.")

    if not Vars[8]:
        log.warning("UPTOBOX_TOKEN not provided!")
    else:
        log.info("Found UPTOBOX_TOKEN.")

    if Get_ENV == False:
        log.info("Got Values from config file!")
    else:
        log.info("Got Values from System Environment!")

if Get_ENV == False:
    log.info("Getting Values from config file...")
    check()
elif Get_ENV == True:
    log.info("Getting Values from System Environment...")
    TOKEN = os.environ.get("TOKEN","")
    GDTot_Crypt = os.environ.get("Crypt","")
    Laravel_Session = os.environ.get("Laravel_Session","")
    XSRF_TOKEN = os.environ.get("XSRF_TOKEN","")
    KCRYPT = os.environ.get("KOLOP_CRYPT","")
    DCRYPT = os.environ.get("DRIVEFIRE_CRYPT","")
    HCRYPT = os.environ.get("HUBDRIVE_CRYPT","")
    KATCRYPT = os.environ.get("KATDRIVE_CRYPT","")
    UPTOBOX = os.environ.get("UPTOBOX_TOKEN","")

    Vars = [
        TOKEN,
        GDTot_Crypt,
        Laravel_Session,
        XSRF_TOKEN,
        KCRYPT,
        DCRYPT,
        HCRYPT,
        KATCRYPT,
        UPTOBOX
    ]
    check()
else:
    log.error(r"Unable to undestand from where to get values?¯\_(ツ)_/¯")
    raise ValueError("Get_ENV value is invalid & should be True or False only!")
