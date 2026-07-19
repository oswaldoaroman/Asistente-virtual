from pathlib import Path

ESTADO = Path.home() / ".cache/asistente-voz/estado"

def cambiar_estado(estado):
    ESTADO.parent.mkdir(exist_ok=True)
    ESTADO.write_text(estado)