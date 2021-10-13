from zipfile import ZipFile
import datetime

filename = input("Enter zip file to read: ")

zip_data = ZipFile(filename,'r')

for info in zip_data.infolist():
    print(info.filename)
    print(f'\tModified Time: {datetime.datetime(*info.date_time)}')
    print(f'\tCompressed Size: {info.compress_size} Bytes')
    print(f'\tUncompressed Size: {info.file_size} Bytes')
