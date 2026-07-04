import logging
logger  = logging.getLogger(__name__)

import os
import sounddevice as sd


nombreMicrofono="GENERAL WEBCAM: USB Audio"
nombreBocina="SSS USB Speaker: Audio"
# ===== CONFIGURACIÓN =====
def detectarSesion():
    if os.environ.get("HYPRLAND_INSTANCE_SIGNATURE"):
        return "hyprland"
    if os.environ.get("WAYLAND_DISPLAY"):
        return "wayland"
    if os.environ.get("DISPLAY"):
        return "x11"
        
    return "desconocido"

def detectarMicrofo(nombreMicrofono):
    for dispositivo in sd.query_devices():
        if (
            nombreMicrofono.lower() in dispositivo["name"].lower() 
            and dispositivo["max_input_channels"]>0
            ):
            logging.info("Se encontro la webcam")
            return dispositivo["index"],int (dispositivo["default_samplerate"])
    
    raise logging.error("No se ha encontrado un microfono valido")

# for dispositivo in sd.query_devices():
#     #print(f"Diccionario exterior",a)
#     if nombreMicrofono.lower() in dispositivo["name"].lower() and dispositivo["max_input_channels"]>0:
#         print("Se encontro la webcam")
#         webcam=dispositivo
#     elif nombreBocina in dispositivo["name"]:
#         print("Se encontro la bocina")
#         bocina=dispositivo

MIC_ID, SAMPLE_RATE = detectarMicrofo(nombreMicrofono)
MODELO = os.path.expanduser("~/.vosk/vosk-model-small-es-0.42")
PALABRA_ACTIVACION = "oye pc"
SESION = detectarSesion()

