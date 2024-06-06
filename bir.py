import os
import concurrent.futures

def count_occurrences(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
        count = contents.count('unli') # 'unli' so'zining necha marta takrorlanganligini hisoblash
        return count

def process_file(file):
    file_name = "path/to/your/directory/" + file
    occurrences = count_occurrences(file_name)
    print(f"{file}: {occurrences} martta 'unli' so'zi qaytgan")

if __name__ == '__main__':
    directory_path = "path/to/your/directory/"
    files = [file for file in os.listdir(directory_path) if file.endswith('.txt')]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_file, files)
