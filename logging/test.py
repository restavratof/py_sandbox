import sys
import logging

my_format = '%(asctime)s - %(process)d - %(name)s - %(levelname)8s - %(filename)s - %(funcName)s - %(message)s'
# logging.basicConfig(level=logging.INFO, stream=sys.stdout, format=my_format, datefmt='%d-%b-%y %H:%M:%S')
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format=my_format, datefmt='%d-%b-%y %H:%M:%S')


logging.info('test 1111')
logging.error('test 1111')
logging.warning('test 1111')
logging.debug('test 1111')
