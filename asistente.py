import logging
logger  = logging.getLogger(__name__)

import queue
import json
from vosk import Model, KaldiRecognizer
from config import SAMPLE_RATE,MODELO,SESION

class AsistenteVoz:
    def __init__(self):
        self.activo = False
        self.tiempo_activacion = 0
        self.TIMEOUT = 5

        self.q = queue.Queue()
        self.sesion=SESION
        self.COMANDOS= self.leercomandos()
        self.MODOS=self.leerModos()
        
        with open("corpus.txt") as f:
            corpus = [l.strip() for l in f if l.strip()]

        #print("Cargando modelo...")
        self.model = Model(MODELO)
        self.rec = KaldiRecognizer(self.model, SAMPLE_RATE, json.dumps(corpus))

    def callback(self, indata, frames, time, status):
        if status:
            print(status)
            logging.error("Error en el callback del microfono")
        self.q.put(bytes(indata))

    def leercomandos(self):
        with open("comandos.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        if((self.sesion!="hyprland" and 
            self.sesion!="wayland") and 
            self.sesion=="x11"):
            with open("qtile.json","r", encoding="utf-8") as comands:
                comandsSesion=json.load(comands)
                logging.info("Backend de comandos cargado: Qtile")
        else:
            with open("hyprland.json","r", encoding="utf-8") as comands:
                comandsSesion=json.load(comands)
                logging.info("Backend de comandos cargado: Hyprland")
            

        COMANDOS = {
            **data["SONIDO"],
            **data["LANZARAPP"],
            **data["MULTIMEDIA"],
            **comandsSesion["NAVEGACION"],
            **comandsSesion["VENTANAS"],
        }

        return COMANDOS
    
    def leerModos(self):
        with open("MODOS.json", "r", encoding="utf-8") as f:
            MODOS = json.load(f)
        return MODOS


