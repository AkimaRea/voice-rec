#!/bin/bash

# Установка пинов
GPIO_PIN_IN=9
GPIO_PIN_OUT=10

# Экспортируем пины
echo $GPIO_PIN_IN > /sys/class/gpio/export
echo $GPIO_PIN_OUT > /sys/class/gpio/export

# Устанавливаем направление пинов
echo "in" > /sys/class/gpio/gpio$GPIO_PIN_IN/direction
echo "out" > /sys/class/gpio/gpio$GPIO_PIN_OUT/direction

# Функция для выполнения действия при наличии сигнала
execute_on_signal() {
    echo "Запуск скрипта..."
    # Здесь можно вызвать ваш скрипт
    /path/to/your/script.sh
}

# Основной цикл для мониторинга GPIO
while true; do
    # Чтение состояния пина
    SIGNAL=$(cat /sys/class/gpio/gpio$GPIO_PIN_IN/value)
    
    if [ "$SIGNAL" -eq "1" ]; then
        echo "1" > /sys/class/gpio/gpio$GPIO_PIN_OUT/value
        execute_on_signal
    else
        echo "0" > /sys/class/gpio/gpio$GPIO_PIN_OUT/value
    fi

    # Задержка для предотвращения чрезмерного использования процессора
    sleep 1
done