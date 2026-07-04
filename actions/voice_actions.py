# actions/voice_actions.py
import time
import subprocess
from Comandos.comander_loader import leer_comandos, leer_modos
from config.setting import PALABRA_ACTIVACION,TIMEOUT,SESION

class VoiceActions:
    def __init__(self):
        self.COMANDOS = leer_comandos(SESION)
        self.MODOS =leer_modos()
        self.tiempo_activo=time.time()
        self.tiempo_limite=TIMEOUT
        self.activo = False
        
    def activar_asistente(self, texto, palabra_activacion=PALABRA_ACTIVACION):
        if not self.activo and palabra_activacion in texto:
            self.activo = True
            return True
        
    def desactivar_asistente(self):
        if self.activo and time.time() - self.tiempo_activacion > self.tiempo_limite:
            self.activo = False
            return True
        return False


    def ejecutar_comando(self, texto):
        for clave, cmd in self.COMANDOS.items():
            if clave in texto:
                subprocess.Popen(cmd)
                self.activo = False
                return True
        return False

    def activacion_y_comando(self, texto, palabra_activacion=PALABRA_ACTIVACION):
        if palabra_activacion not in texto:
            return False

        for clave, cmd in self.COMANDOS.items():
            if clave in texto:
                self.activo = True
                self.tiempo_activacion = time.time()
                subprocess.Popen(cmd)
                self.activo = False
                return True
        return False

    def ejecutar_modos(texto, asistente):
        if "modo" in texto:
            for modo, cmd_list in asistente.MODOS.items():
                if modo in texto:
                    for comando in cmd_list:
                        subprocess.Popen(comando)
                    return True
        return False



