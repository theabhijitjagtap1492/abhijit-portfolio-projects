# Simple E-Commerce Platform (Flask)

A modern, user-friendly e-commerce web application built with Flask, Bootstrap, and pandas. Users can browse products, add them to a cart, place orders, and view their order history. Order data is stored in an Excel file for easy management.

## Features
- Browse products (Laptop, Mouse, Keyboard, Pendrive) with images and descriptions
- Add products to a shopping cart
- View and manage cart contents
- Place orders (saved to `orders.xlsx`)
- View order history in a modern, responsive table
- Delete items from cart
- Flash messages for user feedback
- Mobile-friendly, clean Bootstrap 5 UI


## Project Structure
```
Simple E-Commerce Platform/
├── app.py                  # Main Flask application
├── Requirements.txt        # Python dependencies
├── orders.xlsx             # Order data (auto-created)
├── static/
│   ├── Laptop.png
│   ├── Mouse.png
│   ├── Key.png
│   ├── Pendrive.png
│   └── style.css
└── templates/
    ├── home.html           # Home/product listing page
    ├── cart.html           # Cart and checkout page
    └── order_history.html  # Order history page
```

## Setup & Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/simple-ecommerce-flask.git
   cd simple-ecommerce-flask
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r Requirements.txt
   ```
4. **Run the application**
   ```bash
   python app.py
   ```
5. **Open your browser** and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage
- Browse products on the home page and add them to your cart.
- Click the cart icon to view or remove items.
- Click "Proceed to Checkout" to place your order.
- View your order history from the navigation bar.

## Dependencies
- Flask
- pandas
- openpyxl
- Bootstrap 5 (via CDN)

## Customization
- Add more products by editing the `PRODUCTS` list in `app.py` and adding images to `static/`.
- Change styles in `static/style.css` or the inline `<style>` blocks in templates.

## License
MIT License

---
**Suggested GitHub repo name:** `simple-ecommerce-flask` 
