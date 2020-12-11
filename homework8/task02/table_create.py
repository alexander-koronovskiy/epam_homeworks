import sqlite3

conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute(
    """CREATE TABLE albums
                  (title text, artist text, release_date text,
                   publisher text, media_type text)
               """
)

# Вставляем данные в таблицу
cursor.execute(
    """INSERT INTO albums
                  VALUES ('Glow', 'Andy Hunter', '7/24/2012',
                  'Xplore Records', 'MP3')"""
)

# Сохраняем изменения
conn.commit()
