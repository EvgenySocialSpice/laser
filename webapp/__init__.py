from flask import Flask, render_template, url_for


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
        return render_template('index.html', page_title=title)

    @app.route('/faq')
    def faq():
        title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
        return render_template('faq.html', page_title=title)

    @app.route('/promotions')
    def promotions():
        title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
        return render_template('promotions.html', page_title=title)

    @app.route('/blogs_tips')
    def blogs_tips():
        title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
        return render_template('blogs_tips.html', page_title=title)

    @app.route('/contact')
    def contact():
        title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
        return render_template('contact.html', page_title=title)

    @app.route('/prices')
    def prices():
        title = 'Beauty laser treatments and calorie burning bed sessions - to make you feel renewed'
        return render_template('prices.html', page_title=title)

    return app
