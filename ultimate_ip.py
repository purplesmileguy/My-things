import socket

def get_ip_address():
    try:
        # Получаем имя хоста
        host_name = socket.gethostname()
        # Получаем IP-адрес, связанный с именем хоста
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.error as e:
        print(f"Ошибка при получении IP-адреса: {e}")
        return None

if __name__ == "__main__":
    ip_address = get_ip_address()
    
    if ip_address:
        print(f"IP-адрес вашего компьютера: {ip_address}")
    else:
        print("Не удалось получить IP-адрес.")
