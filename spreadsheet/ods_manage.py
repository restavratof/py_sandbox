from pyexcel_ods import save_data, get_data
from collections import OrderedDict
import os
import json
import io
from io import StringIO

# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO

fileName = "test.ods"

######################################################
# Remove file if exists
if os.path.isfile(fileName):
    print('File ({}) already exists. Removing...'.format(fileName))
    os.unlink(fileName)
    print(' *** Done.\n')

######################################################
# Create ODS document
print('Creating file ({})...'.format(fileName))
data = OrderedDict()
data.update({"Sheet 1":[[1,2,3],[4,5,6]]})
data.update({"Sheet 2":[["row 1", "row 2", "row 3"]]})
save_data(fileName, data)
print(' *** Done.\n')

######################################################
# Read from ODS
print('Reading from file...')
data = get_data(fileName)
print(json.dumps(data))
print(' *** Done.\n')

######################################################
# Updating ODS file
print('Updating file...')
data = get_data(fileName)
data.update({"Sheet 3":[["test1", "test2", "test3"]]})
save_data(fileName, data)
print(json.dumps(data))
print(' *** Done.\n')

######################################################
# Write an ods file to memory
print('Writing ODS file to memory...')
data = OrderedDict()
data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
data.update({"Sheet 2": [[7, 8, 9], [10, 11, 12]]})
io = StringIO()
save_data(io, data)
# do something with the io
# In reality, you might give it to your http response
# object for downloading
print(' *** Done.\n')

######################################################
# Read from an ods from memory
print('Reading ODS file from memory...')
# This is just an illustration
# In reality, you might deal with ods file upload
# where you will read from requests.FILES['YOUR_ODS_FILE']
data = get_data(io)
print(json.dumps(data))
print(' *** Done.\n')

