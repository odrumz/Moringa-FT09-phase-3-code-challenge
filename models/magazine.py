from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
       
        return f'<Magazine {self.name}>'

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
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = category

    @classmethod
    def create(cls, name, category):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?,?)", (name, category))
        conn.commit()
        return cursor.lastrowid

    @classmethod
    def read(cls, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id =?", (magazine_id,))
        row = cursor.fetchone()
        if row:
            return cls(row[0], row[1], row[2])
        else:
            return None

    @classmethod
    def list_all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        rows = cursor.fetchall()
        magazines = []
        for row in rows:
            magazines.append(cls(row[0], row[1], row[2]))
        return magazines

    @classmethod
    def update(cls, magazine_id, name, category):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE magazines SET name =?, category =? WHERE id =?", (name, category, magazine_id))
        conn.commit()

    @classmethod
    def delete(cls, magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM magazines WHERE id =?", (magazine_id,))
        conn.commit()
