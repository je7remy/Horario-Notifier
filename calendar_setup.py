import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Alcance que necesitamos: crear/editar eventos en Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_calendar_service(token_path: str = 'token.pickle',
                         creds_path: str = 'credentials.json'):
    """
    - Carga credenciales guardadas en token.pickle (si existen y son válidas).
    - Si no hay token o está expirado, inicia flujo OAuth en local server.
    - Devuelve un objeto 'service' para llamar a Google Calendar API.
    """
    creds = None
    # 1) Intentar leer token previamente guardado
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token_file:
            creds = pickle.load(token_file)

    # 2) Si no hay credenciales válidas, pedir login
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
        creds = flow.run_local_server(port=49918)
        # Guardar para la próxima vez
        with open(token_path, 'wb') as token_file:
            pickle.dump(creds, token_file)

    # 3) Construir el servicio
    service = build('calendar', 'v3', credentials=creds)
    return service

if __name__ == '__main__':
    # Prueba rápida
    service = get_calendar_service()
    print("✅ Servicio de Google Calendar listo:", service)
