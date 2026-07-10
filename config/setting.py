import os
from speech.audio import detectarSesion

MODELO = os.path.expanduser("~/.vosk/vosk-model-small-es-0.42")
PALABRA_ACTIVACION = "oye pc"
SESION = detectarSesion()
TIEMPO_ACTIVO = 0
TIMEOUT = 5