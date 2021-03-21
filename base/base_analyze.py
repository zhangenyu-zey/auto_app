import yaml


def get_file_data(data_key,file_path):
    '''
    读取数据
    :param data_key: 测试函数
    :param file_path: 数据路径
    :return: 数据列表
    '''
    with open(file_path,"r",encoding="utf-8")as f:
        data_all = yaml.load(f,Loader=yaml.FullLoader)
        data_dict = data_all[data_key]
        data_list = []
        for value in data_dict.values():
            data_list.append(value)
        return data_list
