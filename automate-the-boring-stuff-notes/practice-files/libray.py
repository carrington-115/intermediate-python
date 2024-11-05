"""
This code is a simulation of the school lib in OOP with python
a library have the following tools
    - books
    - students
    - book shelfs
    - reading halls
    - reading desks
    - stairs
    - bag pack storage

    - *books*
        books have the following attributes
        * pages - a page is an class (number, segments, paragraphs, content)
        * cover - name of book, author
        * table of content - sections: each section has a topic (title, section number, page number)
        * content: full string
        * appendix: full string
        * author: person (class)
        books methods
        * open and go to a page
        * can display data on a page
        * return shelf number
        * 

    

"""
class Location:
    def __init__(self, city, street, zipcode, state, country):
        self.city = city
        self.street = street
        self.zipcode = zipcode
        self.state = state
        self.country = country

    def __str__(self):
        return {
            'city': self.city,
            "street": self.street,
            "zipcode": self.zipcode,
            "state": self.state, 
            "country": self.country
        }

# an author is a person
class Person:
    def __init__(self, name, place_of_birth, home_details, date_of_birth, gender, age, marital_status, email, phone_number):
        self.name = name
        self.place_of_birth = place_of_birth
        self.home_details = home_details
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.age = age
        self.marital_status = marital_status
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return {
            'name': self.name,
            "place_of_birth": self.place_of_birth,
            'home_details': self.home_details,
            'date_of_birth': self.date_of_birth,
            'gender': self.gender,
            'age': self.age,
            'marital status': self.marital_status,
            'email': self.email,
            'phone_number': self.phone_number
        }


class Page:
    def __init__(self, page_number, content, paragraphs, topic_segments):
        self.page_number = page_number # type: int
        self.content = content # type: str
        self.paragraphs = paragraphs  # type: int
        self.topic_segments = topic_segments # type: dict

    def __str__(self):
        return {
            "PageNumber": self.page_number,
            "content": self.content,
            "paragraphs": self.paragraphs,
            "topicSegments": self.topic_segments
        }
    
class Cover:
    def __init__(self, book_name, author_name, edition):
        self.book_name = book_name
        self.author_name = author_name
        self.edition = edition

    def __str__(self):
        return {
            "name": self.book_name,
            "author": self.author_name,
            'edition': self.edition
        }

class Book:
    def __init__(self, name, pages, table_of_content, content, shelf_number, cover, appendix, author):
        self.name = name
        self.pages = pages
        self.table_of_content = table_of_content
        self.content = content
        self.shelf_number = shelf_number
        self.cover = cover
        self.appendix = appendix
        self.author = author
