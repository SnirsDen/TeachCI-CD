# 1. Базовый класс Service
class Service:
    def __init__(self,name):
        self.name = name # Общий атрибут для всех сервисов

    def start(self):
        print(f"Starting '{self.name}' service")

    def stop(self):
        print(f"Stopping'{self.name}' sevice")

# 2. Подкласс для systemd сервисов
class SystemdService(Service):
    def start(self):
        # Переопределенный метод запуска для systemd
        print(f"systemctl start {self.name}")

    def stop(self):
        # Переопределенный метод остановки для systemd
        print(f"systemctl stop {self.name}")

# 2. Подкласс для Docker контейнеров
class DockerService(Service):
    def start(self):
        print(f"docker start{self.name}")

    def stop(self):
        print(f"docker stop{self.name}")

# 3. Функция для выполнения методов на списке объектов
def execute_comand(service,method_name):
    for service in services:
        # Получаем метод по имени из текущего объекта
        method = getattr(service,method_name)
        # Вызываем метод
        method()

# Создаем тестовые объекты
if __name__ =="__main__":
    nginx_systemd = SystemdService("nginx")
    postgres_docker = DockerService("postgres")
    firewall_systemd = SystemdService("firewalld")
    
    # Формируем список сервисов
    services = [
        nginx_systemd,
        postgres_docker,
        firewall_systemd
    ]

    # Запускаем все сервисы
    print("Starting services:")
    execute_comand(services, "start")

    print("\nStoping services:")
    execute_comand(services,"stop")