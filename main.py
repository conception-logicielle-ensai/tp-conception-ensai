from datetime import datetime
import pytz
import logging

logging.basicConfig(filename="traitement.log", encoding='utf-8', level=logging.DEBUG)
logging.info(f"Lancement du traitement")
timezone_paris = pytz.timezone('Europe/Paris')
timezone_reunion = pytz.timezone('Indian/Reunion')
def get_date_formatted(timezone):
    if timezone is None:
        raise ValueError("aucune timezone n'a été renseignée")
    logging.debug(f"Demande d'heure sur le timezone : {timezone}")
    date = datetime.now(timezone)
    return date.strftime("%H:%M:%S")
try:
    get_date_formatted(None) 
except ValueError as e:
    logging.error(e)
logging.info(f"result {get_date_formatted(timezone_reunion)}")