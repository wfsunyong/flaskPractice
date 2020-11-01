from flask import Flask
from flask import render_template
from flask import request
# 创建应用程序
app = Flask(__name__)

# 设置路由
@app.route('/')
# 处理上述路由下web发送的请求，及当访问上述路由页面时，执行以下函数˙
def index():
    a = 'hahahaah'
    list1 = ['毛泽东', '江泽民', '习近平', '谁呢', "lalal"]
    return render_template('index.html', jay=a, list=list1)  # render_template自动加载templates文件夹中的index.html文件

@app.route('/second')
def second():
    return '第二个页面'

# 接收页面数据
# 登录页面
@app.route('/login1')
def login1():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # 接收用户名和密码
    username = request.form.get('username')
    password = request.form.get('pwd')
    if username == 'sunyong' and password == 'F920k001':
        return '登录成功'
    else:
        return render_template('login.html', msg='登录失败')


@app.route('/getProfile', methods=['GET', 'POST'])
def getProfile():
    if request.method == 'GET':
        name = request.args.get('name')
        print(name)
        return name
    elif request.method == 'POST':
        name1 = request.json.get('name')  # 获取post方式数据
        return name1



# 生成一个接口，支持get和post
@app.route('/api', methods=['GET', 'POST'])
def apiTest():
    if request.method == 'POST':
        name = request.json.get('name')
        return name
    elif request.method == 'GET':
        name = request.args.get('name')
        return name

# 启动应用
if __name__ == '__main__':
    app.run(port=8080, debug=True)

