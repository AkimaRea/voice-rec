from vosk import Model, KaldiRecognizer
import pyaudio

from response_module import calc_response
from tts_module import speak_text

model = Model("vosk-model-small-ru-0.22") # полный путь к модели
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()

stream = p.open(
		format=pyaudio.paInt16, 
		channels=1, 
		rate=16000, 
		input=True, 
		frames_per_buffer=16000
)
stream.start_stream()
old_recognized=''

""" speak_text(text="Привет, я голосовой помощник, разработан студентом Института Радиотехнических Систем и Управления кафедры САУ, готова ответить на интересующие вопросы") """

while True:
		data = stream.read(16000)

		if len(data) == 0:
				break
			
		new_recognized = eval(rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult()).get('partial')
		if new_recognized != old_recognized:
				old_recognized = new_recognized
		else: continue 
  
		print(old_recognized)
		if old_recognized: calc_response(old_recognized)