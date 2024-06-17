from vosk import Model, KaldiRecognizer
import pyaudio
from speakerpy.lib_speak import Speaker
from speakerpy.lib_sl_text import SeleroText

model = Model("C:\\Users\\IBMStation\\Desktop\\project\\vosk-model-small-ru-0.22") # полный путь к модели
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
speaker = Speaker(model_id="v3_1_ru", language="ru", speaker="xenia", device="cpu")
old_recognized=''

def responseAtText(text): 
	response = ''
 
	if text == 'история':
		response='история'
  
	if response != '':
		speaker.speak(text=response, sample_rate=48000, put_accent=True, put_yo=False)

while True:
		data = stream.read(16000)

		if len(data) == 0:
				break
			
		new_recognized = eval(rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult()).get('partial')
		if new_recognized != old_recognized:
				old_recognized = new_recognized
		else: continue 
  
		print(old_recognized)
		if old_recognized: responseAtText(old_recognized)

  