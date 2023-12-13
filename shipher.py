import time
import pyfiglet

def encrypt_text(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            char_code = str(ord(char.lower()) - 96)  #преобразуем букву в число
            encrypted_text += char_code + " "
        else:
            encrypted_text += str(ord(char)) + " "  #если символ не буква, используем ASCII код
    return encrypted_text.strip()

def decrypt_text(text):
    decrypted_text = ""
    numbers = text.split()  #разделяем числа по пробелам
    for number in numbers:
        if number.isdigit():
            char_code = int(number)
            if 1 <= char_code <= 26:  #проверка, что это код буквы
                char_code += 96
                decrypted_text += chr(char_code)
            else:
                try:
                    decrypted_text += chr(char_code)  #попробуем использовать chr()
                except ValueError:
                    decrypted_text += f"#{char_code}#"  #если chr() не работает, добавим метку
        else:
            decrypted_text += f"#{number}#"  #если это не число, добавим метку
    return decrypted_text

def main():
    print("Loading...")
    time.sleep(2)
    print("Loaded!")
    time.sleep(0.5)
    result = pyfiglet.figlet_format("PurpleCode")
    print(result)

    while True:
        print("Выберите режим:")
        print("1. Шифрование (буквы в цифры)")
        print("2. Дешифрование (цифры в буквы)")
        print("3. Выход")
        choice = input("Введите номер выбранного режима: ")

        if choice == "1":
            plaintext = input("Введите текст для шифрования: ")
            encrypted_text = encrypt_text(plaintext)
            print("Зашифрованный текст:", encrypted_text)
        elif choice == "2":
            ciphertext = input("Введите текст для дешифрования: ")
            decrypted_text = decrypt_text(ciphertext)
            print("Расшифрованный текст:", decrypted_text)
        elif choice == "3":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
