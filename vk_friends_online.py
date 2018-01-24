import vk
import getpass


APP_ID = 6343329


def get_user_login():
    return input('Enter vk login: ')


def get_user_password():
    return getpass.getpass('Enter vk password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_ids = api.friends.getOnline()
    friends_full_name = api.users.get(
        user_ids=friends_ids,
        fields='first_name, last_name'
    )
    return friends_full_name


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print ('\t\t{} {}'.format(friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    try:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(login, password)
        print ('\nVk friends online:')
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print ('Incorrect login or password. Try again.')
