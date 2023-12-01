from flask import Flask, render_template
from ImageProcessing import IP

app = Flask(__name__)
app.config["SECRET_KEY"] = "nam1506"

app.register_blueprint(IP)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
