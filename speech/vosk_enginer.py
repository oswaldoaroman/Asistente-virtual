import json
from vosk import Model, KaldiRecognizer
from Comandos.comander_loader import leer_corpus


class VoskEngine:
    def __init__(self, modelo_path, sample_rate, corpus_lines):
        self.model = Model(modelo_path)
        self.rec = KaldiRecognizer(
            self.model,
            sample_rate,
            json.dumps(corpus_lines)
        )

    def push_audio(self, pcm_bytes):
        return self.rec.AcceptWaveform(pcm_bytes)

    def result(self):
        return json.loads(self.rec.Result())

    def final_result(self):
        return json.loads(self.rec.FinalResult())
    
    def get_result(self):
        return self.rec.Result()
    
    