from pathlib import Path

ESTADO = Path.home() / ".cache/asistente-voz/estado"

ESTADO_INACTIVO = "inactivo"
ESTADO_ESCUCHANDO = "escuchando"
ESTADO_PROCESANDO = "procesando"
ESTADO_EJECUTANDO = "ejecutando"


def cambiar_estado(estado: str):
    ESTADO.parent.mkdir(parents=True, exist_ok=True)
    ESTADO.write_text(estado)