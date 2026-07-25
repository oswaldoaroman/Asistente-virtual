from skills.base_skill import BaseSkill
import subprocess


class HyprSkill(BaseSkill):
    def can_handle(self, texto: str) -> bool:
        claves = (
            # NAVEGACION
            "ir a uno", "ir a dos", "ir a tres", "ir a cuatro", "ir a cinco",
            "ir a seis", "ir a siete", "ir a ocho", "ir a nueve", "ir a diez",
            "siguiente escritorio", "escritorio anterior",
            # VENTANAS
            "cierra ventana", "cierra todo", "maximiza ventana",
            "mover a uno", "mover a dos", "mover a tres", "mover a cuatro", "mover a cinco",
            "mover a seis", "mover a siete", "mover a ocho", "mover a nueve", "mover a diez",
        )
        return any(k in texto for k in claves)

    def execute(self, texto: str) -> bool:
        # -------- NAVEGACION --------
        if "ir a uno" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "1"]); return True
        if "ir a dos" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "2"]); return True
        if "ir a tres" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "3"]); return True
        if "ir a cuatro" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "4"]); return True
        if "ir a cinco" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "5"]); return True
        if "ir a seis" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "6"]); return True
        if "ir a siete" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "7"]); return True
        if "ir a ocho" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "8"]); return True
        if "ir a nueve" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "9"]); return True
        if "ir a diez" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "0"]); return True

        if "siguiente escritorio" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "m+1"]); return True
        if "escritorio anterior" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "workspace", "m-1"]); return True

        # -------- VENTANAS --------
        if "cierra ventana" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "killactive"]); return True

        if "cierra todo" in texto:
            subprocess.Popen([
                "sh", "-c",
                "hyprctl clients -j | jq -r '.[] | .address' | "
                "xargs -I{} hyprctl dispatch closewindow address:{}"
            ])
            return True

        if "maximiza ventana" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "fullscreen"]); return True

        if "mover a uno" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "1"]); return True
        if "mover a dos" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "2"]); return True
        if "mover a tres" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "3"]); return True
        if "mover a cuatro" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "4"]); return True
        if "mover a cinco" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "5"]); return True
        if "mover a seis" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "6"]); return True
        if "mover a siete" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "7"]); return True
        if "mover a ocho" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "8"]); return True
        if "mover a nueve" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "9"]); return True
        if "mover a diez" in texto:
            subprocess.Popen(["hyprctl", "dispatch", "movetoworkspace", "0"]); return True

        return False


def create():
    return HyprSkill()
