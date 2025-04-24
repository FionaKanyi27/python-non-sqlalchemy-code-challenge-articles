class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters.")
        if hasattr(self, 'title'):
            raise Exception("Title cannot be changed")
        self._title = title
        Article.all_articles.append(self)

        @property
        def title(self):
            return self._title
        
        @property
        def author(self):
            return self._author
        
        @author.setter
        def author(self, value):
            if not isinstance(value, Author):
                raise Exception("Author must be an instance of Author class.")
            self._author = value

        @property
        def magazine(self):
            return self._magazine
        
        @magazine.setter
        def magazine(self, value):
            if not isinstance(value, Magazine):
                raise Exception("Magazine must be an instance of Magazine class.")
            self._magazine = value
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.name = name
        self._articles = []

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self.name = name
        self.category = category
        self._articles = []

        Magazine.all_magazines.append(self)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return {article.title for article in self._articles}

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        author_counts = {author: authors.count(author) for author in set(authors)}
        return {author for author, count in author_counts.items() if count > 2}
    
    @classmethod
    def top_publishers(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda magazine: len(magazine.articles))