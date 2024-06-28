calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    b =(len(string), string.upper(), string.lower())
    count_calls()
    return(b)
def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower() or list_to_search[i] in string.lower():
            return True
        else:
            return False


print(string_info('Armstrong'))
print(string_info('Armmageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
