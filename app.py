from flask import Flask, render_template, url_for
from data import Articles

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', title='Home')


@app.route('/articles')
def articles():

    list_articles = Articles()
    return render_template('articles.html', title='Articles', articles=list_articles.get_articles())


@app.route('/article/<int:article_id>')
def article(article_id):
    list_articles = Articles()
    return render_template('article.html', title='Article', article=list_articles.get_article(article_id))


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run('localhost', 8081, debug=True)
