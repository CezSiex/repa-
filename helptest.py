import os
TOKEN = os.environ.get('BOT_TOKEN') # bot token

POST_ID = 696078729277079662 # post id to read reactions from

# roles list according to emotes
ROLES = {
	'🐍': 696069525203845241, # python developer
	'👾': 696069420707086396, # Геймер
	'♣️': 696064368332243076, # CHOSEN
	'⚙️': 696071807903596674 # Helper

}

# exlcude this roles from counting
EXCROLES = {}

MAX_ROLES_PER_USER = 1 # max ammount of roles a user can have 


