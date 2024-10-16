import logging
import os
import sys

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=LOGGING_LEVEL, stream=sys.stdout)