import json

def read_json_file(file_path):
		"""
		Читает JSON-файл и возвращает данные.

		:param file_path: Путь к JSON-файлу.
		:return: Список словарей с полями 'request' и 'response'.
		"""
		try:
				with open(file_path, 'r', encoding='utf-8') as file:
						data = json.load(file)
						return data
		except FileNotFoundError:
				print(f"Файл {file_path} не найден.")
		except json.JSONDecodeError:
				print(f"Ошибка декодирования JSON в файле {file_path}.")
		return None

def search_substring_in_data(data, substring):
		"""
		Выполняет поиск включения подстроки в поле 'request' каждого словаря в списке.

		:param data: Список словарей с полями 'request' и 'response'.
		:param substring: Подстрока для поиска.
		:return: Список словарей, содержащих подстроку в поле 'request'.
		"""
		result = []
		for entry in data:
				request = entry.get('request', '')
				if request in substring:
						result.append(entry)
		return result

def search_and_execute(file_path, substring, callback):
		"""
		Ищет подстроку в JSON-файле и выполняет коллбэк при успешном нахождении.

		:param file_path: Путь к JSON-файлу.
		:param substring: Подстрока для поиска.
		:param callback: Функция, которая будет вызвана для найденной записи.
		"""
		data = read_json_file(file_path)
		if data is not None:
				found_entries = search_substring_in_data(data, substring)
				if found_entries:
						callback(found_entries[0])
				else:
						# not_found_callback()
						print(f"Записи, содержащие подстроку '{substring}', не найдены.")
		else:
				print("Не удалось прочитать данные из файла.")
		