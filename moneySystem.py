class MoneySystem:
    def __init__(self):
        self.load_money_balance()  # Загружаем баланс при создании объекта

    def load_money_balance(self):
        try:
            with open("C:\\Users\\User\\Desktop\\machine\\pyth\\111\\_money.txt", "r") as file:
                self.money = int(file.read())
        except FileNotFoundError:
            self.money = 0

    def add_money(self, amount):
        if amount > 0:
            self.money += amount
            print("Сумма добавлена.")
            self.save_money_balance()  # Сохраняем баланс после изменения
        else:
            print("Сумма должна быть положительной.")

    def subtract_money(self, amount):
        if amount > 0 and amount <= self.money:
            self.money -= amount
            print("Сумма уменьшена.")
            self.save_money_balance()  # Сохраняем баланс после изменения
        else:
            print("Недостаточно средств или неверная сумма.")

    def set_money(self, amount):
        if amount >= 0:
            self.money = amount
            print("Баланс обновлен.")
            self.save_money_balance()  # Сохраняем баланс после изменения

    def show_balance(self):
        self.load_money_balance()  # Загружаем баланс перед показом
        print(f"Ваш баланс: {self.money}")

    def save_money_balance(self):
        with open("C:\\Users\\User\\Desktop\\machine\\pyth\\111\\_money.txt", "w") as file:
            file.write(str(self.money))

def main_menu():
    money_system = MoneySystem()

    while True:
        print("Меню управления деньгами")
        print("1. Добавить деньги")
        print("2. Уменьшить деньги")
        print("3. Установить значение денег")
        print("4. Показать баланс")
        print("5. Выйти")
        choice = input("Выберите опцию: ")

        if choice == "1":
            amount = int(input("Введите сумму для добавления: "))
            money_system.add_money(amount)
        elif choice == "2":
            amount = int(input("Введите сумму для уменьшения: "))
            money_system.subtract_money(amount)
        elif choice == "3":
            amount = int(input("Введите новое значение баланса: "))
            money_system.set_money(amount)
        elif choice == "4":
            money_system.show_balance()
        elif choice == "5":
            print("Выход из программы.")
            break

if __name__ == "__main__":
    main_menu()
