import time
import subprocess
from Comandos.comander_loader import leer_comandos, leer_modos
from config.setting import PALABRA_ACTIVACION, TIMEOUT, SESION
import logging


class VoiceActions:
    def __init__(self):
        self.COMANDOS = leer_comandos(SESION)
        self.MODOS = leer_modos()

        self.activo = False
        self.tiempo_activacion = 0
        self.timeout = TIMEOUT

    # Activación por palabra clave
    def activar(self, texto: str) -> bool:
        if PALABRA_ACTIVACION in texto:
            self.activo = True
            self.tiempo_activacion = time.time()
            return True
        return False

    # TIMEOUT
    def check_timeout(self):
        if self.activo and (time.time() - self.tiempo_activacion > self.timeout):
            self.activo = False
            return True
        return False

    # Ejecutar comandos
    def ejecutar_comando(self, texto: str) -> bool:
        for clave, cmd in self.COMANDOS.items():
            if clave in texto:
                subprocess.Popen(cmd)
                self.activo = False
                return True
        return False

    # ejecutar modos (estudio/debug/etc) *Falta implementar los modos*
    def ejecutar_modos(self, texto: str) -> bool:
        if "modo" not in texto:
            return False

        for modo, cmd_list in self.MODOS.items():
            if modo in texto:
                for cmd in cmd_list:
                    subprocess.Popen(cmd)
                return True

        return False

    
    # Procesar el texto reconocido
    def procesar(self, texto: str):
        # 1. Timeout siempre se revisa
        self.check_timeout()

        # 2. Si es modo, ejecuta directo
        if self.ejecutar_modos(texto):
            return

        # 3. Si no está activo, intenta activar
        if not self.activo:
            if self.activar(texto):
                return self.procesar(texto)  # Reprocesar el texto después de activar
            return
            
        # # 4. Si está activo, ejecuta comandos
        if self.ejecutar_comando(texto):
            logging.info("Comando ejecutado correctamente")
            return 
      

