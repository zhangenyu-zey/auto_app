import os

class Path:
    # data路径
    data_path = os.path.dirname(os.path.abspath(__file__))
    @classmethod
    def login_data(cls):
        return os.path.join(cls.data_path,"login_data.yaml")

    @classmethod
    def vip_data(cls):
        return os.path.join(cls.data_path,"vip_data.yaml")

    @classmethod
    def address_data(cls):
        return os.path.join(cls.data_path,"address_data.yaml")

if __name__ == '__main__':
    print(Path.login_data())