from pathlib import Path
import importlib
import logging

logger = logging.getLogger(__name__)


class SkillManager:
    """
    Carga automáticamente todas las Skills ubicadas en la carpeta skills/.
    Cada módulo debe implementar:
        def create():
            return MiSkill()
    """
    def __init__(self):
        self.skills = []
        self.load_skills()

    def load_skills(self):
        """Busca e instancia todas las Skills."""
        skills_path = Path(__file__).parent.parent / "skills"
        logger.info("Cargando Skills...")

        for archivo in skills_path.glob("*.py"):
            # Ignorar archivos especiales
            if archivo.stem.startswith("__"):
                continue
            # Ignorar la clase base
            if archivo.stem == "base_skill":
                continue

            try:
                modulo = importlib.import_module(
                    f"skills.{archivo.stem}"
                )
                if not hasattr(modulo, "create"):
                    logger.warning(
                        f"{archivo.stem} no tiene función create()"
                    )
                    continue
                skill = modulo.create()
                self.skills.append(skill)
                logger.info(
                    f"Skill cargada: {skill.__class__.__name__}"
                )
            except Exception:
                logger.exception(
                    f"No se pudo cargar la Skill {archivo.stem}"
                )
        logger.info(
            f"{len(self.skills)} Skills cargadas correctamente."
        )

    def execute(self, texto: str) -> bool:
        """
        Busca una Skill capaz de manejar el texto.
        """
        for skill in self.skills:
            try:
                if skill.can_handle(texto):
                    logger.info(
                        f"{skill.__class__.__name__} manejará: '{texto}'"
                    )
                    return skill.execute(texto)

            except Exception:
                logger.exception(
                    f"Error ejecutando {skill.__class__.__name__}"
                )

        return False