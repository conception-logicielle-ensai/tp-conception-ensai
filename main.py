from datetime import datetime
import pytz
import logging
import sys
import os
def get_fichier_sortie_args():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return "traitement.log"
def get_fichier_sortie_env():
    from dotenv import load_dotenv
    load_dotenv()
    local_env_path = ".env.local"
    if os.path.exists(local_env_path):
        load_dotenv(dotenv_path=local_env_path, override=True)
    if os.environ["CHEMIN_FICHIER_LOG"] is not None:
        return os.environ["CHEMIN_FICHIER_LOG"]
    return "traitement.log"
def get_fichier_sortie():
    return get_fichier_sortie_env()
logging.basicConfig(filename=get_fichier_sortie(), encoding='utf-8', level=logging.DEBUG)
logging.info(f"Lancement du traitement")
logging.debug(f"arguments : {sys.argv}")
#logging.debug(f"fichier log : {os.environ['CHEMIN_FICHIER_LOG']}")
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