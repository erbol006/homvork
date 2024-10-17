
movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}
def check(film):
    if film in movies:
        return True
    else:
        return False


def add_film(valid, film):
    if valid is False:
        movies[film] = dict()
        print("Фильм успешно добавлен!")
    else:
        print("Этот фильм уже существует!")

def add_rating(valid, film_name):
    if valid is True:
        name_user = input("Введите ваше имя: ").title()
        if name_user not in movies[film_name]:
            rating = int(input("Оцените фильм (от 0 до 10): "))
            if 0 <= rating <= 10:
                movies[film_name][name_user] = rating
                print(f"Оценка добавлена для {film_name}: {name_user} оценил его на {rating}!")
            else:
                print("Только от 0 до 10!")
        else:
            print("Вы уже оценили этот фильм!")
    else:
        print("Такого фильма не существует!")

def show_ratings():
    for i in movies.keys():
        summa = 0
        count = 0
        if movies[i] != {}:
            for j in movies[i]:
                summa += movies[i][j]
                count += 1
            print(f"{i}: {round(summa / count, 0)}")
        else:
            print(f"Фильм {i} не имеет оценок!")

while True:
    ask = input("Выберите действие:\n1: Добавить фильм\n2: Добавить рейтинг\n3: Показать фильмы\n4: Выйти\nВаш выбор: ")

    if ask == '1':
        new_film = input("Название фильма: ").title()
        valid = check(new_film)
        add_film(valid, new_film)

    elif ask == '2':
        film_name = input("Выберите фильм: ").title()
        valid = check(film_name)
        add_rating(valid, film_name)

    elif ask == '3':
        show_ratings()

    elif ask == '4':
        break