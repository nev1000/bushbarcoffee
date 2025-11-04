from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO
import qrcode
import io


orders = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/qr")
def qr():
    url = "http://localhost:5000/"

    qr_img = qrcode.make(url)

    buf = io.BytesIO()
    qr_img.save(buf, format='PNG')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')
    

@app.route("/submit-order", methods=['POST'])
def submit():
    if request.method == "POST":
        memnum = request.form.get("memnum")
        type = request.form.get("coffee")
        size = request.form.get("size")
        milk = request.form.get("milk")
        notes = request.form.get("notes")
        order = {"memnum": memnum, "type": type, "size": size, "milk": milk, "notes": notes}
        socketio.emit("new order", order, to=None)

    return render_template("thanks.html", order=order)


@app.route("/orders")
def orders():
    return render_template("orders.html")

if __name__ == "__main__":
    socketio.run(app)

