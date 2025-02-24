import logging
import os
from datetime import datetime

# Define log directory
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure the "logs" directory exists

# Define log file name with timestamp
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,  # Default logging level
    format="[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s" # Log format,

)
