# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


# def authenticated(fn):
#     def wrapper(dict):
#         if dict["valid"] == True:
#             return fn(dict)
#         else:
#             print('User is not authenticated, message has not been sent!')
#     return wrapper

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print('User is not authenticated, message has not been sent!')
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


# a = authenticated(message_friends)
# print(a(user1))

message_friends(user1)
