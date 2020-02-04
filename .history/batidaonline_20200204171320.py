import webbrowser
import bs4

exampleFile = webbrowser.open('https://www.ahgora.com.br/batidaonline')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())

