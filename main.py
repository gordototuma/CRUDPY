
clients = 'Luis, Alejandro, '

def create_client(client_name):
    global clients

    if client_name.lower() is not clients.lower():
        clients += client_name
        _add_comma()
    else:
        print('Client alredy is in the client\'s list')



def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients +=', '

def _print_welcome():
    print('WELCOME APP COMERCE')
    print('*'*18)
    print('What would you like to do today?')
    print('[C] create client')
    print('[U] Delete client')

if __name__ == "__main__":
    _print_welcome()
    
    command = input()

    if command in "cC":

        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    else:
        print('Invalid Command')

