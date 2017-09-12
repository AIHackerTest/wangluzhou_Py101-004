from apscheduler.schedulers.blocking import BlockingScheduler
from weather_search import WeatherSearcher
import json


def task():
    print("开始查询任务...")
    # 读取城市信息
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
        cities_to_search = data["section1"]["cities"]
    weather_searcher = WeatherSearcher()
    response_info_dict = weather_searcher.get_weather(cities_to_search)
    # print(response_info_dict) # for debug
    for key in response_info_dict:
        print(response_info_dict[key])


def crontab():
    sched = BlockingScheduler()
    # 读取配置文件
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
        # print(cities_to_search) # for debug
        hour = data["section2"]["search_time"]["hour"]
        # print(type(hour)) # for debug
        minute = data["section2"]["search_time"]["minute"]
        end_date = data["section2"]["end_date"]
        # print(end_date) # for debug
        # print(cities_to_search) # for debug
    # 由于有参数需要传递，因此将task函数在打包成一个lambda函数
    sched.add_job(task,'cron', day_of_week='*', hour=hour, minute=minute, end_date=end_date)
    # sched.add_job(lambda:task(cities_to_search), 'interval', seconds=10) # for debug 每10秒运行一次
    sched.start()

if __name__ == "__main__":
    crontab()
