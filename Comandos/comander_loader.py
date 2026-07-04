import json
import logging

def leer_comandos(sesion):
    with open("/home/Apatosaurio19/asistente-voz/Comandos/comandos.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if (sesion not in ("hyprland", "wayland")) and sesion == "x11":
        with open("/home/Apatosaurio19/asistente-voz/Comandos/qtile.json", "r", encoding="utf-8") as comands:
            comands_sesion = json.load(comands)
        logging.info("Backend de comandos cargado: Qtile")
    else:
        with open("/home/Apatosaurio19/asistente-voz/Comandos/hyprland.json", "r", encoding="utf-8") as comands:
            comands_sesion = json.load(comands)
        logging.info("Backend de comandos cargado: Hyprland")

    return {
        **data["SONIDO"],
        **data["LANZARAPP"],
        **data["MULTIMEDIA"],
        **comands_sesion["NAVEGACION"],
        **comands_sesion["VENTANAS"],
    }

def leer_modos():
    with open("/home/Apatosaurio19/asistente-voz/Comandos/MODOS.json", "r", encoding="utf-8") as f:
        return json.load(f)

def leer_corpus(path="/home/Apatosaurio19/asistente-voz/corpus.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]
