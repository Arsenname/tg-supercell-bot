import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Покупка Brawl Pass</title>
</head>
<body>
    <h1>Купить Brawl Pass</h1>
    <form method="POST" action="/buy">
        <button name="pass" value="brawl_plus">Бравл Пасс Плюс — 829₽</button><br><br>
        <button name="pass" value="brawl">Бравл Пасс — 519₽</button><br><br>
        <button name="pass" value="pro_pass">Про Пасс — 1949₽</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/buy', methods=['POST'])
def buy():
    chosen = request.form.get('pass')
    return f"Вы выбрали {chosen}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
