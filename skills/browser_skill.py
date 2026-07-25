from skills.base_skill import BaseSkill
import subprocess


class BrowserSkill(BaseSkill):

    def can_handle(self, texto):

        return any(
            comando in texto
            for comando in (
                "navegador",
                "youtube",
                "github",
                "whatsapp",
                "ia"
            )
        )

    def execute(self, texto):

        if "navegador" in texto:
            subprocess.Popen(["systemd-run", "--user", "librewolf"])
            return True

        if "youtube" in texto:
            subprocess.Popen(
                ["systemd-run", "--user", "chromium", "--app=https://www.youtube.com/"]
            )
            return True

        if "git" in texto:
            subprocess.Popen(
                ["systemd-run", "--user", "chromium", "--app=https://github.com/"]
            )
            return True

        if "whatsapp" in texto:
            subprocess.Popen(
                ["systemd-run", "--user", "chromium", "--app=https://web.whatsapp.com/"]
            )
            return True

        if "ia" in texto:
            subprocess.Popen(
                ["systemd-run", "--user", "chromium", "--app=https://chat.openai.com/"]
            )
            return True

        return False


def create():
    return BrowserSkill()