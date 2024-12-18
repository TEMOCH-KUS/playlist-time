# playlist-time
# Ranepa case 2 for timp education
## project_7

# Представим, что некое приложение хранит плейлист песен в двух видах:
# * кортеж строк
# * словарь
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
# * может принимать как первый плейлист, так и второй в качестве аргумента
# * принимает параметр n, число. Это количество песен
# * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any

playlist_c = (
"Happy Nation; 3.32",
"It's My Life; 3.59",
"Lady(Hear Me Tonight); 5.07",
"Fields Of Gold; 3.38",
"The Winner Takes It All; 4.54",
"Self Control; 4.06",
"I Shot The Sheriff; 4.57",
"Don't Give Up; 6.34",
"Relax, Take It Easy; 4.30",
"Dancing Queen; 3.36",
)

playlist_b = {
'Портофино': 3.32,
'Снег': 4.35,
'Попытка №5': 3.23,
'Тополиный Пух': 3.53,
'Если хочешь остаться': 4.48,
'Зеленоглазое такси': 5.52,
'Ты не верь слезам': 3.1,
'Nowhere to Run': 2.58,
'Салют, Вера': 4.44,
'Улетаю': 3.24,
'Опять метель': 3.37,
}

import random
import datetime

def _parse_duration(duration_str):
 
 minutes, seconds = map(float, duration_str.split('.'))
 return minutes * 60 + seconds

def _get_duration_from_tuple(playlist, n):
 
 total_seconds = 0
 for _ in range(n):
  song = random.choice(playlist)
  title, duration_str = song.split(';')
  total_seconds += _parse_duration(duration_str)
 return total_seconds

def _get_duration_from_dict(playlist, n):
 
 total_seconds = 0
 for _ in range(n):
  title = random.choice(list(playlist.keys()))
  total_seconds += playlist[title] * 60 # Преобразуем минуты в секунды
 return total_seconds

def get_duration(playlist, n: int) -> str:
 
 if isinstance(playlist, tuple):
  total_seconds = _get_duration_from_tuple(playlist, n)
 elif isinstance(playlist, dict):
  total_seconds = _get_duration_from_dict(playlist, n)
 else:
  raise TypeError("Неверный тип плейлиста.")

 total_minutes, total_seconds = divmod(total_seconds, 60)
 total_hours, total_minutes = divmod(total_minutes, 60)
 return f"{int(total_hours):02}:{int(total_minutes):02}:{int(total_seconds):02}"


print(get_duration(playlist_c, 500)) 
print(get_duration(playlist_b, 500)) 
