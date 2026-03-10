from util.alphabot import AlphaBot
from dotenv import load_dotenv
import os

load_dotenv()
_token = None

def _check() -> bool:
    wd = os.path.realpath('.\\')
    dotenv = os.path.join(wd, '.env')
    if os.path.exists(dotenv):
        global _token
        _token = os.getenv("DISCORD_TOKEN")
        return True
    return False

def main():
    global _token
    bot = AlphaBot()
    bot.run(_token)
    
if __name__ == "__main__":
    if _check():
        main()
    else:
        raise FileNotFoundError('.env file not found')
    
    

        