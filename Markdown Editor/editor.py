user_text = """"""


def menu():
    command = input("- Choose a formatter:")
    if command == '!help':
        print("""Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list
Special commands: !help !done""")
        command = input("- Choose a formatter:")
    elif command not in ['plain', 'bold', 'italic', 'header', 'inline-code', 'link', 'new-line', 'ordered-list', 'unordered-list']:
        print("Unknown formatting type or command")
        command = input("- Choose a formatter:")

    while command != "!done" and command in ['plain', 'bold', 'italic', 'header', 'inline-code', 'link', 'new-line', 'ordered-list', 'unordered-list']:

        if command == "plain":
            plain()
            command = input("- Choose a formatter:")
        elif command == "bold":
            bold()
            command = input("- Choose a formatter:")
        elif command == "new-line":
            new_line()
            command = input("- Choose a formatter:")
        elif command == "italic":
            italic()
            command = input("- Choose a formatter:")
        elif command == "header":
            header()
            command = input("- Choose a formatter:")
        elif command == "inline-code":
            inline()
            command = input("- Choose a formatter:")
        elif command == "link":
            link()
            command = input("- Choose a formatter:")
        elif command == "ordered-list":
            ordered_list()
            command = input("- Choose a formatter:")
        elif command == "unordered-list":
            unordered_list()
            command = input("- Choose a formatter:")
    if command == "!done":
            file = open("output.md", "w+", encoding='utf-8')
            file.write(user_text)


def plain():
    global user_text
    plain = input("Text:")
    user_text += f"{plain}"
    print(user_text)


def bold():
    global user_text
    bold = input("Text:")
    user_text += f"**{bold}**"
    print(user_text)


def new_line():
    global user_text
    user_text += f"\n"
    print(user_text)


def italic():
    global user_text
    italic = input("Text:")
    user_text += f"*{italic}*"
    print(user_text)


def header():
    global user_text
    level = int(input("Level:"))
    if 1 <= level <= 6:
        header = input("Text:")
        user_text += '#' * level + ' ' + f"{header}\n"
        print(user_text)
    else:
        print("The level should be within the range of 1 to 6")


def inline():
    global user_text
    code = input("Text:")
    user_text += f'`{code}`'
    print(user_text)


def link():
    global user_text
    label = input("Label:")
    url = input("URL:")
    user_text += f"[{label}]({url})"
    print(user_text)


def ordered_list():
    global user_text
    num_rows = int(input("Number of rows:"))
    while num_rows <= 0:
        print("The number of rows should be greater than zero")
        num_rows = int(input("Number of rows:"))
    else:
        for i in range(num_rows):
            row = input(f"Row #{i +1}:")
            user_text += f"{i +1}. {row}\n"
        print(user_text)


def unordered_list():
    global user_text
    num_rows = int(input("Number of rows:"))
    while num_rows <= 0:
        print("The number of rows should be greater than zero")
        num_rows = int(input("Number of rows:"))
    else:
        for i in range(num_rows):
            row = input(f"Row #{i +1}:")
            user_text += f"* {row}\n"
        print(user_text)


menu()
