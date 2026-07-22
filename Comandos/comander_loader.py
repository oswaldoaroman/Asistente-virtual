import json
import logging
from pathlib import Path

comandos = Path.home() / "asistente-voz/Comandos/comandos.json"
qtile = Path.home() / "asistente-voz/Comandos/qtile.json"
hypr = Path.home() / "asistente-voz/Comandos/hyprland.json"
modos= Path.home() / "asistente-voz/Comandos/MODOS.json"
corpus= Path.home() / "asistente-voz/corpus.txt"

def leer_comandos(sesion):
    with open(comandos, "r", encoding="utf-8") as f:
        data = json.load(f)
        logging.info("Comandos cargados")

    if (sesion not in ("hyprland", "wayland")) and sesion == "x11":
        with open(qtile, "r", encoding="utf-8") as comands:
            comands_sesion = json.load(comands)
        logging.info("Backend de comandos cargado: Qtile")
    else:
        with open(hypr, "r", encoding="utf-8") as comands:
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
    with open(modos, "r", encoding="utf-8") as f:
        return json.load(f)

def leer_corpus():
    with open(corpus, "r", encoding="utf-8") as f:
        logging.info("Corpus cargado")
        return [l.strip() for l in f if l.strip()]

leer_comandos("hyprland")