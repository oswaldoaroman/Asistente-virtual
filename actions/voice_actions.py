import subprocess
import time
import logging
from Comandos.comander_loader import leer_comandos, leer_modos
from config.setting import (
    PALABRA_ACTIVACION,
    TIMEOUT,
    SESION,
)
from actions.change_state import (
    cambiar_estado,
    ESTADO_INACTIVO,
    ESTADO_ESCUCHANDO,
    ESTADO_EJECUTANDO,
)

class VoiceActions:
    def __init__(self):
        self.comandos = leer_comandos(SESION)
        self.modos = leer_modos()
        self.activo = False
        self.timeout = TIMEOUT
        self.tiempo_activacion = 0

    ## Activar el asistente si se detecta la palabra de activación
    def activar(self, texto):
        if PALABRA_ACTIVACION in texto:
            self.activo = True
            self.tiempo_activacion = time.time()
            cambiar_estado(ESTADO_ESCUCHANDO)
            return True
        return False

    ## Verificar si el asistente ha estado activo por más tiempo del permitido
    def check_timeout(self):
        if (
            self.activo and
            time.time() - self.tiempo_activacion > self.timeout
        ):
            self.activo = False
            cambiar_estado(ESTADO_INACTIVO)
            return True
        return False

    ## Ejecutar un comando si se encuentra en el texto reconocido
    def ejecutar_comando(self, texto):
        for clave, comando in self.comandos.items():
            if clave in texto:
                cambiar_estado(ESTADO_EJECUTANDO)
                subprocess.Popen(comando)
                self.activo = False
                cambiar_estado(ESTADO_INACTIVO)
                return True
        return False

    def ejecutar_modos(self, texto: str) -> bool:
        if "modo" not in texto:
            return False

        for modo, cmd_list in self.modos.items():
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
      

