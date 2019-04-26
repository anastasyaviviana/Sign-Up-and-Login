from flask import Flask, send_from_directory, render_template, request, redirect, url_for
import json

with open('bikin_database.json') as dataku:
    data = json.load(dataku)

app = Flask(__name__, static_url_path='') # static url path utk akses folder images, karena selevel maka string kosong

# home route
@app.route('/')
def home():
    return '<h1>Welcome to my web server!</h1>'

# 404 route
@app.errorhandler(404)
def error404(error):
    return '<h1>Error: 404 Not Found</h1>' # bagusnya error itu berupa JSON

# route for render template html
@app.route('/login')
def login():
    return render_template('html.html')

@app.route('/signup')
def signup():
    return render_template('html2.html')

# POST route for signup
@app.route('/post_signup', methods = ['POST'])
def post_signup():
    # post dari html2.html pake request.form
    nam_s = request.form['nama_signup']
    pwd_s = request.form['pass_signup']
    data.append({'nama': nam_s, 'pass': pwd_s})
    y = json.dumps(data)

    json_data = open('bikin_database.json', 'w')
    json_data.write(y)
    return '<h1>Selamat ' + nam_s + ', Anda berhasil Register</h1>'


# POST route for login
@app.route('/post', methods = ['POST'])
def post_login():
    # post dari html.html pake request.form
    nam_l = request.form['nama_login']
    pwd_l = request.form['pass_login']
    i = 0
    # while i <= len(data):
    for i in range(len(data)):
        if nam_l == data[i]['nama'] and pwd_l == data[i]['pass']:
        # if nam_l == data['nama'] and pwd_l == data['password']:
            print('Nama:', nam_l, 'Password:', pwd_l)
            return redirect(url_for('sukses', nama = nam_l))
            # i += 1
        elif i == len(data) - 1:
            return '<h1>Nama dan Password Anda tidak terdaftar</h1>'
        else:
            # i += 1
            continue

    # def post manual
    # data = request.json
    # print('Anda nge-POST: ' + data['nama'] + (data['password']))
    # return 'Anda nge-POST: ' + data['nama'] + (data['password'])


# coba buat redirect route dengan dynamic route
@app.route('/sukses/<string:nama>')
def sukses(nama):
    return '<h1>Selamat Datang ' + nama + '</h1>'

# route for render static file => localhost:5000/file/helm.png
@app.route('/file/<path:gambar>') # => <tipe data:variable> tipe data path itu yang slash2 '/' di komputer kita
def statik(gambar):
    return send_from_directory('images', gambar) # images adalah folder

# if __name__ == '__main__':
#     app.run(debug = True)