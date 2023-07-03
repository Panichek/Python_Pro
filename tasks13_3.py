'''
3. Створити клас команди який буде при викликанні виводити Hello World
завдання полягає в тому аби створити клас який буде працювати як функція,
яка при виконанні буде виводити до терміналу Hello World
'''


class HelloWorldCommand:
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.print_hello_world()


class ReceiverCommand:
    def print_hello_world(self):
        print("Hello World!")


receiver_command = ReceiverCommand()
hello_world_command = HelloWorldCommand(receiver_command)
hello_world_command.execute()
