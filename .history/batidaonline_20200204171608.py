import webbrowser
import bs4

exampleFile = webbrowser.open('https://www.ahgora.com.br/batidaonline')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#account_i')
print(str(elems[0].getText()))

