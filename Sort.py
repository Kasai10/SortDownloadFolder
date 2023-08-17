import os
import shutil
import mimetypes

user_home = os.path.expanduser("~")

# Construct the path to the user's Downloads folder
DOWNLOAD_DIRECTORY = os.path.join(user_home, "Downloads")
TEXT_DIRECTORY = DOWNLOAD_DIRECTORY + '\Textfiles'
PDF_DIRECTORY = DOWNLOAD_DIRECTORY + '\PDFfiles'
IMG_DIRECTORY = DOWNLOAD_DIRECTORY + '\IMGfiles'
ZIP_DIRECTORY = DOWNLOAD_DIRECTORY + '\ZIPfiles'
MP4_DIRECTORY = DOWNLOAD_DIRECTORY + '\MP4files'
MP3_DIRECTORY = DOWNLOAD_DIRECTORY + '\MP3files'
OTHER_DIRECTORY = DOWNLOAD_DIRECTORY + '\Other'

files_to_exclude = ['IMGfiles', 'MP3files', 'MP4files', 'Other', 'PDFfiles', 'Textfiles', 'ZIPfiles']

files = os.listdir(DOWNLOAD_DIRECTORY)
for file in files_to_exclude:
    files.remove(file)

for entry in files:
    type, _ = mimetypes.guess_type(entry)
    

    if type == 'text/plain':
        if os.path.exists(TEXT_DIRECTORY):
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, TEXT_DIRECTORY)
        else:
            os.mkdir(TEXT_DIRECTORY)
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, TEXT_DIRECTORY)
    
    elif type == 'application/pdf':
        if os.path.exists(PDF_DIRECTORY):
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, PDF_DIRECTORY)
        else:
            os.mkdir(PDF_DIRECTORY)
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, PDF_DIRECTORY)

    elif type == 'image/jpeg' or type == 'image/png' or type == 'image/gif':
        if os.path.exists(IMG_DIRECTORY):
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, IMG_DIRECTORY)
        else:
            os.mkdir(IMG_DIRECTORY)
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, IMG_DIRECTORY)

    elif type == 'application/x-zip-compressed':
        if os.path.exists(ZIP_DIRECTORY):
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, ZIP_DIRECTORY)
        else:
            os.mkdir(ZIP_DIRECTORY)
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, ZIP_DIRECTORY)
    
    elif type == 'audio/mpeg':
        if os.path.exists(MP3_DIRECTORY):
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, MP3_DIRECTORY)
        else:
            os.mkdir(MP3_DIRECTORY)
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, MP3_DIRECTORY)

    elif type == 'video/mp4':
        if os.path.exists(MP4_DIRECTORY):
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, MP4_DIRECTORY)
        else:
            os.mkdir(MP4_DIRECTORY)
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, MP4_DIRECTORY)                

    else:
        if os.path.exists(OTHER_DIRECTORY):
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, OTHER_DIRECTORY)
        else: 
            os.mkdir(OTHER_DIRECTORY)
            shutil.move(DOWNLOAD_DIRECTORY + '\\' + entry, OTHER_DIRECTORY)
