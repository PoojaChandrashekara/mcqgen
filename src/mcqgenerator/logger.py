import logging
import os
from datetime import datetime

#file name
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log" #used to log the time of execution at that particular date and time

#folder path
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

#create log file in the logs folder
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO,
        filename=LOG_FILE_PATH,
        format='%(asctime)s -%(lineno)d %(name)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S')