from skills.base_skill import BaseSkill
import subprocess


class QtileSkill(BaseSkill):
    def can_handle(self, texto: str) -> bool:
        claves = (
            # NAVEGACION
            "escritorio uno", "escritorio dos", "escritorio tres", "escritorio cuatro", "escritorio cinco",
            "siguiente escritorio", "escritorio anterior",
            # VENTANAS
            "cierra ventana", "maximiza ventana",
            "mueve ventana a uno", "mueve ventana a dos", "mueve ventana a tres",
            "mueve ventana a cuatro", "mueve ventana a cinco",
        )
        return any(k in texto for k in claves)

    def execute(self, texto: str) -> bool:
        # -------- NAVEGACION --------
        if "escritorio uno" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "group", "1", "-f", "toscreen"])
            return True
        if "escritorio dos" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "group", "2", "-f", "toscreen"])
            return True
        if "escritorio tres" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "group", "3", "-f", "toscreen"])
            return True
        if "escritorio cuatro" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "group", "4", "-f", "toscreen"])
            return True
        if "escritorio cinco" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "group", "5", "-f", "toscreen"])
            return True

        if "siguiente escritorio" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "screen", "-f", "next_group"])
            return True
        if "escritorio anterior" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "screen", "-f", "prev_group"])
            return True

        # -------- VENTANAS --------
        if "cierra ventana" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "window", "-f", "kill"])
            return True

        if "maximiza ventana" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "window", "-f", "toggle_fullscreen"])
            return True

        if "mueve ventana a uno" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "window", "-f", "togroup", "-a", "1"])
            return True
        if "mueve ventana a dos" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "window", "-f", "togroup", "-a", "2"])
            return True
        if "mueve ventana a tres" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "window", "-f", "togroup", "-a", "3"])
            return True
        if "mueve ventana a cuatro" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "window", "-f", "togroup", "-a", "4"])
            return True
        if "mueve ventana a cinco" in texto:
            subprocess.Popen(["qtile", "cmd-obj", "-o", "window", "-f", "togroup", "-a", "5"])
            return True

        return False


def create():
    return QtileSkill()
