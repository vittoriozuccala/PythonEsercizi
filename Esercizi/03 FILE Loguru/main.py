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