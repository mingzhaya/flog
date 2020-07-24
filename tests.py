from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='Test')
        u.set_password('testtest')
        self.assertFalse(u.check_password('test'))
        self.assertTrue(u.check_password('testtest'))

    def test_follow(self):
        u1 = User(username='T1', email='t1@test.com')
        u2 = User(username='T2', email='t2@test.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u2.followed.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'T2')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'T1')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        u1 = User(username='T1', email='t1@test.com')
        u2 = User(username='T2', email='t2@test.com')
        u3 = User(username='T3', email='t3@test.com')
        db.session.add_all([u1, u2, u3])
        
        now = datetime.utcnow()
        p1 = Post(body='t1 post', author=u1, timestamp=now+timedelta(seconds=1))
        p2 = Post(body='t2 post', author=u2, timestamp=now+timedelta(seconds=4))
        p3 = Post(body='t3 post', author=u3, timestamp=now+timedelta(seconds=2))
        db.session.add_all([p1, p2, p3])
        db.session.commit()

        u1.follow(u2)
        u1.follow(u3)
        u2.follow(u3)
        db.session.commit()

        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        self.assertEqual(f1, [p2, p3, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3])

if __name__ == '__main__':
    unittest.main(verbosity=2)
