from flask import render_template
from app import app
from models.order import *
from models.book_orders import *

@app.route("/")

@app.route("/orders")
def index():
    return render_template("index.html", orders = orders)

@app.route("/orders/<index>")
def show_task_index(index):
    return render_template("order.html", order = orders[int(index)-1])