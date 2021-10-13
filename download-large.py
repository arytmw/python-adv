import requests

file_url = 'https://www.escaux.com/rsrc/EscauxCustomerDocs/DRD_T38Support_AdminGuide/T38_TEST_PAGES.pdf'

result = requests.get(file_url,stream=True)

with open('new.pdf','wb') as downloaded_file:
    for data in result.iter_content(chunk_size=1024):
        if data:
            downloaded_file.write(data)
