import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/feri_logy_analyza/200629_karting/200629130554_gps.log', header=None, sep=';')
df1 = pd.read_csv('data/feri_logy_analyza/200629_karting/kartfinal36pr3r.csv', header=None, sep=';')
df2 = pd.read_csv('data/200623_academy/200623110845_gps.log', header=None, sep=';')
df3 = pd.read_csv('data/200623_academy/200623111152_gps.log', header=None, sep=';')
df4 = pd.read_csv('data/200623_academy/200623120513_gps.log', header=None, sep=';')
df5 = pd.read_csv('data/200623_academy/200623121213_gps.log', header=None, sep=';')
df6 = pd.read_csv('data/200623_academy/200623122206_gps.log', header=None, sep=';')

df = df.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']

df1 = df1.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df1.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']

df2 = df2.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df2.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']
df3 = df3.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df3.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']
df4 = df4.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df4.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']
df5 = df5.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df5.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']
df6 = df6.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df6.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']

# print(df.head(50))

df = pd.read_csv('data/200623_academy/trasa23.csv', sep=';', header=None)
df = df.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
df.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']

df.plot(x='LAT', y='LON')
plt.show()

# df2.plot(x='LAT', y='LON')
# df3.plot(x='LAT', y='LON')
# df4.plot(x='LAT', y='LON')
# df5.plot(x='LAT', y='LON')
# df6.plot(x='LAT', y='LON')
# plt.show()

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

