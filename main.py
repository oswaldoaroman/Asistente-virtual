from asistente import AsistenteVoz
from config import MIC_ID,SAMPLE_RATE,PALABRA_ACTIVACION
import sounddevice as sd
import time 
import subprocess
import json

asistente = AsistenteVoz()

def activar_asistente(texto, asistente):
    if not asistente.activo and PALABRA_ACTIVACION in texto:
        asistente.activo = True
        asistente.tiempo_activacion = time.time()
        
        return True
    return False


def ejecutar_comando(texto, asistente):
    for clave, cmd in asistente.COMANDOS.items():
        if clave in texto:
            print(f"▶ Ejecutando: {clave}")
            subprocess.Popen(cmd)
            asistente.activo = False
            return True
    return False


def activacion_y_comando(texto, asistente):
    if PALABRA_ACTIVACION not in texto:
        return False

    for clave, cmd in asistente.COMANDOS.items():
        if clave in texto:
            asistente.activo = True
            asistente.tiempo_activacion = time.time()
            print(f"▶ Ejecutando: {clave} {cmd}")
            subprocess.Popen(cmd)
            asistente.activo = False
            #print ("[DEBUG] Entro en funcion activacion y comando")
            return True
    
    return False

def comando_buscar(texto):
    if texto.startswith("busca "):
        termino = texto.replace("busca ", "").strip()
        if termino:
            subprocess.Popen(["firefox", termino])
            return True
    return False

def ejecutarModos(texto,asistente):
    if "modo" in texto:
        print(type(asistente.MODOS))
        for modo,cmd in asistente.MODOS.items():
            if modo in texto:
                print(f"Ejecutando modo:",{modo})
                for comando in cmd:
                    subprocess.Popen(comando)

def comando_buscar(texto):
    if texto.startswith("busca "):
        termino = texto.replace("busca ", "").strip()
        if termino:
            subprocess.Popen(["firefox", termino])
            return True
    return False


# def recargarComandos(texto,asistente):
#     if ("regarcar comandos"):
#         asistente.leercomandos()

with sd.RawInputStream(
    device=MIC_ID,
    samplerate=SAMPLE_RATE,
    blocksize=8000,
    dtype="int16",
    channels=1,
    callback=asistente.callback
):
    print("[Debug] El asistente esta en funcionamiento")

    while True:
        data = asistente.q.get()

        if asistente.rec.AcceptWaveform(data):
            texto = json.loads(asistente.rec.Result()).get("text", "").strip()
            texto = asistente.normalizar(texto)

            if not texto:
                continue
    
            print(f"[DEBUG] Se escucho: ",texto)
            
            if asistente.activo:
                if comando_buscar(texto):
                    asistente.activo = False
                continue

            if activacion_y_comando(texto, asistente):
                continue
            
            if activar_asistente(texto, asistente):
                continue

            if asistente.activo:
                ejecutar_comando(texto, asistente)

            if asistente.activo:
                ejecutarModos(texto, asistente)

            # if asistente.activo and "recarga comandos" in texto:
            #     asistente.leercomandos()
            #     print("Se han recargado los archivos")

            if asistente.activo and "salir" in texto:
                break

        if asistente.activo and time.time() - asistente.tiempo_activacion > asistente.TIMEOUT:
            asistente.activo = False

