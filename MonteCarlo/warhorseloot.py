import random


Loot_chance = 0.006

def hasLoot() -> bool:
    return random.randint() < Loot_chance

def week_sequence(no_of_weeks : int) -> bool:
    return any([hasLoot() for _ in range(no_of_weeks)])
