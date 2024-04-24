from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
STRING_SESSION = getenv("STRING_SESSION", None)
OWNER_ID = int(getenv("OWNER_ID", "5959548791"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "FRIENDS_LOVER_GROUP")
UPDATE_CHNL = getenv("UPDATE_CHNL", "ALL_SANATANI_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "V_VIP_OWNER")


