from flask import Flask, send_from_directory, render_template, request, redirect, url_for
app = Flask(__name__, static_url_path='') # static url path utk akses folder images, karena selevel maka string kosong

data = {
    'nama' : 'Andi',
    'password' : '12345'
}

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

# @app.route('/signup')
# def signup():
#     return render_template('html2.html')

# POST route
@app.route('/post', methods = ['POST'])
def post():
    # post dari html.html pake request.form
    nam = request.form['nama']
    pwd = request.form['pass']
    if nam == data['nama'] and pwd == data['password']:
        print('Nama:', nam, 'Password:', pwd)
        return redirect(url_for('sukses', nama = nam))
    else:
        return '<h1>Nama dan Password Anda tidak terdaftar</h1>'

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