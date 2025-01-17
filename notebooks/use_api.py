import requests
import json
import app
import threading
import pandas as pd
import time
#start api
def start_api():
    app.app.run(debug=True, use_reloader=False)

api_thread = threading.Thread(target=start_api, daemon=True)
api_thread.start()

api_url = "http://127.0.0.1:5000" #Standaard api url



def predict(time=7):
    endpoint = f"{api_url}/predict"
    params = {"time": time}
    try:
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            print("\nVoorspellingen ontvangen:")
            print(response.json())

            data = response.json()
            df = pd.DataFrame(data["predictions"], columns=["Predicted Values"])
            print('\n')
            print(df)
        else:
            print(f"Fout bij /predict: {response.status_code}")
            print(response.json())
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

def update_model(params):
    endpoint = f"{api_url}/update-model"
    payload = {"params": params}
    try:
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            print("Modelparameters bijgewerkt:")
            print(response.json())
        else:
            print(f"Fout bij /update-model: {response.status_code}")
            print(response.json())
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

def menu():
    while True:
        print("\n \n \nKies een actie:")
        print("1. Voorspellingen ophalen (/predict)")
        print("2. Model trainen met nieuwe data (/train)")
        print("3. Modelparameters updaten (/update-model)")
        print("4: Exit")
    
        keuze = input("Voer je keuze in (1/2/3/4): ")
    
        if keuze == "1":
            try:
                time = int(input("Aantal dagen voor voorspellingen (standaard 7): ") or 7)
                predict(time)
            except ValueError:
                print("Voer een geldig getal in.")
    
        # elif keuze == "2":
        #     data_path = input("Geef het pad naar de nieuwe data (CSV-bestand): ")
        #     if data_path:
        #         train(data_path)
        #     else:
        #         print("Geen data pad opgegeven.")
    
        elif keuze == "3":
            params = input("Voer de parameters in JSON-formaat in (bv. {\"param1\": \"value1\"}): ")
            try:
                params_dict = json.loads(params)
                update_model(params_dict)
            except json.JSONDecodeError:
                print("Ongeldige JSON-invoer. Zorg ervoor dat je een geldig JSON-formaat gebruikt.")

        elif keuze == "4":
            break

        else:
            print("Ongeldige keuze. Probeer opnieuw.")

        input("\nPress enter to continue\n")

if __name__ == "__main__":
    time.sleep(2)
    menu()