
country_flags = {'us':{'белый','синий','красный'},
                 'ru':{'красный', 'синий', 'белый'},
                 'ua':{'жолтый', 'синий'},
                 'tr':{'красный', 'белый'}}
while True:
    user_choice = input("ведите цвет флага ").split()
    if 'выйти' in user_choice:
        print("вы остоновили програму")
        break
    match_countries = []
    for country, colors in country_flags.items():
        if all(color in colors for color in user_choice):
            match_countries.append(country)

    if match_countries:
        print(f"вот что вышла по вашым запросам {match_countries}")
    else:
        print("не правельна вели ")
