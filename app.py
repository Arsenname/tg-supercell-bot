from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>Купить Brawl Pass</title></head>
<body>
    <h1>Купить Brawl Pass</h1>
    <form method="POST" action="/buy">
        <button name="pass" value="brawl_plus">Brawl Pass Plus — 829₽</button><br><br>
        <button name="pass" value="brawl">Brawl Pass — 519₽</button><br><br>
        <button name="pass" value="pro_pass">Pro Pass — 1949₽</button>
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
    prices = {
        "Бравл Пасс Плюс": 829,
        "Бравл Пасс": 519,
        "Про Пасс": 1949
    }
    price = prices.get(chosen, "неизвестна")
    return f"Вы выбрали {chosen}, стоимость: {price}₽"

if __name__ == '__main__':
    app.run(port=5000)
