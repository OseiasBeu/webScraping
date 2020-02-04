import webbrowser

webbrowser.open('http://www.google.com/')


#! python3
# mapIt.py – Inicia um mapa no navegador usando um endereço da
# linha de comando ou do clipboard.
import webbrowser, sys
if len(sys.argv) > 1:
  # Obtém o endereço da linha de comando.
  address = ' '.join(sys.argv[1:])