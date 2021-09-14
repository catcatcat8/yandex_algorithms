themes = dict()
num_message_to_num_theme = dict()  # номер сообщения => номер темы
theme_to_amount = dict()  # номер темы => количество упоминаний

n = int(input())
index = 1
theme_index = 1

for i in range(0, n):
    code = int(input())
    if (code == 0):
        theme_name = input()
        themes[theme_index] = theme_name
        message = input()
        num_message_to_num_theme[index] = theme_index
        theme_to_amount[theme_index] = 1
        theme_index += 1
    else:
        num_theme = num_message_to_num_theme[code]
        theme_to_amount[num_theme] += 1

        num_message_to_num_theme[index] = num_theme
        message = input()
    index += 1

max = 0
max_theme = ""
for key in theme_to_amount:
    if (theme_to_amount[key] > max):
        max_theme = themes[key]
        max = theme_to_amount[key]

print(max_theme)
