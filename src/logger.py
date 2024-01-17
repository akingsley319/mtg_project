import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_$S')}.log"
# will create logs folder and find location
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# tells code to append file even though it exists already
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# whenever use "logging.info" it will use this basic config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Test case
if __name__=="__main__":
    logging.info("Logging has started")