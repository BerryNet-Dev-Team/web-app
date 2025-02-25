import logging
import logging.config
from pathlib import Path

# Charges the config file into logging
confFile_path = (Path(__file__).parent / "logging.conf").resolve()
logging.config.fileConfig(str(confFile_path))

# Deactivate werkzeug propagation
logging.getLogger("werkzeug").propagate = False

# Get logger instances
logger = logging.getLogger()
