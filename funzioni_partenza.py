import pandas as pd
import json

def caricaOttieniDf(nome_file):
    with open(nome_file, "r") as file:
        stringa_python = file.read()

    oggetto_python = json.loads(stringa_python)
    df = pd.DataFrame(oggetto_python)
    return df

# creazione tabella di partenza
def tabella(df):
  pd.set_option('display.float_format', '{:,.0f}'.format)

  df_tabella=df.pivot(index="Nazione", columns="Anno", values="Emissioni_CO2")

  return df_tabella
