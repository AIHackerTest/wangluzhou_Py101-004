from flask import Flask, jsonify, render_template, request, session
from weather_search import WeatherSearcher


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


# _add_numbers 和 函数名称  add_numbers是否有某种对应关系?答：无关系
@app.route('/_get_weather_info', methods=['GET', 'POST'])
def response():
    weather_searcher = WeatherSearcher()
    # print("method是" + request.method)
    if request.method == 'POST':
        if "history" in session:
            history = session["history"]
        else:
            history = []
        order = request.form['order']
        print(order)
        if order == "help":
            help_info = '''
                输入城市名，查询该城市的天气数据；
                点击[帮助]，获得帮助信息；
                点击[历史]，显示查询历史。
                '''
            result = {"help" : help_info}
        elif order == "history":
            result = {"history": history}
        else:
            city_to_search = order
            response_info = weather_searcher.get_weather([city_to_search])
            if response_info[city_to_search] is not None:
                print(response_info[city_to_search]) # for debug
                result = response_info[city_to_search]
                history.append(response_info[city_to_search])
                print(history)
            else:
                result = {"error" : """你要查找的城市没有找到，或者API异常，
                             请重新输入!可以点击[帮助]按钮查看帮助信息。"""}
        session["history"] = history
        return jsonify(result=result)


@app.route('/')
def index():
    session.clear()
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
