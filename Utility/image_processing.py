from numpy import zeros


def thermal_conversion(image):
    # Получить размеры изображения
    height, width = image.shape[:2]

    # Создать массив для хранения результатов
    temperatures = zeros((height, width))

    # Обойти изображение построчно
    for i in range(height):
        for j in range(width):
            # Получить RGB-компоненты пикселя
            R, G, B = image[i][j]

            # Преобразовать RGB-компоненты в температуру (в °C)
            temperature = -0.095 * R + 0.193 * G + 0.212 * B + 20.890
            # Записать значение температуры в массив temperatures
            temperatures[i][j] = temperature

    return temperatures
