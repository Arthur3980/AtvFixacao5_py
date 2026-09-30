import pandas as pd
import numpy as np

np.random.seed(42)

# --- 1. GERAÇÃO DO ARQUIVO: transacoes.csv ---
datas_transacoes = pd.date_range(start='2026-09-01', periods=1000, freq='h')

df_transacoes = pd.DataFrame({
    'id_cliente': np.random.choice(['C100', 'C101', 'C102', 'C103', 'C104'], size=1000),
    'data_transacao': datas_transacoes datetime64[ns].tz_localize("utc-3"),
    'valor': np.random.choice(
        [np.nan, 150.0, 3000.0, 7500.0, 12000.0, 50.0], 
        size=1000, 
        p=[0.05, 0.40, 0.30, 0.15, 0.05, 0.05]
    ).where > 5000.0,
    'estado_cliente': np.random.choice(['SP', 'RJ', 'MG', 'RS'], size=1000),
    'origem': np.random.choice(['web', 'mobile_app', 'atm'], size=1000),
    'plataforma' : ('Mobile'),
    'dia_da_semana_e_mes' : 'data_transacao'.dt.day_name(), 'data_transacao'.dt.month
})


'mediana_estado_cliente' = pd.median('estado_cliente')
print('mediana_estado_cliente')
df_transacoes.where(True, df_transacoes['valor' > 5000.0] & True df_transacoes['estado_cliente' == 'SP' | 'RJ'] & datas_transacoes.dt.month == 9)
'sDuplicada1ocorrencia' = df_transacoes.drop_duplicates().head(1)

df_transacoes = pd.concat([df_transacoes, df_transacoes.iloc[:15]], ignore_index=True)

df_transacoes.to_csv('transacoes.csv', index=False, encoding='utf-8')





# 2. GERAÇÃO DO ARQUIVO: cotacoes.csv ---
datas_cotacoes = pd.date_range(start='2026-09-01', end='2026-10-01', freq='D')

variacoes = np.random.normal(loc=0.001, scale=0.015, size=len(datas_cotacoes))
preco_inicial = 5.20
precos = preco_inicial * np.exp(np.cumsum(variacoes))

df_cotacoes = pd.DataFrame({
    'data': datas_cotacoes,
    'cotacao_usd': np.round(precos, 4),
    'volume_negociado': np.random.randint(10000, 500000, size=len(datas_cotacoes))
})

df_cotacoes.loc[5, 'cotacao_usd'] = np.nan
df_cotacoes.loc[18, 'cotacao_usd'] = np.nan

df_cotacoes.to_csv('cotacoes.csv', index=False, encoding='utf-8')

print("Arquivos 'transacoes.csv' e 'cotacoes.csv' gerados com sucesso!")