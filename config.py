import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5127131547:AAFlH9vA_oNcqwQi985TzBRSyAL9svrYCrs")
API_ID = int(os.environ.get("API_ID", "17378766"))
API_HASH = os.environ.get("API_HASH", "64363ed3e29119c36ff4ef28deac8645")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001600759370"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1607263889").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://harshit:harshit@cluster0.ry72g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
