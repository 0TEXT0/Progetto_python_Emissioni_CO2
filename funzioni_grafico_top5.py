import matplotlib.pyplot as plt
import json
import pandas as pd

def graficoTop5(df):
  emissioni_totali = df.groupby('Nazione')['Emissioni_CO2'].sum().sort_values(ascending=False)
  top_5_nazioni = emissioni_totali.head(5).index

  fig, graficoTop5 = plt.subplots(figsize=(12, 6))

  for nazione in top_5_nazioni:
      dati_nazione = df[df['Nazione'] == nazione]
    # Disegna la linea per quella singola nazione sugli assi graficoTop5
      graficoTop5.plot(
        dati_nazione['Anno'],          # Asse X: i valori della colonna Anno
        dati_nazione['Emissioni_CO2'], # Asse Y: i valori delle Emissioni_CO2
        label=nazione,                 # label: Aggiunge il nome del Paese per la legenda
        marker='o'                     # marker='o': Mette un puntino su ogni dato per chiarezza
      )

# Aggiunge titoli, etichette e legenda agli assi graficoTop5
  graficoTop5.set_title('Andamento Emissioni CO2 delle Top 5 Nazioni (2001-2012)', fontsize=16)
  graficoTop5.set_xlabel('Anno', fontsize=12)
  graficoTop5.set_ylabel('Emissioni CO₂', fontsize=12)
  graficoTop5.legend(title='Nazione', loc='upper right') # loc='upper right' sposta la legenda in alto a destra
  graficoTop5.grid(axis='y', linestyle='--') # grid: Aggiunge le linee orizzontali di griglia
  graficoTop5.set_xticks(df['Anno'].unique()) # xticks: Forza l'asse X a mostrare tutti gli anni (2001, 2002, etc.)
  return fig