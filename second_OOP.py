class User:
    def __init__(self,name, role):
        self.name = name    # публичный атрибут
        self.__role = role  # приватный атрибут (два подчеркивания)


    def get_role(self):
        return self.__role     # метод для получения роли
    
    def set_role(self,new_role):
        if new_role == "root":
            return "Error: it is forbidden role 'root'!"
        self.__role = new_role  # обновляем роль, если не root


user1 = User("Den", "admin")
user2 = User("David", "engineer")

print(f"{user1.name}: {user1.get_role()}")
print(f"{user2.name}: {user2.get_role()}")

user1.set_role("moderator")
print(f"Den change in: {user1.get_role()}")

error_message = user2.set_role("root")
print(error_message)
print(f"Role David not change: {user2.get_role()}")