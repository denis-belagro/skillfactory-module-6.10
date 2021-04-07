class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_client(self):
        return  "Клиент «" + self.name + "». Баланс: " + str(self.balance) + " руб."

client1 = Client("Иван Петров", 50)
print(client1.get_client())


