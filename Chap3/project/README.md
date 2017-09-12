## 未来计划
1. 封装API，可以实现API的自由切换
 - [国内API：心知天气](https://www.seniverse.com/api)


# 基础任务程序说明
## 环境要求
- Python 3.6.0
- Flask
- JQuery 3.1.1
- Semantic UI

## 编译和安装
本程序为Web程序。主程序为app.py, 执行：`Python app.py`即可。
## 特点
实时查询天气。

## 功能介绍
本程序为命令行形式的天气查询系统。功能要求如下:

- 输入城市名，查询该城市的天气数据；
- 点击[帮助]，获得帮助信息；
- 点击[历史]，显示查询历史。


## 技术介绍：
- WeatherSearcher类，相当于天气API的代理类
- 通过ajax方式实现前后端交互
- 用户历史查询记录存放在session中。

## Change Log
- 2017-09-03: 修改weatherSearcher类，增加fetch_weather_by_XXX函数，将天气查找类和API的关系松耦合化。
- 2017-09-10： 修改weatherSearcher类，和API函数，将返回结构字典化，方便和前端进行交互
