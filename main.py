import subprocess,time,json,logging
from config.logging_config import logging
from speech.vosk_enginer import VoskEngine
from Comandos.comander_loader import leer_corpus
from config.setting import MODELO
from actions.voice_actions import VoiceActions

voiceActions=VoiceActions()

logging.info("Asistente de voz iniciado")


vosk = VoskEngine(MODELO, 16000, leer_corpus())
proceso = subprocess.Popen(
    [
        "parecord",
        "--raw",
        "--rate=16000",
        "--channels=1",
        "--format=s16le"
    ],
    stdout=subprocess.PIPE
)
logging.info(" El asistente esta en funcionamiento")


while True:
    #data = VoskEngine.q.get()
    data = proceso.stdout.read(4000)

    if vosk.push_audio(data):
        texto = json.loads(vosk.get_result()).get("text", "").strip()
        if not texto:
            continue

        logging.info(f"Texto reconocido: {texto}")

        if voiceActions.activo==False:
            if voiceActions.activacion_y_comando(texto):
                logging.info("Asistente activado y comando ejecutado")
                voiceActions.tiempo_activacion = time.time()

        if voiceActions.activo==False:
            if voiceActions.activar_asistente(texto):
                logging.info("Asistente activado")
                voiceActions.tiempo_activacion = time.time()
        else:
            if voiceActions.desactivar_asistente():
                logging.info("Asistente desactivado por inactividad")
                continue

            if voiceActions.ejecutar_comando(texto):
                logging.info(f"Comando ejecutado: {texto}")
                continue

            if voiceActions.ejecutar_modos(texto, voiceActions):
                logging.info(f"Modo ejecutado: {texto}")
                continue

        

