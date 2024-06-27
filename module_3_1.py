calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(a):
    b = len(a)
    c = a.upper()
    d = a.lower()
    calls = count_calls()
    return (b, c, d)


def is_contains(string, list_to_search):
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower() or string.upper() == list_to_search[i].upper():
            calls = count_calls()
            return True
    else:
        calls = count_calls()
        return False


print(string_info('Armstrong'))
print(string_info('Armmageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
