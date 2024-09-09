# Задание на тему "произвольное число параметров".

# Функция поиска однокоренных слов или похожих слов:
def  single_root_words (root_word, *other_words):
    same_words = []
    #root_word = root_word.lower() # Перевод  проверочного слова в нижний регистр для упрощения поиска.
    for word in other_words:
        #word = word.lower()  #Перевод слова из списка в нижний регистр для упрощения поиска.
        if word.lower().find(root_word.lower()) >= 0: # Проверка, если слово из списка включает в себя проверочное слово.
            same_words.append(word)
        if root_word.lower().find(word.lower()) >= 0: # Проверка, если проверочное слово включает в себя слово из списка.
           same_words.append(word)

    return same_words


# Запуск выполнения функции, согласно условию задачи:
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
