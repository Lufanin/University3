calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    b = len(string), string.upper(), string.lower()
    return(b)
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower() or i in string.lower():
            return True
        if string.lower() not in i.lower() or i not in string.lower():
            return False


print(string_info('Armstrong'))
print(string_info('Armmageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
