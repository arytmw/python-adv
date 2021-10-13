import requests

file_url = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'

result = requests.get(file_url)

with open('python_logo.png','wb') as image:
    image.write(result.content)

#image = open('python_logo.png','w')
#image.write(result.content)
#image.close()
