# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# type(res)
# # <class 'requests.models.Response'>
# res.status_code == requests.codes.ok
# # True
# len(res.text)
# # 178981
# print(res.text[:2500])
# # The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
playFile.write(chunk)
# 100000
# 78981
playFile.close()