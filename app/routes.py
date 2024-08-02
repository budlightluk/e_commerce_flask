from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from app.models import Product, Order
from app.forms import CheckoutForm
import stripe

main = Blueprint('main', __name__)


@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@main.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)


@main.route('/cart')
def cart():
    # Placeholder for cart logic
    return render_template('cart.html')


@main.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    if form.validate_on_submit():
        # Process checkout here
        return redirect(url_for('main.index'))
    return render_template('checkout.html', form=form)


@main.route('/login')
def login():
    # Placeholder for login logic
    return render_template('login.html')


@main.route('/register')
def register():
    # Placeholder for registration logic
    return render_template('register.html')
