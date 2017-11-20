import redis


client = redis.Redis(host='localhost', port=6379, db=0)


idea_dict = dict(
    idea_id='1',
    title='Make figure',
    description='Making figures by paper',
    rating=3.0,
    votes=1,
    email='xxx@gmail.com',
    author='Daniel'
)

client.hmset('1', idea_dict)


print(client.hmget('1', [
    'idea_id', 'title', 'description', 'rating', 'votes', 'email', 'author'
]))
