print("===== Loop Lab: Interaktiv Topshiriqlar =====")
print("1. 🎯 Maxfiy sonni toping (Random son o'yini)")
print("2. 🔄 So'zni teskari yozish")
print("3. 🔢 Sonlar orasidagi eng kichigini topish")
print("4. 🧮 FizzBuzz o'yini (1 dan N gacha)")
print("0. ❌ Dasturdan chiqish")
print("=============================================")

import random

while True:
    choice = input("Tanlovingizni kiriting (0-4): ")
    
    if choice == '1':
        import random
        secret_number = random.randint(1, 100)
        guess = None
        while guess != secret_number:
            guess = int(input("Maxfiy sonni toping (1-100): "))
            if guess < secret_number:
                print("Yana kattaroq son kiriting.")
            elif guess > secret_number:
                print("Yana kichikroq son kiriting.")
            else:
                print("Tabriklaymiz! Maxfiy sonni topdingiz!")
    
    elif choice == '2':
        word = input("So'zni kiriting: ")
        reversed_word = word[::-1]
        print(f"Teskari yozilgan so'z: {reversed_word}")
    
    elif choice == '3':
        numbers = list(map(int, input("Sonlarni kiriting (bo'shliq bilan ajratilgan): ").split()))
        if numbers:
            min_number = min(numbers)
            print(f"Eng kichik son: {min_number}")
        else:
            print("Hech qanday son kiritilmadi.")
    
    elif choice == '4':
        n = int(input("N ni kiriting: "))
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    
    elif choice == '0':
        print("Dasturdan chiqish...")
        break
    
    else:
        print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")
