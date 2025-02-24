import logging
import logging.config

# Charges the config file into logging
logging.config.fileConfig("logging.conf")

# Get logger instances
logger = logging.getLogger()
