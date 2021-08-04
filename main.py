
clients = 'Luis, Alejandro, '

def create_client(client_name):
    global clients

    if client_name.lower() is not clients.lower():
        clients += client_name
        _add_comma()
    else:
        print('Client alredy is in the client\'s list')


def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, update_client_name)
    else:
        print('Client is not in clients lists')


def list_clients():
    global clients
    print(clients)


def delete_client(client_name):
    global clients
    if  client_name in clients:
        clients = clients.replace(client_name+",", "")
    else:
        print('Client is not in clients lists')


def search_client(client_name):
    global clients


    for client in clients.split(','):
        if client != client_name:
            continue
        else:
            return True

    """
    if client_name in clients:
        return True
    else:
        return False
    """

def _add_comma():
    global clients
    clients +=', '


def _get_client_name():
    return input('What is the client name? ')


def _print_welcome():
    print('WELCOME APP COMERCE')
    print('*'*18)
    print('What would you like to do today?')
    print('[C] create client')
    print('[L] List client')
    print('[D] Delete client')
    print('[U] Update client')
    print('[S] Search Client')


if __name__ == "__main__":
    _print_welcome()
    
    command = input().upper()

    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command  == "L":
        list_clients()
    elif command == "U":
        client_name = _get_client_name()
        update_client_name = input("What is the updated client name? ")
        update_client(client_name, update_client_name)
        list_clients()
    elif command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        print(found)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'ś list')
    else:
        print('Invalid Command')

