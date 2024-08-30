import os 

def create_file(filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Hello")
    print(f"File {filename} created successfully")


def remove_file(filename: str) -> None:
    os.remove(filename)
    print(f"File '{filename}' was removed successfully")


if __name__ == '__main__':
    filename = "delete_me.txt"
    #create_file(filename)
    remove_file(filename)