from fastapi import FastAPI
import requests
import json
import time
import datetime

app = FastAPI()


@app.post("/newUser")
def newUser(urlDestino:str, EnvioTotalVeces:int, intervaloSegundos: int):

    # webHook sending
    print(f" Iniciando envío de webhooks cada {intervaloSegundos} segundos...")
    print(" Presiona Ctrl+C para detener")
    print("=" * 50)

    contador = 1

    # Send Automatic
    try:
        while (contador <= EnvioTotalVeces):
            # Payload con timestamp
            payload = {
                "name": "Victor",
                "ap_paterno" : "Alva",
                "email" : "victor@gmail.com",
                "timestamp": datetime.datetime.now().isoformat(),
                "numero_envio": contador
            }

            # Enviando la peticion post
            response = requests.post(urlDestino, data=json.dumps(payload), headers={'Content-Type' : 'application/json'})
            # Mostrar información del envío
            tiempo_actual = datetime.datetime.now().strftime('%H:%M:%S')
            print(f" Envío #{contador} - Estado: {response.status_code} - Hora: {tiempo_actual}")

            contador += 1
            # Sleep del dato intervaloSegundos
            time.sleep(intervaloSegundos)
        return f"Datos nuevos {payload}"
    except KeyboardInterrupt:
       return ("Detenido por el usuario", 400)