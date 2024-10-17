while True:
    word = input('Введите слово. Inter word. : ')

    if word.lower() in ['stop', 'exit', 'выход']:
        print("Выход .")
        break

    vowels_letters_latin = 'aeiou'
    vowels_letters_cyrillic = 'аеёиоуыэюя'
    consonant_letters_latin = 'bcdfghjklmnpqrstvwxyz'
    consonant_letters_cyrillic = 'бвгджзйклмнпрстфхцчшщъь'

    vowels = vowels_letters_latin + vowels_letters_cyrillic
    consonants = consonant_letters_latin + consonant_letters_cyrillic
    vowel_count = 0
    consonant_count = 0
    for symbol in word:
        if symbol.lower() in vowels:
            vowel_count += 1
        elif symbol.lower() in consonants:
            consonant_count += 1

    symbol_count = vowel_count + consonant_count
    print('Количество букв в слове:', symbol_count)
    print('Количество гласных букв:', vowel_count)
    print('Количество согласных букв:', consonant_count)

    if symbol_count > 0:
        vowel_percent = (vowel_count / symbol_count) * 100
        consonant_percent = (consonant_count / symbol_count) * 100
        print(f"Гласных букв: {vowel_percent:.2f}%")
        print(f"Согласных букв: {consonant_percent:.2f}%")
    else:
        print("В введенном слове нет букв.")














