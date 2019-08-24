import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# tmp = []

# for i in range(32):
#    tmp += [math.sin(i)]

# sin = np.asarray(tmp)

# transformed = np.fft.fft(sin)



# plt.plot(transformed[0:sin.size//2])
# plt.show()

df = pd.read_csv('garbage_data.csv')
print(df.head())
plt.plot(df['EEG.AF3'])

frontal_signals = df[['EEG.F7', 'EEG.F3', 'EEG.FC5', 'EEG.FC6', 'EEG.F4', 'EEG.F8']]
frontal_numpy = frontal_signals.values

# print("The length of frontal_numpy is: ", len(frontal_numpy))

frontal_numpy_chunks = frontal_numpy[0:32]

for i in range(0, len(frontal_numpy), 32):
   frontal_numpy_chunks = np.append(frontal_numpy_chunks, frontal_numpy[i:i+32], axis=0)

print(frontal_numpy_chunks.shape)



# plt.plot(arry[:3])
# # print(df.dtypes)
# plt.show()