from database.connection import get_db_connection


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return f'<Author {self.name}>'

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name

    @classmethod
    def create(cls, name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        return cursor.lastrowid

    @classmethod
    def read(cls, author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id =?', (author_id,))
        author_data = cursor.fetchone()
        if author_data:
            return Author(author_data["id"], author_data["name"])
        else:
            return None

    @classmethod
    def list_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        authors_data = cursor.fetchall()
        authors = []
        for author_data in authors_data:
            authors.append(Author(author_data["id"], author_data["name"]))
        return authors

    @classmethod
    def update(cls, author_id, new_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE authors SET name =? WHERE id =?', (new_name, author_id))
        conn.commit()

    @classmethod
    def delete(cls, author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM authors WHERE id =?', (author_id,))
        conn.commit()

    @classmethod
    def articles(cls, author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT articles.*
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE authors.id =?
        ''', (author_id,))
        articles_data = cursor.fetchall()
        articles = []
        for article_data in articles_data:
            from article import Article
            articles.append(Article(article_data["id"], article_data["title"], article_data["content"]))
        return articles

    @classmethod
    def magazines(cls, author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT magazines.*
            FROM authors
            JOIN magazine_authors ON authors.id = magazine_authors.author_id
            JOIN magazines ON magazine_authors.magazine_id = magazines.id
            WHERE authors.id =?
        ''', (author_id,))
        magazines_data = cursor.fetchall()
        magazines = []
        for magazine_data in magazines_data:
            from magazine import Magazine
            magazines.append(Magazine(magazine_data["id"], magazine_data["title"], magazine_data["issue_number"]))
        return magazines