import urllib
import scipy.io.wavfile
import pydub
import numpy as np
import matplotlib.pyplot as plt

rate, data = scipy.io.wavfile.read("sampleMusic/GoingDownbyJakeChudnow.wav")

# print(rate) # 44100

# print(data) # stereo recording (left and right channel)
# print(data.shape[0]) #978554

channel1 = data[:,0] # left
channel2 = data[:,1] # right

wavLength = data.shape[0]/rate

print(wavLength," seconds ")

# scipy.io.wavfile.write("sampleMusic/GDJC_SLOW.wav", 30000, data)


# Energy of music 
np.sum(channel1.astype(float)**2)

#power - energy per unit of time
1.0/(2*(channel1.size)+1)*np.sum(channel1.astype(float)**2)/rate

#create a time variable in seconds
time = np.arange(0, float(data.shape[0]), 1) / rate

#plot amplitude (or loudness) over time
plt.figure(1)
plt.subplot(211)
plt.plot(time, channel1, linewidth=0.01, alpha=0.9, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(212)
plt.plot(time, channel2, linewidth=0.01, alpha=0.9, color='#ff7f00')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()