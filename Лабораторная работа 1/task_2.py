# TODO Найдите количество книг, которое можно разместить на дискете

size_mb = 1.44  # Размер дискеты в Мб
pages_book = 100  # Количество страниц в книге
lines_page = 50    # Число строк на странице
symbols_in_line = 25    # Количество символов в строке
bytes_symbol = 4     # Количество байт для хранения одного символа

# Переводим в байты
disk_size_byte = size_mb * 1024 * 1024

# Объем одной книги в байтах
book_size_byte = pages_book * lines_page * symbols_in_line * bytes_symbol

# Количество книг, помещающихся на дискету
number_of_books = disk_size_byte // book_size_byte

print("Количество книг, помещающихся на дискету:", int(number_of_books))
