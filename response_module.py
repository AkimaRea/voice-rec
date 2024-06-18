from read_json_module import search_and_execute
from tts_module import speak_text

additional_message = ". Если остались еще вопросы, то с радостью отвечу!"
file_path = 'data.json'

# def not_found_callback():
# 	speak_text('Можете пожалуйста повторить вопрос')

def response_callback(entry): 
	speak_text(text=entry['response'] + additional_message)

def calc_response(question): 
	"""
	Вычисляет ответ на заданный вопрос.

	:param question: Текст вопроса
	"""

	if not question:
		return

	if question:
		search_and_execute(file_path=file_path, substring=question, callback=response_callback)
