# Loggers       - expose the interface that application code directly uses.
# Handlers      - send the log records (created by loggers) to the appropriate destination.
# Filters       - provide a finer grained facility for determining which log records to output.
# Formatters    - specify the layout of log records in the final output.
import sys
import logging

my_format = '%(asctime)s - %(process)d - %(name)s - %(levelname)8s - %(filename)s - %(funcName)s - %(message)s'
# logging.basicConfig(level=logging.INFO, stream=sys.stdout, format=my_format, datefmt='%d-%b-%y %H:%M:%S')
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format=my_format, datefmt='%d-%b-%y %H:%M:%S')


logging.info('test 1111')
logging.error('test 1111')
logging.warning('test 1111')
logging.debug('test 1111')
