from flask import render_template, jsonify
from flask import Blueprint

# 第一個引數為藍圖名稱 第二個引數為該藍圖所在模塊
app_v01 = Blueprint('v01', __name__, static_folder='appweb/static')


@app_v01.route("/")
def login():
    return render_template('v01/login.html')

@app_v01.route("/main")
def main():
    return render_template('v01/main.html')


# 帳號
@app_v01.route("/acount")
def acount():
    '''後台帳號頁面'''
    return


@app_v01.route("/api_acount")
def api_acount():
    '''後台帳號頁面'''
    return


@app_v01.route("/user")
def user():
    '''使用者帳號頁面'''
    return


@app_v01.route("/api_user")
def api_user():
    '''使用者帳號 API'''
    return


@app_v01.route('/api_account_verify')
def api_account_verify():
    pass


# 以下測試
@app_v01.route("/test", methods=['GET', 'POST'])
def test():
    return render_template('v01/test.html')


@app_v01.route("/api_test", methods=['GET', 'POST'])
def api_test():
    tut = []
    for i in range(0, 10):
        tut.append({'sid': i})
    res = {
        "page": 1,
        "total": 1,
        "records": 10,
        "rows": tut
    }
    return jsonify(res), 200
