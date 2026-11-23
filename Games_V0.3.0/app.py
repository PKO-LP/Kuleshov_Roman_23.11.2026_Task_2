# ВЕРСИЯ 0.3.0 ОСНОВНОЙ КОД
secret_1 = 102
secret_2 = 4

secrets = [secret_1, secret_2]

for secret in secrets:
    attempts = 0
    print("Хэй! Я загадал число! Сможешь его отгадать?)")
    print("(По секреты скажу, я загадал от одного до 105)")

    while True:
        guess = input("Введи свое число: ")
        attempts += 1

        if guess == "six seven":
            print("Ты нашел секретную первую пасхалочку😃✨! Теперь введи обычное число:")
        if guess == "Бибирево это район бобров":
                    print("Ты нашел секретную вторую пасхалочку😃✨! Теперь введи обычное число:")
        else:
            guess = int(guess)
            if guess < secret:
                print("Больше!")
            elif guess > secret:
                print("Меньше!")
            else:
                print(f"Победа! Ты угадал число {secret} за {attempts} попыток.")
                break

print("\nИгра окончена! Ты отгадал все 2 числа.")
