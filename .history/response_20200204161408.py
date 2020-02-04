import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
# <class 'requests.models.Response'>
res.status_code == requests.codes.ok
# True
len(res.text)
# 178981
print(res.text[:250])
# The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare