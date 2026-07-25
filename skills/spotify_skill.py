from skills.base_skill import BaseSkill
import subprocess


class AudioSkill(BaseSkill):
    def can_handle(self, texto):
        claves = (
            "sube volumen",
            "baja volumen",
            "silencio",
            "siguiente cancion",
            "cancion anterior",
            "pausa",
            "reanuda",
            "spotify"
        )
        return any(k in texto for k in claves)

    def execute(self, texto):
        # SONIDO
        if "sube volumen" in texto:
            subprocess.Popen(
                ["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", "5%+"]
            )
            return True

        if "baja volumen" in texto:
            subprocess.Popen(
                ["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", "5%-"]
            )
            return True

        if "silencio" in texto:
            subprocess.Popen(
                ["wpctl", "set-mute", "@DEFAULT_AUDIO_SINK@", "toggle"]
            )
            return True

        # MULTIMEDIA
        if "siguiente cancion" in texto:
            subprocess.Popen(["playerctl", "next"])
            return True

        if "cancion anterior" in texto:
            subprocess.Popen(["playerctl", "previous"])
            return True

        if "pausa" in texto:
            subprocess.Popen(["playerctl", "pause"])
            return True

        if "reanuda" in texto:
            subprocess.Popen(["playerctl", "play"])
            return True

        if "spotify" in texto:
            subprocess.Popen("systemd-run", "--user", "spotify")

        return False


def create():
    return AudioSkill()
