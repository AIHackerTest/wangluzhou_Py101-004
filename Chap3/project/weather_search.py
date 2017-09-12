# encoding: utf-8
'''
输入城市名，查询该城市的天气数据；
输入help或者h，获得帮助信息；
输入history，显示查询历史；
输入 c，切换到摄氏度；
输入 f，切换到华氏度；
输入quit, 退出程序。

TODO: 不应该把WeatherSearcher和某个API深度纠缠
'''
__version__ = "V0.1.1"
__author__ = "luke"
__lisence__ = "MIT@2017-08"

from sys import exit
import requests
import json

def fetch_weather_by_seniverse(city_to_search, unit='c'):
    key = '8psxortvwf7jkdow', # API 密匙
    language = 'zh-Hans',  # 查询结果的返回语言
    url = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
    # 使用get方法交互的时候，参数的顺序不能任意变化
    result = requests.get(url, params={
        'key': key, # API 密匙
        'location': city_to_search, # 所要搜索的城市
        'language': language,  # 查询结果的返回语言,
        'unit': unit # 温度单位
    }, timeout=5)
    data = (json.loads(result.text)) # data为dict类型
    # print(data)  # for debug
    if "status" in data: # 说明没有查到任何信息
        return None
    data = data["results"][0] # 获取主干信息，类型为字典
    # print(type(data["now"]["temperature"]))
    # 将返回信息封装成字典类型
    response_info = {"city" : data["location"]["name"],
                     "description" : data["now"]["text"],
                     "temperature" : data["now"]["temperature"] + unit,
                     "update_time": data["last_update"]}
    return response_info


def fetch_weather_by_open_weather_map(city_to_search, unit):
    # TODO: 关注API的返回的json的相同性，如果不同就算了
    pass


class WeatherSearcher(object):
    def __init__(self):
        self._history = []
        self._unit = 'c' # 温度单位默认是摄氏度
        self._api_name = "seniverse" # 默认使用心知天气
        self._api_dict = {"open_weather_map":fetch_weather_by_open_weather_map,
                          "seniverse":fetch_weather_by_seniverse}
    def get_weather(self, cities_to_search):

        response_info_dict = dict()
        for city_to_search in cities_to_search:
            try:
                response_info = self._api_dict[self._api_name](city_to_search, self._unit)
                # self._history[city_to_search] = response_info
                # self.add_history(city_to_search, response_info)
                response_info_dict[city_to_search] = response_info
                # print("get_weather" + response_info) # for debug
            except BaseException as err:
                raise
                print("API查询异常!")
                response_info_dict[city_to_search] = None
        return response_info_dict

    def get_history(self):
        return self._history

    def search_history(self, city_to_search):
        if city_to_search in self._history:
            return self._history[city_to_search]
        else:
            return None

    def set_unit(self, unit):
        self._unit = unit

    def set_api(self, api_name):
        self._api_name = api_name

    def add_history(self, city, result):
        self._history.append(result)
