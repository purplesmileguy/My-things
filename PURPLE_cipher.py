import time
import pyfiglet

def encrypt_text(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            char_code = str(ord(char.lower()) - 96)  # Преобразуем букву в число
            encrypted_text += char_code + " "
        else:
            encrypted_text += char + " "
    return encrypted_text.strip()


def decrypt_text(text):
    decrypted_text = ""
    numbers = text.split()
    for number in numbers:
        if number.isdigit():
            char_code = int(number) + 96  # Преобразуем число в букву
            decrypted_text += chr(char_code)
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
