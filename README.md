# 📅 Horario Notifier con Google Calendar

Este proyecto en Python te permite automatizar la creación de eventos diarios en tu Google Calendar basados en tu **Horario**, para que recibas notificaciones en tu teléfono y mantengas un día productivo y enfocado.

---

## 📂 Estructura del Proyecto

```
horario_god/
├── calendar_setup.py
├── horario_god.py
├── push_events.py
├── requirements.txt
├── credentials.json  # (Agrega tu archivo aquí)
└── README.md
```

---

## 📥 Requisitos

- Python 3.x
- Cuenta de Google con acceso a Google Calendar
- API de Google Calendar habilitada y `credentials.json` descargado

### 📦 Instalación de Dependencias

```bash
pip install -r requirements.txt
```

---

## 📌 Configuración Inicial

1. **Habilita Google Calendar API**  
   Ve a [Google Cloud Console](https://console.cloud.google.com/apis/library/calendar.googleapis.com) y habilita la API.

2. **Crea Credenciales**
   - Tipo: `OAuth Client ID`
   - Aplicación: `Desktop App`
   - Descarga `credentials.json` y colócalo en la carpeta raíz del proyecto.

3. **Autenticación**
   La primera vez que ejecutes `push_events.py`, se abrirá una ventana de login de Google. Se guardará un token en `token.pickle` para futuras ejecuciones.

---

## ✅ Cómo Usarlo

Ejecuta:

```bash
python push_events.py
```

Esto creará los eventos del día actual en tu Google Calendar según el **Horario GOD** definido en `horario_god.py`, con recordatorios automáticos **10 minutos antes**.

---

## 📝 Personaliza tu Horario

Edita `horario_god.py` para cambiar las horas, nombres de actividades o misiones.

Ejemplo:

```python
HORARIO_GOD = [
    {'start': '06:30', 'end': '07:30', 'title': 'Prepararte y alistarte',
     'mission': '🌿 Ritual Matutino (SNP)'},
    ...
]
```

---

## 📱 Notificaciones en el Teléfono

Solo necesitas tener tu cuenta de Google sincronizada en tu dispositivo Android o iPhone, y Google Calendar enviará notificaciones automáticamente según los recordatorios configurados.

---

## 🚀 Autor

Jeremy José de la Cruz Pérez  
📧 [LinkedIn](https://www.linkedin.com/in/jeremy-jos%C3%A9-de-la-cruz-p%C3%A9rez-0a49b9237/)
🎓 Estudiante de Lic. en Informática

---

## 📜 Licencia

Este proyecto está bajo licencia [MIT](https://github.com/je7remy/linuxknowledge/blob/main/LICENSE).  
