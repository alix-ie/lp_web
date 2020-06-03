from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)


@app.route("/")
def index():
    page_title = 'News Python'
    weather = weather_by_city('Moscow', 'Russia')
    return render_template('index.html', page_title=page_title, weather=weather)


if __name__ == "__main__":
    app.run(debug=True)
