from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import sys
import json
from vosk import Model, KaldiRecognizer

from response_module import calc_response

model = Model("vosk-model-small-ru-0.22") # путь к модели
rec = KaldiRecognizer(model, 16000)

# Создание очереди для передачи аудио данных
audio_queue = queue.Queue()

is_response_started = False

# Обработка аудио данных в реальном времени
def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(bytes(indata))

# Инициализация потока записи
def recognize_audio():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',channels=1, callback=audio_callback):
        print("Начало распознавания. Говорите в микрофон...")
        while True:
            data = audio_queue.get()
            if rec.AcceptWaveform(data):
                result = rec.Result()
                text = json.loads(result)["text"]
                print("Распознано: " + text)
                calc_response(text)
                    

if __name__ == "__main__":
    try:
        recognize_audio()
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем")
    except Exception as e:
        print(str(e))