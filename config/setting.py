import os
from speech.audio import detectarSesion

#nombreMicrofono="GENERAL WEBCAM: USB Audio"
#nombreBocina="SSS USB Speaker: Audio"
# Configuración de la aplicación
#MIC_ID, SAMPLE_RATE = detectarMicrofo(nombreMicrofono)
MODELO = os.path.expanduser("~/.vosk/vosk-model-small-es-0.42")
PALABRA_ACTIVACION = "oye pc"
SESION = detectarSesion()
TIEMPO_ACTIVO = 0
TIMEOUT = 5