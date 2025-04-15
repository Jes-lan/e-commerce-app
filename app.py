from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Sample product data
PRODUCTS = [
    {'id': 1, 'name': 'Telefon', 'price': 1000},
    {'id': 2, 'name': 'Laptop', 'price': 5000}
]

@app.route('/')
def home():
    """Render the home page with the list of products."""
    return render_template('index.html', products=PRODUCTS)

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)