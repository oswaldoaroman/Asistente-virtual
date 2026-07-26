import re
import subprocess

from skills.base_skill import BaseSkill


class AudioSkill(BaseSkill):
    INTENCIONES = (
        "cambia",
        "usar",
        "usa",
        "pon",
        "cambiar",
    )

    def can_handle(self, texto: str) -> bool:
        texto = texto.lower()
        return any(palabra in texto for palabra in self.INTENCIONES)

    def execute(self, texto: str) -> bool:
        dispositivo = self.buscar_dispositivo(texto)
        if dispositivo is None:
            print("No encontré ningún dispositivo parecido.")
            subprocess.run(
                [
                        "notify-send",
                        "No encontré ningún dispositivo de audio parecido."
                ]
            )
            return False
        print(f"Cambiando salida a: {dispositivo['nombre']}")
        subprocess.run(
            [
                        "notify-send",
                        "Cambiando salida de audio a: " + dispositivo["nombre"]
            ]
        )
        subprocess.run(
            [
                "wpctl",
                "set-default",
                str(dispositivo["id"])
            ]
        )
        return True

    ###########################################################

    def obtener_dispositivos(self):
        salida = subprocess.check_output(
            ["wpctl", "status"],
            text=True
        )
        dispositivos = []
        dentro_sinks = False
        for linea in salida.splitlines():
            if "Sinks:" in linea:
                dentro_sinks = True
                continue
            if dentro_sinks:
                if "Sources:" in linea:
                    break
                match = re.search(
                    r"(\d+)\.\s+(.+?)\s+\[",
                    linea
                )
                if match:

                    dispositivos.append(
                        {
                            "id": int(match.group(1)),
                            "nombre": match.group(2),
                            "aliases": self.generar_aliases(
                                match.group(2)
                            )
                        }
                    )
        return dispositivos

    ###########################################################

    def generar_aliases(self, nombre):
        nombre = nombre.lower()
        aliases = set()
        palabras = re.findall(r"[a-zA-Z0-9]+", nombre)
        aliases.update(palabras)
        if "speaker" in nombre:
            aliases.update(
                [
                    "bocina",
                    "altavoz",
                    "usb",
                    "estereo",
                    "speaker"
                ]
            )
        if "hdmi" in nombre:
            aliases.update(
                [
                    "hdmi",
                    "monitor",
                    "pantalla"
                ]
            )
        if (
            "head" in nombre
            or "headset" in nombre
            or "hyperx" in nombre
        ):
            aliases.update(
                [
                    "audifonos",
                    "cascos",
                    "headset",
                    "diadema"
                ]
            )
        return aliases

    ###########################################################

    def buscar_dispositivo(self, texto):
        texto = texto.lower()
        dispositivos = self.obtener_dispositivos()
        mejor = None
        puntuacion = 0
        for dispositivo in dispositivos:
            score = 0
            for alias in dispositivo["aliases"]:
                if alias in texto:
                    score += 1
            if score > puntuacion:
                puntuacion = score
                mejor = dispositivo
        return mejor

def create():
    return AudioSkill()