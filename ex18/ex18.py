# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("I got nothin'.")

print_two("Jackson", "Baker")
print_two_again("Jackson", "Baker")
print_one("First!")
print_none()