from flask import render_template
from flask import Blueprint

# 第一個引數為藍圖名稱 第二個引數為該藍圖所在模塊
app_v01 = Blueprint('v01', __name__, static_folder='appweb/static')


@app_v01.route("/")
def index():
    return render_template('v01/lo.html')
