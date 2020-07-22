from getpass import getpass

from web import create_app
from web.model import db, User

app = create_app()

with app.app_context():
    while True:
        username = input('Enter username: ')

        if User.query.filter(User.username == username).count():
            print('This username is already taken')
        else:
            break

    while True:
        password = getpass('Enter password: ')
        password2 = getpass('Confirm password: ')

        if password == password2:
            break
        else:
            print('The passwords are different')

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('User {} has been added'.format(new_user.id))
