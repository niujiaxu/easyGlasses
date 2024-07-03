import pyaudio
import wave

# 参数设置
FORMAT = pyaudio.paInt16  # 采样深度
CHANNELS = 1              # 单声道
RATE = 44100              # 采样率
CHUNK = 1024              # 块大小
RECORD_SECONDS = 5        # 录音时间
WAVE_OUTPUT_FILENAME = "output.wav"  # 输出文件名

audio = pyaudio.PyAudio()

# 打开麦克风流
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# 开始录制
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# 停止并关闭麦克风流
stream.stop_stream()
stream.close()
audio.terminate()

# 保存音频数据到文件
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
