def task1():
    print("\t\t\t\t\tTask 1")

    def read_and_display_text_file(file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    print(line.strip())
        except:
            print("Файл не найден")

    file_path = 'text1.txt'
    read_and_display_text_file(file_path)
