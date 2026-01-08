import matplotlib.pyplot as plt
import json
import pandas as pd

selezionate = []

# generazione del grafico con le nazioni selezionate
def generaGrafico(df):

        global selezionate
        if not selezionate: # se la lista selezionate è vuota quano viene chiamato
            print("Nessuna nazione selezionata per il grafico.")
            return

        fig, graficoSelezionate = plt.subplots(figsize=(12,6)) # crea il grafico

        for dati_nazione in selezionate:
            graficoSelezionate.plot(
                dati_nazione["Anno"],
                dati_nazione["Emissioni_CO2"],
                label=dati_nazione["Nazione"].iloc[0],
                marker = "o"
            )

        graficoSelezionate.set_title('Andamento Emissioni CO2 delle nazioni selezionate', fontsize=16)
        graficoSelezionate.set_xlabel('Anno', fontsize=12)
        graficoSelezionate.set_ylabel('Emissioni CO₂', fontsize=12)
        graficoSelezionate.legend(title='Nazione', loc='upper right')
        graficoSelezionate.grid(axis='y', linestyle='--')
        graficoSelezionate.set_xticks(df['Anno'].unique())

        selezionate.clear() # svuota la lista

        return fig

      # controllo sull'input della nazione
def controlloInput(nazione, df):
    # controlla l'input e restituisce il nuovo df o none
    nazione = nazione.strip().lower() # rimuove spazi bianchi prima o dopo la parola

    df_selezionata = df[df["Nazione"].str.lower() == nazione] #crea il df

    if df_selezionata.empty:
        return None
    else:
        return df_selezionata

# gestione delle nazioni date in input
def onInviaClick(df, inputNazione):
    # gestisce il click sul pulsante

    global selezionate

    nazione = inputNazione.strip()
    df_nazione = controlloInput(nazione, df)

    if df_nazione is None:
        return f" Errore: La nazione '{nazione}' non è presente nel dataset."

    elif nazione in [n.lower() for n in selezionate]:
        return f"La nazione '{nazione}' è già stata selezionata."
    
    selezionate.append(df_nazione)

    return f"Nazione '{nazione}' aggiunta. Totale: {len(selezionate)}"