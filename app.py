from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()
while True:
        print("\nChoose an operation:")
        print("1. Create an author")
        print("2. Read an author")
        print("3. List of authors")
        print("4. Update an author")
        print("5. Delete an author")
        print("6. Create a magazine")
        print("7. Read a magazine")
        print("8. List of magazines")
        print("9. Update a magazine")
        print("10. Delete a magazine")
        print("11. Create an article")
        print("12. Read an article")
        print("13. List of articles")
        print("14. Update an article")
        print("15. Delete an article")
        print("16. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            author_name = input("Enter author's name: ")
            author_id = Author.create(author_name)
            print(f"Author created with ID: {author_id}")

        elif choice == "2":
            author_id = int(input("Enter the author ID: "))
            author = Author.read(author_id)
            if author:
                print(author)
            else:
                print("Author not found")

        elif choice == "3":
            authors = Author.list_all()
            print("List of authors:")
            for author in authors:
                print(author)

        elif choice == "4":
            author_id = int(input("Enter the author ID: "))
            new_author_name = input("Enter the new author's name: ")
            Author.update(author_id, new_author_name)
            print("Author updated")

        elif choice == "5":
            author_id = int(input("Enter the author ID: "))
            Author.delete(author_id)
            print("Author deleted")

        elif choice == "6":
            magazine_name = input("Enter magazine's name: ")
            magazine_id = Magazine.create(magazine_name)
            print(f"Magazine created with ID: {magazine_id}")

        elif choice == "7":
            magazine_id = int(input("Enter the magazine ID: "))
            magazine = Magazine.read(magazine_id)
            if magazine:
                print(magazine)
            else:
                print("Magazine not found")

        elif choice == "8":
            magazines = Magazine.list_all()
            print("List of magazines:")
            for magazine in magazines:
                print(magazine)

        elif choice == "9":
            magazine_id = int(input("Enter the magazine ID: "))
            new_magazine_name = input("Enter the new magazine's name: ")
            Magazine.update(magazine_id, new_magazine_name)
            print("Magazine updated")

        elif choice == "10":
            magazine_id = int(input("Enter the magazine ID: "))
            Magazine.delete(magazine_id)
            print("Magazine deleted")

        elif choice == "11":
            title = input("Enter article title: ")
            content = input("Enter article content: ")
            author_id = int(input("Enter author ID: "))
            magazine_id = int(input("Enter magazine ID: "))
            article_id = Article.create(title, content, author_id, magazine_id)
            print(f"Article created with ID: {article_id}")


        elif choice == "12":
            article_id = int(input("Enter the article ID: "))
            article = Article.read(article_id)
            if article:
                print(f"Article ID: {article.id}")
                print(f"Title: {article.title}")
                print(f"Content: {article.content}")
                print(f"Author: {article.author_name}")
            else:
                print("Article not found")

        elif choice == "13":
            articles = Article.list_all()
            print("List of articles:")
            for article in articles:
                print(f"Article ID: {article.id}")
                print(f"Title: {article.title}")
                print(f"Content: {article.content}")
                print(f"Author: {article.author_name}")
                print(f"Magazine: {article.magazine_name}")
                print("--------------------")

        elif choice == "14":
            article_id = int(input("Enter the article ID: "))
            new_title = input("Enter the new article title: ")
            new_content = input("Enter the new article content: ")
            new_author_id = int(input("Enter the new author ID: "))
            new_magazine_id = int(input("Enter the new magazine ID: "))
            Article.update(article_id, new_title, new_content, new_author_id, new_magazine_id)
            print("Article updated")

        elif choice == "15":
            article_id = int(input("Enter the article ID: "))
            Article.delete(article_id)
            print("Article deleted")

        elif choice == "16":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()