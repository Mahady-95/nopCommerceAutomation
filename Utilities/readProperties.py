import configparser
config=configparser.RawConfigParser()

config.read("C:\\Users\\User\\PycharmProjects\\DCLSQA_V2\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURl():
        url=config.get('common info', 'baseUrl')
        return url
    @staticmethod
    def getUsername():
        username=config.get('common info', 'username')
        return username
    @staticmethod
    def getPasssword():
        password= config.get('common info','password')
        return password
