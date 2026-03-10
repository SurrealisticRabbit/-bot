from util.discordbot import DiscordBot
from dotenv import load_dotenv
import os

load_dotenv()
_token = None

def _check() -> bool:
    wd = os.path.realpath('.\\')
    dotenv = os.path.join(wd, '.env')
    if os.path.exists(dotenv):
        return True
    return False

def main():    
    bot = DiscordBot()
    bot.run(_token)
    
if __name__ == "__main__":
    if _check():
        main()
    else:
        raise FileNotFoundError('.env file not found')
    
    

        