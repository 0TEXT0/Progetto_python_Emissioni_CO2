import json
import pandas as pd

# risposta al riscontro singolo
def cercaDati( df, inputNazione, inputAnno):
    dato_emissioni=None
    # trova il dato per la determinata nazione per il determinato anno
    nazione = inputNazione.strip()
    anno_str = inputAnno.strip()

    try:
        # Tenta di convertire l'anno in un intero.
        anno = int(anno_str)
    except ValueError:
        # Gestisce il caso in cui l'utente digita testo o un float nell'anno
        return "Errore: L'anno deve essere un numero intero valido, compreso tra il 2001 e il 2012 (es. 2005)."

    if anno<2001 or anno>2012:
        return "Errore: l'anno deve essere compreso tra il 2001 e il 2012"
    dato_trovato = df[(df['Nazione'].str.strip().str.lower() == nazione.lower()) & (df['Anno'] == anno_str)]
    #crea il df con i dati selezionati
    if not dato_trovato.empty:
        # Estrae il valore dalla colonna 'Emissioni_CO2'
        dato_emissioni = dato_trovato['Emissioni_CO2'].iloc[0]
        numero = float(dato_emissioni)

        dato_formattato = f"{numero:,.2f}" # virgola per separare le migliaia,
        # 2f per mantenere 2 decimali

        return dato_formattato
    else: 
        return None
    



