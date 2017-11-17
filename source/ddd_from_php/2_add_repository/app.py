"""

Пример из 90-х

"""

import sqlite3


class Idea:
    def __init__(self):
        self.idea_id = None
        self.title = None
        self.description = None
        self.rating = None
        self.votes = None
        self.email = None

    def add_rating(self, rating):
        self.rating += int(rating)


class IdeaController:

    def __init__(self, request, idea_repository):
        self.request = request
        self.idea_repository = idea_repository

    def rate_action(self):
        idea_id = self.request.get('id')
        new_rating = self.request.get('rating')

        # find idea
        idea = self.idea_repository.find_by_id(idea_id)
        if not idea:
            raise ValueError('Idea does not exist')

        # add user rating
        idea.add_rating(new_rating)

        # save rating to repository
        self.idea_repository.update(idea)


class IdeaRepository:

    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def find_by_id(self, idea_id):
        # finding the idea in the database
        sql = 'SELECT * from Ideas where IdeaId = ?'
        row = self.cursor.execute(sql, idea_id).fetchone()
        if not row:
            raise ValueError('Idea does not exist')

        # Building the Idea from database
        idea_id, title, description, rating, votes, email = row
        idea = Idea()
        idea.idea_id = idea_id
        idea.title = title
        idea.description = description
        idea.rating = rating
        idea.votes = votes
        idea.email = email

        return idea

    def update(self, idea):
        update_statement = "UPDATE Ideas SET Rating='{}' WHERE IdeaId='{}'"
        self.cursor.execute(update_statement.format(idea.rating, idea.idea_id))
        self.connection.commit()


if __name__ == '__main__':
    request = {
        'id': '1',
        'rating': 100
    }

    repository = IdeaRepository('../db.sqlite3')
    controller = IdeaController(request, repository)

    controller.rate_action()
