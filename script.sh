#!/bin/bash

# Инициализация библиотек
gpio mode 9 in
gpio mode 10 out

# Функция для выполнения действия при наличии сигнала
execute_on_signal() {
    echo "Запуск скрипта..."
    # Здесь можно вызвать ваш скрипт
    /path/to/your/script.sh
}

# Основной цикл для мониторинга GPIO
while true; do
    # Чтение состояния пина
    SIGNAL=$(gpio read 9)
    
    if [ "$SIGNAL" -eq "1" ]; then
        gpio write 10 1
        execute_on_signal
    else
        gpio write 10 0
    fi

    # Задержка для предотвращения чрезмерного использования процессора
    sleep 1
done
