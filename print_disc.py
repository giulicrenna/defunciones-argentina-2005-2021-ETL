import pandas as pd
import seaborn as sns
import re

datos : pd.DataFrame = pd.read_csv('defunciones.csv', encoding='ISO-8859-1')

for i in datos['clasificacion'].unique():
    print(f'-> {i}')