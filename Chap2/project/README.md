## 未来计划
1. 封装API，可以实现API的自由切换
 - [国外API：OpenWeatherMap](http://openweathermap.org/api)
 - [国内API：心知天气](https://www.seniverse.com/api)



# 基础任务程序说明
## 环境要求
Python 3.6.0

## 编译和安装
本程序为脚本程序。
## 特点
实时查询天气。

## 功能介绍
本程序为命令行形式的天气查询系统。功能要求如下:

- 输入城市名，获取该城市的天气情况
- 输入指令help，获取帮助信息
- 输入指令history，获取历史查询信息
- 输入指令quit，退出程序
- 程序会自动去除输入文字间的空格字符


## 结构：
- WeatherSearcher类，存储查询历史和天气数据库，提供相关的信息查询接口
- 基于给定的上面的四个要求完成和WeatherSearcher的交互

## Change Log
- 2017-09-03: 修改weatherSearcher类，增加fetch_weather_by_XXX函数，将天气查找类和API的关系松耦合化。
