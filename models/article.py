from database.connection import get_db_connection


class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
    def __init__(self, id, title, content, author_id, magazine_id, author_name=None, magazine_name=None):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id
        self._author_name = author_name
        self._magazine_name = magazine_name

    def __repr__(self):
        return f'<Article {self.title}>'
       

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if not isinstance(content, str):
            raise TypeError("Content must be a string")
        if len(content) < 10 or len(content) > 1000:
            raise ValueError("Content must be between 10 and 1000 characters")
        self._content = content

    @property
    def author_id(self):
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        if not isinstance(author_id, int):
            raise TypeError("Author ID must be an integer")
        self._author_id = author_id

    @property
    def magazine_id(self):
        return self._magazine_id

    @magazine_id.setter
    def magazine_id(self, magazine_id):
        if not isinstance(magazine_id, int):
            raise TypeError("Magazine ID must be an integer")
        self._magazine_id = magazine_id

    @classmethod
    def create(cls, title, content, author_id, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?,?,?,?)
        ''', (title, content, author_id, magazine_id))
        conn.commit()
        return cursor.lastrowid

    #I implemented the method of showing the author and the magazine in the read and list_all function
    @classmethod
    def read(cls, article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT articles.*, authors.name AS author_name, magazines.name AS magazine_name
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE articles.id =?
        ''', (article_id,))
        article_data = cursor.fetchone()
        if article_data:
            return cls(article_data["id"], article_data["title"], article_data["content"],
                    article_data["author_id"], article_data["magazine_id"],
                    author_name=article_data["author_name"],
                    magazine_name=article_data["magazine_name"])
        else:
            return None

    @classmethod
    def list_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT articles.*, authors.name AS author_name, magazines.name AS magazine_name
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            JOIN magazines ON articles.magazine_id = magazines.id
        ''')
        articles_data = cursor.fetchall()
        articles = []
        for article_data in articles_data:
            articles.append(cls(article_data["id"], article_data["title"], article_data["content"],
                            article_data["author_id"], article_data["magazine_id"],
                            author_name=article_data["author_name"],
                            magazine_name=article_data["magazine_name"]))
        return articles

    @classmethod
    def update(cls, article_id, title, content, author_id, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE articles
            SET title =?, content =?, author_id =?, magazine_id =?
            WHERE id =?
        ''', (title, content, author_id, magazine_id, article_id))
        conn.commit()

    @classmethod
    def delete(cls, article_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM articles WHERE id =?', (article_id,))
        conn.commit()

    @property
    def author_name(self):
        return self._author_name

    @property
    def magazine_name(self):
        return self._magazine_name