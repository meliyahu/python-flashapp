class Articles:

    def __init__(self):
        self.articles = [
            {
                'id': 1,
                'title': 'Article One',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur autem, eligendi',
                'author': 'Mosheh EliYahu',
                'create_date': '12-01-2019'
            }, {
                'id': 2,
                'title': 'Article Two',
                'body': 'et expedita explicabo facilis id, inventore nemo nostrum officiis sunt vero vitae',
                'author': 'Caleb EliYahu',
                'create_date': '14-01-2019'
            }, {
                'id': 3,
                'title': 'Article Three',
                'body': 'voluptas? Alias beatae culpa quod vitae voluptate',
                'author': 'Tovia ben Yoseph',
                'create_date': '12-01-2018'
            }
            ]

    def get_articles(self):
        return self.articles

    def get_article(self, article_id):
        for article in self.articles:
            if article['id'] == article_id:
                return article
        return f'No article with id {article_id} was found!'



