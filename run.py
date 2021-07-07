from fast_food import app

if __name__ == '__main__':
    app.secret_key = 'choco'
    app.run(debug=True)