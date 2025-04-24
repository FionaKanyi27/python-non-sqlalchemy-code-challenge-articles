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
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass