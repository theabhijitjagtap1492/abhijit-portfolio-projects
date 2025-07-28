from flask import Flask, render_template, request, redirect, url_for, session, flash
import pandas as pd
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret'  # For session

PRODUCTS = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1500},
    {"name": "Pendrive", "price": 800}
]

@app.route("/")
def home():
    return render_template("home.html", products=PRODUCTS)

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_name = request.form.get("product_name")
    quantity = int(request.form.get("quantity", 1))
    
    cart = session.get("cart", [])
    cart.append({"product": product_name, "quantity": quantity})
    session["cart"] = cart
    flash(f"{quantity} {product_name}(s) added to cart!", "success")
    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    return render_template("cart.html", cart=session.get("cart", []))

@app.route("/checkout", methods=["POST"])
def checkout():
    cart = session.get("cart", [])
    if not cart:
        flash("Your cart is empty!", "warning")
        return redirect(url_for("cart"))

    try:
        df = pd.read_excel("orders.xlsx")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Order ID", "Product Name", "Quantity", "Order Date"])
    
    date = datetime.now().strftime("%Y-%m-%d")
    for item in cart:
        order_id = str(uuid.uuid4())[:8]  # Unique short ID for each product
        print(f"Adding order: {order_id}, {item['product']}, {item['quantity']}, {date}")  # DEBUG
        df.loc[len(df)] = [order_id, item["product"], item["quantity"], date]
    
    df.to_excel("orders.xlsx", index=False)
    print("Current orders after save:\n", df)  # DEBUG
    session["cart"] = []
    flash(f"Order(s) placed successfully!", "success")
    return redirect(url_for("orders"))

@app.route("/orders")
def orders():
    try:
        df = pd.read_excel("orders.xlsx")
        orders = df.to_dict(orient="records")
    except FileNotFoundError:
        orders = []
    return render_template("order_history.html", orders=orders)

@app.route("/delete_from_cart/<int:index>", methods=["POST"])
def delete_from_cart(index):
    cart = session.get("cart", [])
    if 0 <= index < len(cart):
        removed_item = cart.pop(index)
        session["cart"] = cart
        flash(f"{removed_item['product']} removed from cart!", "info")
    return redirect(url_for("cart"))

@app.route("/order_history")
def order_history():
    try:
        df = pd.read_excel("orders.xlsx")
        orders = df.to_dict(orient="records")
    except FileNotFoundError:
        orders = []
    return render_template("order_history.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True)