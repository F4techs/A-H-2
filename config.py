from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv('TOKEN')
PLACEHOLDER = getenv('PLACEHOLDER')
CLEAR_CONTEXT_ANSWER = getenv('CLEAR_CONTEXT_ANSWER')
CONTEXT_SIZE = int(getenv('CONTEXT_SIZE'))
ALLOWED_IDS = list(map(lambda x: int(x.strip()), getenv('ALLOWED_IDS').split(',')))
START_PLACEHOLDER = getenv('START_PLACEHOLDER')

