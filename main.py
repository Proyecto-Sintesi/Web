import os

from quart import Quart, render_template

app = Quart(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
async def home():
    services_path = "static/images/services"
    images = list()
    for service_image in os.listdir(services_path):
        images.append(f"{services_path}/{service_image}")

    return await render_template("index.html", images=images[::-1])


@app.route("/servicios")
async def servicios():
    return render_template("services.html")


if __name__ == "__main__":
    from constants import HOST, PORT

    app.run(host=HOST, port=PORT, debug=True)
