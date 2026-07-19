import os
from config.entorno import detectar_sesion

MODELO = os.path.expanduser("~/.vosk/vosk-model-small-es-0.42")
PALABRA_ACTIVACION = "oye pc"
SESION = detectar_sesion()
TIEMPO_ACTIVO = 0
TIMEOUT = 5