import pandas as pd
import matplotlib.pyplot as plt

def init_dataframe(path):
    df = pd.read_csv(path, header=None, sep=';')
    df = df.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
    df.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']
    return df

df0 = init_dataframe('data/feri_logy_analyza/200629_karting/200629130554_gps.log')
df1 = init_dataframe('data/feri_logy_analyza/200629_karting/kartfinal36pr3r.csv')
df2 = init_dataframe('data/200623_academy/200623110845_gps.log')
df3 = init_dataframe('data/200623_academy/200623111152_gps.log')
df4 = init_dataframe('data/200623_academy/200623120513_gps.log')
df5 = init_dataframe('data/200623_academy/200623121213_gps.log')
df6 = init_dataframe('data/200623_academy/200623122206_gps.log')
df7 = init_dataframe('data/200623_academy/trasa23.csv')

df0.plot(x='LAT', y='LON')
df1.plot(x='LAT', y='LON')
df2.plot(x='LAT', y='LON')
df3.plot(x='LAT', y='LON')
df4.plot(x='LAT', y='LON')
df5.plot(x='LAT', y='LON')
df6.plot(x='LAT', y='LON')
df7.plot(x='LAT', y='LON')
plt.show()

# fig = plt.figure()
# for frame in [df1, df2, df3, df4, df5, df6]:
#     plt.plot(frame['LON'], frame['LAT'])
# plt.show()

# fig = plt.figure()
# for frame in [df, df1]:
#     plt.plot(frame['LON'], frame['LAT'])

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(df['LON'], df['LAT'], df['GSPEED'])

# df1['NXPT'].plot()

# plt.show()

