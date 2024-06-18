from gtts import gTTS
from io import BytesIO
import pygame

# Текст для озвучки
text = ""

# Создание объекта gTTS и передача текста
tts = gTTS(text, lang='ru')

# Использование BytesIO для хранения аудиоданных в памяти
audio_data = BytesIO()
tts.write_to_fp(audio_data)

# Инициализация Pygame
pygame.mixer.init()
audio_data.seek(0)
pygame.mixer.music.load(audio_data)
pygame.mixer.music.play()

# Ожидание завершения воспроизведения
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)