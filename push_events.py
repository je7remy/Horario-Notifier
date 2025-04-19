from datetime import datetime
from calendar_setup import get_calendar_service
from horario_god import HORARIO_GOD

def crear_evento(service, fecha: str, actividad: dict):
    """
    Inserta un evento en Google Calendar:
    - fecha: YYYY-MM-DD
    - actividad: diccionario con start, end, title, mission
    """
    start_dt = datetime.fromisoformat(f"{fecha}T{actividad['start']}:00")
    end_dt   = datetime.fromisoformat(f"{fecha}T{actividad['end']}:00")

    event_body = {
        'summary': f"{actividad['title']} | {actividad['mission']}",
        'start': {'dateTime': start_dt.isoformat(), 'timeZone': 'America/Santo_Domingo'},
        'end':   {'dateTime': end_dt.isoformat(),   'timeZone': 'America/Santo_Domingo'},
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    created = service.events().insert(calendarId='primary', body=event_body).execute()
    print(f"✅ Creado: {created['summary']} ({actividad['start']}-{actividad['end']})")

def main():
    fecha = datetime.now().date().isoformat()
    service = get_calendar_service()
    for act in HORARIO_GOD:
        crear_evento(service, fecha, act)

if __name__ == '__main__':
    main()
