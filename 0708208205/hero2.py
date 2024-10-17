class SuperHiro:
    class SuperHero:
        people = 'people'

        def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
            self.name = name
            self.nickname = nickname
            self.superpower = superpower
            self.health_points = health_points
            self.catchphrase = catchphrase
            self.damage = damage
            self.fly = False

        def get_name(self):
            return self.name

        def double_health(self):
            self.health_points = self.health_points ** 2
            self.fly = True

        def __str__(self):
            return f"{self.nickname}: {self.superpower}, Health: {self.health_points}, Damage: {self.damage}, Fly: {self.fly}"

        def catchphrase_length(self):
            return len(self.catchphrase)

        def true_phrase(self):
            return f"True in the {self.catchphrase}"

class AirHero(SuperHiro.SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.air_property = "Can control winds"

class EarthHero(SuperHiro.SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.earth_property = "Can cause earthquakes"

class Villain(EarthHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 2

air_hero = AirHero("Peter Parker", "Spider-Man", "Web-slinging", 100, "With great power comes great responsibility!", 25)
earth_hero = EarthHero("Bruce Banner", "Hulk", "Super Strength", 150, "HULK SMASH!", 30)
villain = Villain("Loki", "God of Mischief", "Illusion", 120, "I am a god!", 35)

print(air_hero)
air_hero.double_health()
print(air_hero)
print(air_hero.true_phrase())

print(earth_hero)
earth_hero.double_health()
print(earth_hero)
print(earth_hero.true_phrase())

print(f"{villain.nickname} crit damage: {villain.crit()}")
print(f"Villain people type: {villain.people}")
