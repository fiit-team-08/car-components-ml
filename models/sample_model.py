import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model

ref1 = pd.read_csv('data/ref1_v2.csv')
ref2 = pd.read_csv('data/ref2_v2.csv')
ref = pd.concat([ref1, ref2])

samples_out = ref['CMD'].to_numpy()
samples_out = samples_out.reshape((samples_out.shape[0], 1))
samples_in = ref[['LAT', 'LON', 'CRS', 'GSPEED', 'NLAT',
                  'NLON', 'NCRS']].to_numpy()

inp = Input(shape=(7,))
mid1 = Dense(10, activation='linear')(inp)
mid2 = Dense(10, activation='linear')(mid1)
mid3 = Dense(10, activation='linear')(mid2)
out = Dense(1, activation='linear')(mid3)
model = Model(inputs=inp, outputs=out)
model.summary()

model.compile(optimizer='adam', loss='mse', metrics=['mse', 'mae'])
model.fit(samples_in, samples_out, batch_size=500, epochs=220000)

# loss over 89,7%
model.save('sample_model.h5')

result = model.predict(samples_in)

fig = plt.figure()
plt.plot(result, label='Prediction')
plt.plot(samples_out, label='Real data')
plt.ylabel('Steering command')
plt.xlabel('Sample')
plt.legend(loc="upper left")
plt.show()

