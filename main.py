import subprocess,time,json,logging
from config.logging_config import logging
from speech.vosk_enginer import VoskEngine
from Comandos.comander_loader import leer_corpus
from config.setting import MODELO
from actions.voice_actions import VoiceActions

# import openwakeword
# from openwakeword.model import Model

# # One-time download of all pre-trained models (or only select models)
# openwakeword.utils.download_models()

# # Instantiate the model(s)
# model = Model(
# #         wakeword_models=["path/to/model.tflite"],  # can also leave this argument empty to load all of the included pre-trained models
# )

# # Get audio data containing 16-bit 16khz PCM audio data from a file, microphone, network stream, etc.
# # For the best efficiency and latency, audio frames should be multiples of 80 ms, with longer frames
# # increasing overall efficiency at the cost of detection latency


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

# #=============OPenWakeWord================#
# frame = proceso
# # Get predictions for the frame
# prediction = model.predict(proceso)
# #=========================================#


while True:
    #data = VoskEngine.q.get()
    data = proceso.stdout.read(4000)

    if vosk.push_audio(data):
        texto = json.loads(vosk.get_result()).get("text", "").strip()
        if not texto:
            continue

        logging.info(f"Texto reconocido: {texto}")
        voiceActions.procesar(texto)