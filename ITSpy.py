# Індивідуальне творче завдання
# Варіант завдання: Лікар

while True:
    print("/-----------------------------\\")
    print('|    Програма "Лікувальник"    |')
    print("\\-----------------------------/")
    print()
    print("1. Облік пацієнтів")
    print("2. Види аналізів")
    print("3. Графік прийому пацієнтів")
    print("4. Найпопулярніші хвороби ")
    print("5. Калькулятор доз лікарських засобів")
    print("6. BMI калькулятор")
    print("7. Про програму")
    print("0. Вихід")
    print()
    s = input("Оберіть пункт меню -> ")

    if s == "0":   # Вихід з програми
        print("Програму завершено.")
        exit()

    if s == "7":   # Про програму
        print("/-----------------------------\\")
        print('|    Програма "Лікувальник"    |')
        print("\\-----------------------------/")
        print()
        print("Розробив: Гайдамака Даниїл Максимович")
        print("          група КН-Б23")
        print()
        print("Натисніть Enter для продовження.")
        input()

    if s == "1":    #Облік пацієнтів
      print("/-----------------------------\\")
      print('|    Програма "Лікувальник"    |')
      print("\\-----------------------------/")
      print()
      i  = input("Введіть П.І.Б: ")
      i2 = input("Введіть дату народження: ")
      i3 = input("Адреса проживання: ")
      i4 = input("Контактний телефон: ")
      i5 = input("Інформація про хворобу або травму: ")
      print()
      print("Натисніть Enter для продовження.")
      input()

    if s == "2":    #Види аналізів
     print("/-----------------------------\\")
     print('|    Програма "Лікувальник"    |')
     print("\\-----------------------------/")
     print()
     print("Види аналізів")
     print("1. Клінічний аналіз крові")
     print("2. Загальний аналіз сечі")
     print("3. Біохімічний аналіз крові")
     print("4. Гемоглобін")
     print("5. Специфічні показники еритроцитів")
     print("6. Специфічні показники лейкоцитів")
     print()
     print("Натисніть Enter для продовження.")
     input()

    if s == "3":   #Графік прийому пацієнтів
     print("/-----------------------------\\")
     print('|    Програма "Лікувальник"    |')
     print("\\-----------------------------/")
     print()
     print("/-----------------------------\\")
     print('| Понеділок - з 8:00  - 14:00  |')
     print('| Вівторок  - з 12:00 - 18:00  |')
     print('| Cереда    - з 8:00  - 14:00  |')
     print('| Четвер    - з 12:00 - 18:00  |')
     print('| Пятниця   - з 8:00  - 14:00  |')
     print('| Cубота    - з 8:00  - 11:00  |')
     print("\\-----------------------------/")
    print()

    if s == "4":    #Найпопулярніші хвороби
     print("/-----------------------------\\")
     print('|    Програма "Лікувальник"    |')
     print("\\-----------------------------/")
     print()
     print("Найвідоміші хвороби: ")
     print("1. Серцево-судинні захворювання: ")
     print("2. Інфекційні захворювання: ")
     print("3. Респіраторні захворювання: ")
     print("4. Цукровий діабет: ")
     print("5. Рак: ")
     print("6. Ожиріння: ")
     print("7. Психічні розлади: ")

    if s == "5":    #Калькулятор доз лікарських засобів
        print("/-----------------------------\\")
        print('|    Програма "Лікувальник"    |')
        print("\\-----------------------------/")
        print()
        print("Калькулятор дозованості лікарських засобів: ")
        weight = float(input("Введіть вагу пацієнта (кг): "))
        age = int(input("Введіть вік пацієнта: "))

        # Введення даних про ліки
        medication_name = input("Введіть назву лікарського засобу: ")
        standard_dose = float(input("Введіть стандартну дозу лікарського засобу (мг): "))

        # Розрахунок дози на основі ваги та віку
        adjusted_dose = standard_dose * (weight / 70) * (age / 30)

        # Виведення результату
        print("\nДля пацієнта вагою ", weight," кг та віком ", age," років.")
        print("Рекомендована доза ", medication_name, " ", adjusted_dose, "мг.")

    if s == "6":    #BMI калькулятор
        print("/-----------------------------\\")
        print('|    Програма "Лікувальник"    |')
        print("\\-----------------------------/")
        print()
        print("BMI(індекс маси тіла) калькулятор:")
        # Введення ваги та зросту від користувача
        weight = float(input("Введіть вагу в кілограмах: "))
        height = float(input("Введіть зріст в метрах: "))

        # Розрахунок BMI
        bmi = weight / (height ** 2)

        # Виведення результату
        print("\nBMI:",bmi)

        # Визначення класифікації BMI
        if bmi < 18.5:
            print("Класифікація: Недостатня маса тіла")
        elif 18.5 <= bmi < 24.9:
            print("Класифікація: Нормальна маса тіла")
        elif 25 <= bmi < 29.9:
            print("Класифікація: Надлишкова маса тіла")
        else:
            print("Класифікація: Ожиріння")
    print()
    print("Натисніть Enter для продовження.")
    input()





