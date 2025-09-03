import sys
import logging
from loguru import logger

LOG_FORMAT = (
    "<level>{level: <3} | "
    "{message}</level>"
    "<white> - {name} : {function} : {line}</white>"
)

logger.remove()
logger.add(
    sys.stderr,
    format=LOG_FORMAT,
    colorize=True,
    level="INFO",
    backtrace=True,
    diagnose=True
)


class InterceptHandler(logging.Handler):
    IGNORE = (
        "cryptg detected, it will be used for encryption",
        "Failed to load SSL library",
        "Connecting to", "Connection to",
        "Start polling", "Run polling for bot",
        "Update id="
    )

    def emit(self, record):
        message = record.getMessage()
        if any(ig in message for ig in self.IGNORE):
            if "Run polling for bot" in message:
                log.info("BOT STARTED!")
            return
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        logger.opt(
            depth=6,
            exception=record.exc_info,
            ansi=True,
            lazy=True
        ).log(level, message)

logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO, force=True)

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

start_banner = r'''

!   ___  ____                         __          __                
!  |_  ||_  _|                       [  |        [  |  _            
!    | |_/ /    .--.   _   __  ,--.   | |  .--.   | | / ]   _   __  
!    |  __'.  / .'`\ \[ \ [  ]`'_\ :  | | ( (`\]  | '' <   [ \ [  ] 
!   _| |  \ \_| \__. | \ \/ / // | |, | |  `'.'.  | |`\ \   \ '/ /  
!  |____||____|'.__.'   \__/  \'-;__/[___][\__) )[__|  \_][\_:  /   
!                                                          \__.'     '''
start_info=f'''-----------------------------------------------
•   version: None
•   bot name: telegram-bot-cobalt
•   developer: devKovalsky
-----------------------------------------------




'''

print(start_banner, start_info, sep="\n")

