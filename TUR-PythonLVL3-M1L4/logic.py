import random
from datetime import datetime, timedelta


class Pokemon:

    pokemons = {}

    def __init__(self, trainer):

        self.trainer = trainer
        self.name = random.choice(["Pikachu", "Charmander", "Bulbasaur", "Squirtle"])
        self.hp = 100
        self.power = random.randint(10, 20)

        # son beslenme zamanı
        self.last_feed_time = datetime.min

        Pokemon.pokemons[trainer] = self


    async def info(self):

        return f"""
Pokemon: {self.name}
Trainer: {self.trainer}
HP: {self.hp}
Power: {self.power}
"""


    async def show_img(self):

        return f"https://img.pokemondb.net/artwork/{self.name.lower()}.jpg"


    async def attack(self, enemy):

        damage = random.randint(5, self.power)

        enemy.hp -= damage

        if enemy.hp <= 0:
            enemy.hp = 0
            return f"{self.trainer}'ın {self.name} pokemonu {enemy.trainer}'ın pokemonunu yendi!"

        return f"{self.trainer}'ın {self.name} pokemonu {enemy.trainer}'ın pokemonuna {damage} hasar verdi!"


    async def feed(self):

        now = datetime.now()
        interval = timedelta(seconds=20)

        if now - self.last_feed_time >= interval:

            self.hp += 10
            self.last_feed_time = now

            return f"{self.name} beslendi! Yeni HP: {self.hp}"

        else:

            next_time = self.last_feed_time + interval
            wait = int((next_time - now).total_seconds())

            return f"{self.name} henüz aç değil. {wait} saniye sonra tekrar besleyebilirsin."


class Fighter(Pokemon):

    async def feed(self):

        now = datetime.now()
        interval = timedelta(seconds=20)

        if now - self.last_feed_time >= interval:

            self.hp += 20   # Fighter daha fazla iyileşir
            self.last_feed_time = now

            return f"{self.name} güçlü bir şekilde beslendi! Yeni HP: {self.hp}"

        else:

            next_time = self.last_feed_time + interval
            wait = int((next_time - now).total_seconds())

            return f"{self.name} henüz tekrar beslenemez. {wait} saniye bekle."


class Wizard(Pokemon):

    async def feed(self):

        now = datetime.now()
        interval = timedelta(seconds=10)   # Wizard daha hızlı beslenir

        if now - self.last_feed_time >= interval:

            self.hp += 10
            self.last_feed_time = now

            return f"{self.name} sihirli şekilde beslendi! Yeni HP: {self.hp}"

        else:

            next_time = self.last_feed_time + interval
            wait = int((next_time - now).total_seconds())

            return f"{self.name} henüz tekrar beslenemez. {wait} saniye bekle."