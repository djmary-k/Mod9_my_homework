# Завдання
# Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, і відповідати відповідно до введеної команди.

CONTACTS = {'Mary': '123', 'Gary': '543'}

# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо. Декоратор input_error повинен обробляти винятки, що виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
def input_error(wrap):
    def inner(*args):
        try:
            return wrap(*args)
        except IndexError:
            return 'Give me name and phone please'
        except KeyError:
            return 'Invalid user name. Please, try again.'
        except ValueError:
            return 'Invalid phone number. Please, try again.'        
    return inner

# Функції обробники команд — набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
def hello_handler(*args):
    return 'How can I help you?'

def exit_handler(*args):
    return 'Good bye!'

@input_error
def add_handler(data):
    name = data[0].title()
    phone = int(data[1])
    CONTACTS[name] = phone
    return f'Contact {name} with phone number: {phone} has been saved.'

@input_error
def change_handler(data):
    name = data[0].title()
    phone = int(data[1])
    CONTACTS.pop(name)
    CONTACTS[name] = phone
    return f'Contact {name} with phone number: {phone} has been changed.'

@input_error
def phone_handler(data):
    name = data[0].title()
    return CONTACTS[name]

def show_all_handler(*args):
    for name, phone in CONTACTS.items():
        print(f'{name} {phone}')    
    return 'These are your contacts in the phonebook.'


COMMANDS = {
    hello_handler: ['hello', 'hello!', 'hi', 'hi!'],
    exit_handler: ['bye', 'good bye', 'close', 'exit', 'quit'],
    add_handler: ['add', 'adding', '+'],
    change_handler: ['change'],
    phone_handler: ['phone'],
    show_all_handler: ['show all'],    
}

# Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
def command_parser(raw_str: str):
    elements = raw_str.split()
    for key, value in COMMANDS.items():
        if raw_str.lower() in value:
            return key(elements[1:])
        elif elements[0].lower() in value:
            return key(elements[1:])
    return 'Invalid command. Please, try again.'

# Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції-handlerа.
def main():
    print('Hello!')
    while True:        
        user_input = input('>>> ')
        if not user_input:
            continue                
        result = command_parser(user_input)        
        print(result)
        if result == 'Good bye!':
            break


if __name__ == '__main__':
    main()

