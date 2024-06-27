import pyaudio
import wave

# デバイスインデックスとチャンネル数を指定
DEVICE_INDEX = 3  # MacBook Proのマイクのインデックス
CHANNELS = 1  # モノラル

# 録音の設定
FORMAT = pyaudio.paInt16  # 16ビットの音声
RATE = 44100  # サンプリングレート
CHUNK = 1024  # 一度に読み込むフレーム数
RECORD_SECONDS = 10  # 録音時間（秒）
OUTPUT_FILENAME = "output.wav"  # 出力ファイル名

# PyAudioのインスタンスを作成
audio = pyaudio.PyAudio()

try:
    # 録音の開始
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, input_device_index=DEVICE_INDEX,
                        frames_per_buffer=CHUNK)
    print("Recording...")

    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording")

    # 録音の終了
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 録音したデータをファイルに保存
    waveFile = wave.open(OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

except Exception as e:
    print(f"An error occurred: {e}")