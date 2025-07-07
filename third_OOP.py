class Server:
    def __init__(self, hostname, ip):
        self.hostname = hostname  # Название сервера
        self.ip = ip              # IP-адрес сервера
    
    def deploy(self):
        print(f"[{self.hostname}] Deploy application complite correct")
    
    def status(self):
        print(f"[{self.hostname}] Status: access (IP: {self.ip})")


class Database(Server):
    def __init__(self, hostname, ip, db_type):
        super().__init__(hostname, ip)  # Инициализация родительского класса
        self.db_type = db_type          # Тип базы данных (PostgreSQL, MySQL и т.д.)
    
    def backup(self):
        print(f"[{self.hostname}] Make backup {self.db_type} base... completed !")


# Демонстрация работы
if __name__ == "__main__":
    # Создаем объекты
    web_server = Server("WebByNew11", "192.168.22.10")
    db_server = Database("DBServer11", "192.168.22.20", "PostgreSQL")

    # Работа с обычным сервером
    print("="*50)
    web_server.deploy()
    web_server.status()

    # Работа с сервером баз данных
    print("="*50)
    db_server.deploy()
    db_server.status()
    db_server.backup()