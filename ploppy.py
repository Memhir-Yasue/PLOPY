import urllib
import scipy.io.wavfile
import pydub

rate, data = scipy.io.wavfile.read("sampleMusic/GoingDownbyJakeChudnow.wav")

# print(rate) # 44100

# print(data) # stereo recording (left and right channel)
# print(data.shape[0]) #978554

wavLength = data.shape[0]/rate

print(wavLength," seconds ")

