from abc import ABC, abstractmethod

class Database(ABC):
    @staticmethod
    @abstractmethod
    def connect():
        pass

class MySQL(Database):
    @staticmethod
    def connect():
        return "Connected to MySQL Database"

print(MySQL.connect())
