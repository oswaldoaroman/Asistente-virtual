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

        voiceActions.procesar(texto)