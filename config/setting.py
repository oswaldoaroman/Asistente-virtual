import os
from config.entorno import detectar_sesion
import logging
from pathlib import Path

corpus= Path.home() / "asistente-voz/corpus.txt"

def leer_corpus():
    with open(corpus, "r", encoding="utf-8") as f:
        logging.info("Corpus cargado")
        return [l.strip() for l in f if l.strip()]

MODELO = os.path.expanduser("~/.vosk/vosk-model-small-es-0.42")
PALABRA_ACTIVACION = "oye pc"
SESION = detectar_sesion()
TIEMPO_ACTIVO = 0
TIMEOUT = 5