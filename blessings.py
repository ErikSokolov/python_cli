from blessings import Terminal

t = terminal

with t.loaction(0, 0):
    print(t.bold(t.red('Hello, World!')))

with t.hidden_curser():
    print(t.bold(t.green('This is a hidden cursor.')))


