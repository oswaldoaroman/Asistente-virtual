# Asistente de Voz Offline

Un asistente de voz completamente **offline** desarrollado en Python para Linux, diseñado para controlar el sistema mediante comandos de voz sin depender de servicios en la nube.

Actualmente utiliza **Vosk** como motor de reconocimiento de voz y está orientado principalmente a entornos **Wayland (Hyprland)**, aunque su arquitectura permite añadir soporte para otros escritorios.

> **Estado del proyecto:** En desarrollo activo.

---

## Características actuales

- Reconocimiento de voz completamente offline mediante Vosk.
- Palabra de activación configurable.
- Ejecución de comandos del sistema.
- Modos personalizados mediante archivos JSON.
- Carga dinámica de comandos.
- Soporte para múltiples sesiones (Hyprland / Qtile).
- Configuración centralizada.
- Registro de eventos mediante `logging`.
- Arquitectura modular y fácilmente extensible.

---

## Arquitectura

El proyecto está dividido en módulos con responsabilidades independientes.

```
Audio
   │
   ▼
VoskEngine
   │
   ▼
Texto reconocido
   │
   ▼
VoiceActions
   │
   ├── Comandos
   ├── Modos
   └── Sistema operativo
```

### Componentes principales

| Módulo | Responsabilidad |
|---------|-----------------|
| `main.py` | Orquesta el funcionamiento del asistente |
| `VoskEngine` | Encapsula el reconocimiento de voz mediante Vosk |
| `VoiceActions` | Procesa el texto reconocido y ejecuta acciones |
| `commander_loader` | Carga comandos, corpus y modos desde JSON |
| `setting.py` | Configuración global del proyecto |
| `entorno.py` | Detecta la sesión gráfica actual |
| `logging_config.py` | Configuración del sistema de logs |

---

## Estructura del proyecto

```
asistente-voz/
│
├── actions/
│   └── voice_actions.py
│
├── speech/
│   └── vosk_engine.py
│
├── config/
│   ├── setting.py
│   ├── entorno.py
│   └── logging_config.py
│
├── Comandos/
│   ├── commander_loader.py
│   ├── comandos.json
│   ├── modos.json
│   └── corpus.json
│
├── main.py
│
└── README.md
```

---

## Funcionamiento

1. El asistente captura audio desde el micrófono.
2. Vosk convierte el audio en texto.
3. Se verifica la palabra de activación.
4. Se procesa el comando reconocido.
5. Se ejecuta la acción correspondiente.

---

## Configuración

Las principales opciones se encuentran en `config/setting.py`.

```python
MODELO
PALABRA_ACTIVACION
SESION
TIMEOUT
```

---

## Comandos

Los comandos se almacenan en archivos JSON, lo que permite añadir nuevas funcionalidades sin modificar el código fuente.

Ejemplo:

```json
{
    "abre firefox": [
        "firefox"
    ],
    "abre terminal": [
        "alacritty"
    ]
}
```

---

## Modos

También es posible definir modos personalizados.

Ejemplo:

```json
{
    "modo estudio": [
        ["spotify"],
        ["firefox"],
        ["code"]
    ]
}
```

Cada modo puede ejecutar múltiples comandos de forma secuencial.

---

## Tecnologías utilizadas

- Python 3
- Vosk
- PipeWire
- parecord
- subprocess
- JSON
- logging
- systemd (User Services)

---

## Objetivos del proyecto

- Mantener el funcionamiento completamente offline.
- Reducir al mínimo el consumo de recursos.
- Facilitar la creación de nuevos comandos.
- Diseñar una arquitectura modular.
- Permitir futuras integraciones con modelos de IA locales.

---

## Próximas características

- [ ] Integración con OpenWakeWord.
- [ ] Sistema de Skills.
- [ ] Indicador de estado en Waybar.
- [ ] Soporte para comandos con argumentos.
- [ ] Integración opcional con Ollama.
- [ ] Historial de comandos.
- [ ] Configuración mediante interfaz gráfica.
- [ ] Mejor manejo del contexto de conversación.

---

## Licencia

Este proyecto es desarrollado con fines educativos y de aprendizaje.

No está afiliado con Vosk, Hyprland ni OpenAI.

---

## Autor

Desarrollado por **Oswaldo Abimael Flores Roman**.
