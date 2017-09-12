from flask import Flask, session, redirect, url_for, escape, request
# from flask.ext.session import Session

app = Flask(__name__)
# sess = Session()
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# sess.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("at the very beginning:" + str(session))
    if request.method == 'POST':
        ip = request.remote_addr # 获取客户的IP地址，作为客户的唯一标识
        if "obj" not in session:
            print("分支1")
            session["ip"] = ip
            session["obj"] = []
            session['obj'].append(request.form['order'])
        elif ip != session["ip"] or session["obj"] is None: # 这种情况应该不会发生
            print("分支2")
            session["ip"] = ip
            session["obj"] = []
            session['obj'].append(request.form['order'])
        else:
            print("分支3")
            print(session["obj"])
            # 第二种方法
            # tmp = session['obj']
            # tmp.append(request.form['order'])
            # session["obj"] = tmp
            session["obj"].append(request.form['order'])

            print(id(session['obj']))
    return '''
        <form action="" method="post">
            <p><input type=text name=order>
            <p><input type=submit value=Login>
            <p>{obj}</p>
        </form>
    '''.format(obj=str(session["obj"] if "obj" in session else ""))


if __name__ == '__main__':
    app.debug = True
    app.run()
