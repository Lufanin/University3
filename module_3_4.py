def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower().count(root_word.lower()) == 1 or root_word.lower().count(i.lower()) == 1:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
calls = 0# я уже выполнял это задание, вместе с ним отправляю задание которым его заменили
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    b =(len(string), string.upper(), string.lower())
    calls = count_calls()
    return (b)
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