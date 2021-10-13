import tarfile

filename = input("Enter tar file to read: ")

tar_content = tarfile.open(filename)

for item in tar_content.getnames():
    print(item)
