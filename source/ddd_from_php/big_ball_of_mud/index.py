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

    def __init__(self, request):
        self.request = request

    def rate_action(self):
        idea_id = self.request.get('id')
        new_rating = self.request.get('rating')

        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        # finding the idea in the database
        sql = 'SELECT * from Ideas where IdeaId = ?'
        row = c.execute(sql, '1').fetchone()
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

        # add user rating
        idea.add_rating(new_rating)

        update_statement = "UPDATE Ideas SET Rating='{}' WHERE IdeaId='{}'"
        c.execute(update_statement.format(idea.rating, idea.idea_id))
        conn.commit()


if __name__ == '__main__':
    request = {
        'id': '1',
        'rating': 3
    }

    controller = IdeaController(request)

    controller.rate_action()
