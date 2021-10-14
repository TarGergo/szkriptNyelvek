import random
from typing import List, Dict

import numpy as np

LOTTERY_NUMBERS_MINIMUM = 1
LOTTERY_NUMBERS_MAXIMUM = 90
LOTTERY_NUMBERS_COUNT = 5


def generate_lottery_tickets(count: int) -> List[np.ndarray]:
    result = []
    for _ in range(count):
        result.append(np.sort(generate_lottery_ticket()))
    return result


def generate_lottery_ticket() -> np.ndarray:

    result = []
    while np.unique(result).size != 5:
        result = []
        for _ in range(LOTTERY_NUMBERS_COUNT):
            lottery_number = round((LOTTERY_NUMBERS_MAXIMUM - LOTTERY_NUMBERS_MINIMUM) * random.random()) + LOTTERY_NUMBERS_MINIMUM
            result.append(lottery_number)
    return np.sort(result)

def check_winner_tickets(tickets : List[np.ndarray], pulled_numbers: np.ndarray) -> Dict:

    return {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0
    }

def calculate_total_prizes(tickets: List[np.ndarray], pulled_numbers: np.ndarray, prize_lookup: np.ndarray) -> int:

    return 0