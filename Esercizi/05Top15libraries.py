# Questo file prende spunto dal video https://www.youtube.com/watch?v=o06MyVhYte4
# Le top 15 librerie utili in python

'''
1) Pendulum https://pendulum.eustace.io/
Serve per visualizzare le date in  modo smart
Permette di gestire date, tempo, differenze di tempo, fusi orari...
'''

#import pendulum
#now = pendulum.now("Europe/Paris")
## Changing timezone
#now.in_timezone("Europe/Rome")
## Default support for common datetime formats
#now.to_iso8601_string()
#days2 = now.add(days=2).format('YYYY-MM-DD')
#
## Shifting
#print(days2)

'''
2) pypdf https://pypi.org/project/pypdf/
Free opensource
Legge, splitta, aggiunge pagine
'''
# from pypdf import PdfReader
# reader = PdfReader("FilesDati\\SCB Qlik.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()
# print(text[0:63])


'''
3) icecream: https://pypi.org/project/icecream/
Serve per fare debug.
Al posto di print si usa ic per fare la stampa della istruzione con risultato
'''
# from icecream import ic
# a: int = 4
# b: int = 5
# ic(a+b)

'''
4) loguru: https://github.com/Delgan/loguru
Serve per fare logs

Per leggere i logs: https://betterstack.com/
Lo spiega nel video: https://www.youtube.com/watch?v=y8qLhov8QU8
'''
from loguru import logger
import sys

logger.remove(0)
# rotation="500 MB": Max size oppure "12:00" o ancora "1 week"
# Possibile opzione: #compression="zip", 
# Extra serve per inserire informazioni aggiuntive come nel childLogger.bind oppure direttamente in logger.info() o altri metodi
# serialize = true   permette di avere output in json
logger.add(sys.stderr, serialize=True ,format="<green>{time}</green> | {level} | {module}: {line} {message} | {extra}")
# lg.add("FilesDati\\log_loguru.txt", format="{time} {level} {message}", filter="my_module", level="INFO") # Files di log
# lg.add(sys.stderror)

logger.info("Message INFO!", feature="f-strings")
logger.trace("Message TRACE!")
logger.debug("Message DEBUG!")
logger.success("Message SUCCESS!")
logger.warning("Message WARNING!")
logger.error("Message ERROR!")
logger.critical("Message CRITICAL!")

childLogger = logger.bind(seller = "01", product="Prova")
childLogger.info("Aperto nuovo prodotto")

# Molto utile il decoratore che analizza il problema

@logger.catch
def divisione(x: int):
    '''Divide 50 per un numero'''
    y= 50/x
    return y

divisione(5)



'''
4b) logging: https://docs.python.org/3/library/logging.html
Serve per fare logs.
E' possibile anche mandare il messaggio su un sistema in cloud di logging come PAPERTRAIL (https://www.papertrail.com/)
Video in questione https://www.youtube.com/watch?v=pxuXaaT1u3k
'''
# import logging
# def main():
#     logging.basicConfig(
#         #filename='FilesDati\\myapp.log',    # Dove stampare il login 
#         level=logging.DEBUG,
#         format= "%(asctime)s %(levelname)s %(message)s",
#         datefmt= "%Y-%m-%d %H:%M:%S"
#     )
#     logging.debug("Message of Debug")
#     logging.info("Message of Info")
#     logging.warning("Message of Warning")
#     logging.error("Message of Error")
#     logging.critical("Message of Critical")


# if __name__=="__main__":
#     main()


'''
5) Rich: https://rich.readthedocs.io/en/stable/introduction.html
Permette di mandare a schermo del testo formattato con colori ed effetti diversi comprese 
tabelle, markdown
Ma anche input formattati in modo gradevole
Ma anche interessantissimi progress bar
'''
# from rich.console import Console
# from rich.text import Text
# from rich.table import Table

# console = Console()
# text = Text("Hello, World!")
# text.stylize("bold magenta", 0, 6)
# console.print(text)

# MARKDOWN = """
# # This is an h1

# Rich can do a pretty *decent* job of rendering markdown.

# 1. This is a list item
# 2. This is another list item
# """
# from rich.console import Console
# from rich.markdown import Markdown

# console = Console()
# md = Markdown(MARKDOWN)
# console.print(md)

# table = Table(title="Star Wars Movies")

# table.add_column("Released", justify="right", style="cyan", no_wrap=True)
# table.add_column("Title", style="magenta")
# table.add_column("Box Office", justify="right", style="green")

# table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
# table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
# table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
# table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

# console = Console()
# console.print(table)

# from rich.prompt import Prompt
# name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")
# from rich.prompt import Confirm
# is_rich_great = Confirm.ask("Do you like rich?")
# assert is_rich_great

# import time

# from rich.progress import Progress

# with Progress() as progress:

#     task1 = progress.add_task("[red]Downloading...", total=1000)
#     task2 = progress.add_task("[green]Processing...", total=1000)
#     task3 = progress.add_task("[cyan]Cooking...", total=1000)

#     while not progress.finished:
#         progress.update(task1, advance=0.5)
#         progress.update(task2, advance=0.3)
#         progress.update(task3, advance=0.9)
#         time.sleep(0.02)

'''
6) argparse: https://docs.python.org/3/library/argparse.html
Permette di fare il parsing di un programma a line di comando
'''
# import argparse
# parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
# parser.print_help()

'''
7) tqdm: https://pypi.org/project/tqdm/
Crea delle progress bar per progressione su dataframe o array
'''

# from tqdm import tqdm
# from time import sleep
# for i in tqdm(range(10000)):
#     sleep(0.02)

'''
8) xarray come pandas ma per array multidimensionali. Lavora bene con numpy e scientific python
9) Polars per dataframe: https://pola.rs/
10) seaborn per visualizzare dati statistici
11) result https://pypi.org/project/result/
E' una alternativa al error using exception
'''
# from result import Result, Ok, Err

# def divide(a: int, b: int) -> Result[int, str]:
#     if b == 0:
#         return Err("Cannot divide by zero")
#     return Ok(a // b)

# values = [(10, 0), (10, 5)]
# for a, b in values:
#     match divide(a, b):
#         case Ok(value):
#             print(f"{a} // {b} == {value}")
#         case Err(e):
#            print(e)

'''
12) pydantic: https://docs.pydantic.dev/latest/
Permette di analizzare l'input in maniera molto formale
Per altro utilizzata in molte librerie
13) FastAPI
14) SQLModel: https://sqlmodel.tiangolo.com/
Permette di interagire con i database tramite una interfaccia python senza sql
15) httpx
'''
