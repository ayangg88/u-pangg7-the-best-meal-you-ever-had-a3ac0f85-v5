"""The best meal I ever had was not a restaurant meal at all.

It was three in the morning, on the night my partner walked out, and I
found myself standing at the kitchen sink eating cold nasi goreng straight
from the pan with a spoon. No plate, no chair, no ceremony — just the
leftover rice, sweet soy sauce, and a fried egg, eaten where I stood.
Everything that day had hurt, one thing after another, and then this
small, ordinary mouthful did not. That is the whole memory: grief,
a cold pan, and one bite that finally felt kind. I still remember the
cool metal of the pan against my palm and the way the egg yolk broke
over the rice, sweet and salty at once, while the house stayed silent.
"""

import os

SENTENCE = "At 3 a.m. after she left, I ate cold nasi goreng from the pan with a spoon, standing at the sink, and the sweet soy and fried egg were the first thing that day that did not hurt."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
