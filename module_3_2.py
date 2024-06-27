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