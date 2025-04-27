
---

# 📅 Horario Notifier con Google Calendar

Este proyecto en Python te permite automatizar la creación de eventos diarios en tu Google Calendar basados en tu **Horario GOD**, para que recibas notificaciones en tu teléfono y mantengas un día productivo y enfocado.

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

### 1. Habilita la API de Google Calendar

Ve a [Google Cloud Console](https://console.cloud.google.com/apis/library/calendar.googleapis.com) y habilita la API de Calendar para tu proyecto.

---

### 2. Crea las Credenciales

- Tipo: `OAuth Client ID`
    
- Aplicación: `Desktop App`
    
- Descarga el archivo `credentials.json` y colócalo en la carpeta raíz del proyecto.
    

---

### 3. Configura el Redirect URI Correcto

Es posible que te encuentres con este error:

```
Error 400: redirect_uri_mismatch
```

Esto significa que la URI de redirección de tu script (`http://localhost:49918/`) no está registrada en Google Cloud Console.

#### Solución:

- Ve a [Google Cloud Console](https://console.cloud.google.com/).
    
- Entra en tu proyecto.
    
- Dirígete a **API y servicios > Credenciales**.
    
- Edita tu cliente OAuth 2.0.
    
- En **URIs de redireccionamiento autorizados**, agrega exactamente:
    

```
http://localhost:49918/
```

- Guarda los cambios.
    

_Nota:_ Si el puerto cambia (por ejemplo a `localhost:50722`), también debes actualizarlo en la consola.

---

### 4. Agrega tu Usuario como Tester (si la app es externa)

- En Google Cloud Console, ve a **OAuth Consent Screen**.
    
- Si el tipo de usuario es **Externo**, baja hasta **Usuarios de prueba (Test Users)**.
    
- Agrega el correo de la cuenta de Google con la que iniciarás sesión.
    
- Guarda los cambios.
    

---

## ✅ Cómo Usarlo

### 1. Configurar conexión

Ejecuta primero:

```bash
python calendar_setup.py
```

Esto abrirá una ventana para que inicies sesión en Google y creará un archivo `token.json` que permitirá el acceso a tu cuenta de forma segura.

**¿Qué significa si ves algo como esto?**

```
✅ Servicio de Google Calendar listo: <googleapiclient.discovery.Resource object at 0x...>
```

¡Perfecto! Eso indica que la conexión quedó configurada exitosamente.

---

### 2. Crear los eventos

Ahora ejecuta:

```bash
python push_events.py
```

o si estás en PowerShell:

```powershell
& .\.venv\Scripts\python.exe .\push_events.py
```

Este script tomará tu **Horario GOD** definido en `horario_god.py` y lo subirá a tu Google Calendar para el día de hoy (y/o días futuros si configuras el script así).

Cada evento te enviará una notificación **10 minutos antes** automáticamente.

---

## 🛠️ Solución a errores comunes

### ❌ Error: `Google Calendar API has not been used in project ... or it is disabled`

Esto ocurre si la API aún no está activada en tu proyecto.

**Solución:**

1. Entra a este enlace:  
    👉 [Activar Google Calendar API](https://console.developers.google.com/apis/api/calendar-json.googleapis.com/overview)
    
2. Selecciona tu proyecto.
    
3. Haz clic en **Habilitar**.
    
4. Luego, vuelve a correr:
    

```bash
python push_events.py
```

---

## 📜 Ejemplo de Ejecución Correcta

Cuando todo esté bien configurado, deberías ver en tu consola algo como:

```
✅ Creado: Prepararte y alistarte | 🌿 Ritual Matutino (SNP) (06:30-07:30)
✅ Creado: Concentración en el camino | ⚡ Modo Alerta (SNS) (07:30-07:50)
✅ Creado: Llegada temprana al trabajo | 📅 Planificación Relámpago (SNS) (07:50-08:00)
✅ Creado: Trabajo (tiempos libres para estudio) | 🔥 Modo Productividad (SNS) (08:00-17:00)
✅ Creado: Concentración camino de vuelta | 🎯 Reflexión Estratégica (SNP) (17:00-17:30)
✅ Creado: Ejercicio | 💪 Sprint de Adrenalina (SNS) (17:30-17:50)
✅ Creado: Baño y refrescarse | 🌿 Modo Zen (SNP) (17:50-18:10)
✅ Creado: Tareas y estudio | 🔥 Desafío Mental (SNS) (18:10-19:10)
✅ Creado: Curso de Ciberseguridad | 🛡️ Subida de Nivel (SNS) (19:10-20:10)
✅ Creado: Cena | 🍽 Banquete Reparador (SNP) (20:10-20:40)
✅ Creado: Tiempo libre y preparación sueño | 🌿 Exploración Tranquila (SNP) (20:40-22:00)
```

**Y los eventos aparecerán automáticamente en tu Google Calendar.** 📅✅

---

## 📝 Personaliza tu Horario

Puedes modificar fácilmente el contenido de tu horario editando el archivo `horario_god.py`.

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