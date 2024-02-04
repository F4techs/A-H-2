from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = getenv('TOKEN')
CLEAR_CONTEXT_ANSWER = getenv('CLEAR_CONTEXT_ANSWER')
CONTEXT_SIZE = int(getenv('CONTEXT_SIZE'))
START_PLACEHOLDER = getenv('START_PLACEHOLDER')

