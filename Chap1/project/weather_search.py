from sys import exit

class WeatherSearcher(object):
    def __init__(self):
        self.data_init()
        self._history = ""

    def data_init(self):
        self._data = {}
        with open('../resource/weather_info.txt', 'r') as f:
            for line in f:
                tmp = line.strip().split(',')
                self._data[tmp[0]] = tmp[1]

    def get_weather(self, city_to_search):
        if city_to_search in self._data.keys():
            weather = self._data[city_to_search]
            self._history += city_to_search + " " + weather + "\n"
            return weather
        else:
            return None

    def get_help(self):
        help_info = '''
            输入城市名，查询该城市的天气数据；
            输入help或者h，获得帮助信息；
            输入history，显示查询历史；
            输入quit, 退出程序。
            '''
        return help_info

    def get_history(self):
        return self._history

def ischinese(user_input):
    """
    判断用户输入的数据是否是中文
    :param user_input:(str), 用户输入字符串信息
    """
    for i in user_input:
        if i < '\u4e00' or i > '\u9fa5':
            return False
    return True


def run():
    # 初始化城市天气搜索类
    weather_searcher = WeatherSearcher()
    while True:
        try:
            city_to_search = input("请输入指令和你要查询的城市名: ")
        except BaseException as err:
            print("你的输入导致系统报错，gg")
            exit(0)
        # 输入矫正
        city_to_search = city_to_search.replace(" ", "")
        # 判断输入内容
        if city_to_search == "quit":
            print("再见！")
            exit(0)
        elif city_to_search in ["help", "h"]:
            print(weather_searcher.get_help())
        elif city_to_search == "history":
            print(weather_searcher.get_history())
        elif ischinese(city_to_search):
            weather = weather_searcher.get_weather(city_to_search)
            if weather is not None:
                print("{city}的天气状况为{weather}".format(city=city_to_search,
                weather=weather))
            else:
                print("你要查找的城市没有找到，请重新输入!可以输入help或者h查看帮助信息。")
        else:
            print("你输入的不是中文，请重新输入，或者输入help或者h需求帮助，谢谢!")


if __name__ == "__main__":
    run()
