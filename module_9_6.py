# Выполнение задания на тему "генераторы".

def all_variants(text):
    i = 0

    for j in range(1, len(text)+1):
        while i+j <= len(text):
            yield text [i:i+j]    # Вывод комбинаций в соответствии с примером тестового вывода из задания.
            i +=1
        i = 0


a = all_variants("abc")
for i in a:
    print(i)



