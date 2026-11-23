# ВЕРСИЯ 0.1.0 ОСНОВНОЙ КОД
secret_1 = 102
secret_2 = 4

secrets = [secret_1, secret_2]

for secret in secrets:
    attempts = 0
    print("Хэй! Я загадал число! Сможешь его отгадать?)")

    while True:
        guess = int(input("Введи свое число: "))
        attempts += 1

        if guess < secret:
            print("Больше!")
        elif guess > secret:
            print("Меньше!")
        else:
            print(f"Победа! Ты угадал число {secret} за {attempts} попыток.")
            break

print("\nИгра окончена! Ты отгадал все 2 числа.")
