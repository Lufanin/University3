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


def send_email(recipient, sender='university.help@gmail.com'):
    if '@' not in sender or not sender.endswith(("com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>.")
    elif '@' not in sender or not sender.endswith(("com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")

send_email(recipient= 'orion.pax37@gmail.com')
send_email(recipient='university.help@gmail.com')
send_email(recipient='university.gmail.com')
send_email(recipient='university.gmail')
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
