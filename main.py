from quart import Quart, render_template

app = Quart(__name__)


@app.route("/")
async def home():
    return await render_template("index.html")


if __name__ == "__main__":
    app.run(port=25000, debug=True)
