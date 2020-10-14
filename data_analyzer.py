import pandas as pd

df = pd.read_csv('data/feri_logy_analyza/200629_karting/kartfinal36pr3r.csv', header=None, sep=';')

df = df.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']

print(df.head(50))

