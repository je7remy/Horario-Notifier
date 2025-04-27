import time  # 👈 Importar esto arriba
from datetime import datetime, timedelta
from horario_god import HORARIO_GOD
from calendar_setup import get_calendar_service

DIAS_A_CREAR = 30

def crear_evento(service, fecha, actividad):
    start_time = f"{fecha}T{actividad['start']}:00"
    end_time = f"{fecha}T{actividad['end']}:00"
    event_body = {
        'summary': actividad['title'],
        'description': actividad['mission'],
        'start': {'dateTime': start_time, 'timeZone': 'America/Santo_Domingo'},
        'end': {'dateTime': end_time, 'timeZone': 'America/Santo_Domingo'},
        'reminders': {'useDefault': False, 'overrides': [{'method': 'popup', 'minutes': 10}]}
    }
    created = service.events().insert(calendarId='primary', body=event_body).execute()
    print(f"✅ Creado ({fecha}): {actividad['title']} | {actividad['mission']} ({actividad['start']}-{actividad['end']})")
    time.sleep(1)  # 👈 Espera 1 segundo antes de crear el siguiente evento

def main():
    service = get_calendar_service()
    hoy = datetime.now()
    for i in range(DIAS_A_CREAR):
        fecha = (hoy + timedelta(days=i)).strftime('%Y-%m-%d')
        for actividad in HORARIO_GOD:
            crear_evento(service, fecha, actividad)

if __name__ == '__main__':
    main()
