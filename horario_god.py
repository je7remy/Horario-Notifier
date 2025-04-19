"""
Define tu Horario GOD como una lista de actividades diarias.
Cada actividad tiene:
 - start: hora de inicio (HH:MM, 24h)
 - end:   hora de fin    (HH:MM, 24h)
 - title: nombre de la actividad
 - mission: indicador SNS/SNP con emoji
"""
HORARIO_GOD = [
    {'start': '06:30', 'end': '07:30', 'title': 'Prepararte y alistarte',
     'mission': '🌿 Ritual Matutino (SNP)'},
    {'start': '07:30', 'end': '07:50', 'title': 'Concentración en el camino',
     'mission': '⚡ Modo Alerta (SNS)'},
    {'start': '07:50', 'end': '08:00', 'title': 'Llegada temprana al trabajo',
     'mission': '📅 Planificación Relámpago (SNS)'},
    {'start': '08:00', 'end': '17:00', 'title': 'Trabajo (tiempos libres para estudio)',
     'mission': '🔥 Modo Productividad (SNS)'},
    {'start': '17:00', 'end': '17:30', 'title': 'Concentración camino de vuelta',
     'mission': '🎯 Reflexión Estratégica (SNP)'},
    {'start': '17:30', 'end': '17:50', 'title': 'Ejercicio',
     'mission': '💪 Sprint de Adrenalina (SNS)'},
    {'start': '17:50', 'end': '18:10', 'title': 'Baño y refrescarse',
     'mission': '🌿 Modo Zen (SNP)'},
    {'start': '18:10', 'end': '19:10', 'title': 'Tareas y estudio',
     'mission': '🔥 Desafío Mental (SNS)'},
    {'start': '19:10', 'end': '20:10', 'title': 'Curso de Ciberseguridad',
     'mission': '🛡️ Subida de Nivel (SNS)'},
    {'start': '20:10', 'end': '20:40', 'title': 'Cena',
     'mission': '🍽 Banquete Reparador (SNP)'},
    {'start': '20:40', 'end': '22:00', 'title': 'Tiempo libre y preparación sueño',
     'mission': '🌿 Exploración Tranquila (SNP)'},
]
