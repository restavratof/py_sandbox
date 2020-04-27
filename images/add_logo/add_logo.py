from PIL import Image
import os

IN_DIR = 'inbox'
OUT_DIR = 'result'
LOGO_FILENAME = 'logo.png'

IN_FILENAME = 'pic1.png'

#################################################################################
# Check logo file
if os.path.exists(LOGO_FILENAME) and os.path.isfile(LOGO_FILENAME):
    print('OK: Logo file ({}) exist.'.format(LOGO_FILENAME))
else:
    print('ERROR: Logo file ({}) must be near the script!'.format(LOGO_FILENAME))
    exit(99)

# Check IN directory
if os.path.exists(IN_DIR) and os.path.isdir(IN_DIR):
    print('OK: Inbox directory ({}) exist.'.format(IN_DIR))
else:
    print('ERROR: Inbox directory ({}) must be near the script!'.format(IN_DIR))
    exit(99)


#################################################################################
# Get logo parameters
logoIm = Image.open(LOGO_FILENAME)
# print(logoIm)
logoWidth, logoHeight = logoIm.size
print('LOGO width:{}  height:{}'.format(logoWidth, logoHeight))

# Check/prepare RESULT directory
print('Preparing result directory ({})...'.format(OUT_DIR))
if os.path.exists(OUT_DIR) and os.path.isdir(OUT_DIR):
    print(' *** WARNING: Result directory ({}) already exists.'.format(OUT_DIR))
    if not os.listdir(OUT_DIR):
        print(' *** OK: The directory is empty.')
    else:
        print(' *** ERROR: The directory contains files!')
        print('            Clean out directory and run script again.')
else:
    print(' *** Creating result directory ({})'.format(OUT_DIR))
    os.mkdir(OUT_DIR)
    print(' *** Done')


#################################################################################
# Go through files inbox INBOX directory
print('Reading files in inbox directory ({})...'.format(IN_DIR))
for fname in os.listdir(IN_DIR):
    # Check if a file
    if os.path.isfile(os.path.join(IN_DIR, fname)) and fname.lower().endswith(('.png', '.jpg', '.jpeg')):
        print(' *** File ({})'.format(fname))
        in_image = Image.open(os.path.join(IN_DIR, fname))
        # print(in_image)
        width, height = in_image.size
        print('     *** width:{}  height:{}'.format(width, height))
        print('     *** Adding logo...')
        out_image = in_image.copy()
        out_image.paste(logoIm, (0, height - logoHeight), logoIm)
        out_image.save(os.path.join(OUT_DIR, fname))


    else:
        print('WARNING: Proceed only pictures with extentions: png, jpg, jpeg. Skip file ({})'.format(fname))

exit(1)









