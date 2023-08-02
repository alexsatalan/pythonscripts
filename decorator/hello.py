# my_list = ['a', 'b', 'b', 'n', 'n']

# duplicates = list(set([x for x in my_list if my_list.count(x) > 1]))

# print(duplicates)

# Decorator


# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('*********')
#         func(*args, **kwargs)
#         print('*********')
#     return wrap_func


# @my_decorator
# def hello(greeting, emoji=':('):
#     print(greeting, emoji)


# # @my_decorator
# # def bye():
# #     print('see ya later')


# hello('hiiiii')

# from time import time


# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper


# @performance
# def long_time():
#     for i in range(10000000000):
#         i*5


# long_time()


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid'] is True:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
