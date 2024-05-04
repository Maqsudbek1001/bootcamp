import random

GameOver = ValueError


def random_number():
    return random.randint(1, 10)


def check_number(number, guess):
    message = "Men o'ylagan son "

    if number < guess:
        return f"{message} {guess} dan kichikroq."

    if number > guess:
        return f"{message} {guess} dan kattaroq."

    raise GameOver


def main():
    number = random_number()
    print("Men 1-10 oralig'idagi bitta son o'yladim.")
    eng_kichik = 0
    eng_katta = 3

    while eng_kichik < eng_katta:
        try:
            guess = int(input("Tahmin kodingizni kiriting: "))
            message = check_number(number, guess)
            print(message)
            eng_kichik += 1

        except GameOver:
            print("O'ylangan sonni topdingiz.")
            break
    else:
        print("3 tadan ko'p urinish bo'ldi.")


if __name__ == '__main__':
    main()
