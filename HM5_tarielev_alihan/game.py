import configparser
from game_logic import calculate_winnings, generate_winning_slot

config = configparser.ConfigParser()
config.read('settings.ini')
starting_money = int(config['DEFAULT']['MY_MONEY'])


def play_game ():
    money = starting_money
    while True:
        print(f"У вас есть {money}$")


        if money <= 0:
            print(' У вас недостаточно средств для продолжения игры')
            break

        slot = None
        while slot not in range(1, 11):
            try:
                slot = int(input("Выберите слот от 1 до 10: "))
                if slot < 1 or slot > 10:
                    print("Выбранный слот должен быть строго от 1 до 10!!!")

            except ValueError:
                print("Выбранный слот должен быть строго от 1 до 10!!!")

        bet_amount = int(input('Сколько денег вы хотитие поставить'))
        winning_slot = generate_winning_slot()
        winnings = calculate_winnings(bet_amount, slot, winning_slot)

        if winnings > 0:
            print(f"Вы выиграли {winnings}$!")
        else:
            print("Вы проиграли...")

        money += winnings

        play_again = input('Хотите сыграть еще раз (y/n): ')
        if play_again.lower() == "нет":
            break
    if money > starting_money:
        print(f"Поздравляем! Вы выиграли {money - starting_money}$.")
    else:
        print(f"К сожалению, вы проиграли {starting_money - money}$.")

if __name__ == "__main__":
    play_game()


