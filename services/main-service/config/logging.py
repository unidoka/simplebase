import logging
import sys

def setup_logging():

    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='Y-m-d H:i:s',
        handlers=[
            logging.FileHandler('storage/logs/app.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

    return logging.getLogger(__name__)


# Использование

# from config.logging import setup_logging
#
# logger = setup_logging()
# logger.info("123123")