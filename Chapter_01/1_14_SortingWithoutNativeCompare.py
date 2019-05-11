from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


if __name__ == '__main__':
    users = [User(23), User(3), User(99)]

    print(users)

    sorted_users_lambda = sorted(users, key=lambda u: u.user_id)
    print(sorted_users_lambda)

    sorted_users_attr = sorted(users, key=attrgetter('user_id'))
    print(sorted_users_attr)