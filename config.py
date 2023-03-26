# Copyright (C) 2023 DX_MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you are not deploying through buttons you can paste variable here
import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","")     

DB_URL = os.environ.get("DB_URL","")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get('PORT', '8080')

WEBHOOK = bool(os.environ.get("WEBHOOK", True))
