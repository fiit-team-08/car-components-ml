import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from similaritymeasures import area_between_two_curves, curve_length_measure, frechet_dist
from os import listdir
from shutil import copy

def init_dataframe_old(path):
    df = pd.read_csv(path, header=None, sep=';')
    df = df.drop(columns=[0, 1, 3, 5, 7, 9, 11, 13, 15, 17])
    df.columns = ['LAT', 'LON', 'UTMX', 'UTMY', 'HMSL', 'GSPEED', 'CRS', 'HACC', 'NXPT']
    return df

def init_dataframe(path):
    df = pd.read_csv(path, sep=',')
    return df

def create_and_save_images():
    for fileName in listdir('data/laps'):
        df = init_dataframe('data/laps/{}'.format(fileName))
        df.plot(x='LAT', y='LON')
        plt.savefig('data/laps_images/{}'.format(fileName[:-4]))

# df0 = init_dataframe_old('data/feri_logy_analyza/200629_karting/200629130554_gps.log')
# df1 = init_dataframe_old('data/feri_logy_analyza/200629_karting/kartfinal36pr3r.csv')
# df2 = init_dataframe_old('data/200623_academy/200623110845_gps.log')
# df3 = init_dataframe_old('data/200623_academy/200623111152_gps.log')
# df4 = init_dataframe_old('data/200623_academy/200623120513_gps.log')
# df5 = init_dataframe_old('data/200623_academy/200623121213_gps.log')
# df6 = init_dataframe_old('data/200623_academy/200623122206_gps.log')
# df7 = init_dataframe_old('data/200623_academy/trasa23.csv')

# df0.plot(x='LAT', y='LON')
# df1.plot(x='LAT', y='LON')
# df2.plot(x='LAT', y='LON')
# df3.plot(x='LAT', y='LON')
# df4.plot(x='LAT', y='LON')
# df5.plot(x='LAT', y='LON')
# df6.plot(x='LAT', y='LON')
# df7.plot(x='LAT', y='LON')

ref1 = init_dataframe('data/ref1.csv')
ref2 = init_dataframe('data/ref2.csv')
# traces1 = init_dataframe('data/traces1.csv')
# traces2_1 = init_dataframe('data/traces2-1.csv')
# traces2_2 = init_dataframe('data/traces2-2.csv')

# traces2_1.plot(x='LAT', y='LON')
# traces2_2.plot(x='LAT', y='LON')
# plt.show()

# fig = plt.figure()
# for frame in [df2, df7]:
#     plt.plot(frame['LON'], frame['LAT'])
#plt.show()

def create_curve(dataframe):
    curve = np.zeros((dataframe.shape[0], 2))
    curve[:, 0] = dataframe.LON
    curve[:, 1] = dataframe.LAT
    return curve

def find_out_difference():
    ref1 = init_dataframe('data/ref1.csv')
    ref2 = init_dataframe('data/ref2.csv')

    ideal_curve_ref1 = create_curve(ref1)
    ideal_curve_ref2 = create_curve(ref2)
    laps_dir = 'data/laps'

    nameColumn = 'Name'
    frechetColumn = 'Frechet distance'
    curveLenColumn = 'Curve length measure'
    data_structure = {nameColumn: [], frechetColumn: [], curveLenColumn: []}
    difference_df = pd.DataFrame(data=data_structure)

    for fileName in listdir(laps_dir):
        lap = init_dataframe('{}/{}'.format(laps_dir, fileName))
        experimental_curve = create_curve(lap)

        ideal_curve = ideal_curve_ref1 if fileName.startswith('lap1') else ideal_curve_ref2
        fd = frechet_dist(experimental_curve, ideal_curve)
        cl = curve_length_measure(experimental_curve, ideal_curve)    

        difference_df = difference_df.append({nameColumn: fileName, frechetColumn: fd, curveLenColumn: cl}, ignore_index=True)
        print(fileName)

    difference_df.to_csv('data/differences.csv', index=False)

def init_dataframe_differences():
    df = pd.read_csv('data/differences.csv')
    return df

# differences_df = init_dataframe_differences()
# differences_df.plot.scatter(x='Frechet distance', y='Curve length measure')
# plt.show()

# fig = plt.figure()
# for frame in [df, df1]:
#     plt.plot(frame['LON'], frame['LAT'])

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(df['LON'], df['LAT'], df['GSPEED'])

# df1['NXPT'].plot()

# plt.show()

