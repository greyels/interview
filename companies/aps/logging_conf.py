import logging

# Create a logger instance with a specific name
logger = logging.getLogger("aps")

# Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger.setLevel(logging.DEBUG)

# Create a FileHandler to save logs to a file
file_handler = logging.FileHandler("eqrthquake.log")

# Define a log format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the FileHandler to the logger
logger.addHandler(file_handler)
