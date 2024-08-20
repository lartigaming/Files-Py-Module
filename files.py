# -*- coding: utf-8 -*-
from colorama import Fore, Style
import os

def getline(filename, line_number):
    """
    Читает определенную строку из текстового файла.

    Args:
        filename: Путь к файлу.
        line_number: Номер строки для чтения (начиная с 1).

    Returns:
        Строка текста, если строка найдена, иначе None.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i + 1 == line_number:
                    return line.strip()
        return None
    except FileNotFoundError:
        print(f"{Fore.RED} ❌ Файл \"{filename}\" не найден. ❌ {Style.RESET}")

def replaceline(filename, line_number, new_line):
    """
    Заменяет строку в текстовом файле на другую строку.

    Args:
        filename: Путь к файлу.
        line_number: Номер строки для замены (начиная с 1).
        new_line: Новая строка для замены.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_line + '\n'

        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    else:
        print(f"{Fore.RED} ❌ Номер строки {line_number} вне диапазона ❌ {Style.RESET}")

def addline(filename, new_line):
    """
    Добавляет строку в конец текстового файла.

    Args:
        filename: Путь к файлу.
        new_line: Строка для добавления.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(new_line + '\n')
        print(f"Строка '{new_line}' добавлена в файл '{filename}'")
    except FileNotFoundError:
        print(f"{Fore.RED} ❌ Файл не найден: {filename} ❌ {Style.RESET}")


def read_file(filename):
    """
    Читает весь файл и возвращает его содержимое в виде списка строк.

    Args:
        filename: Путь к файлу.

    Returns:
        Список строк, если файл найден, иначе None.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"{Fore.RED} ❌ Файл не найден: {filename} ❌ {Style.RESET}")
        return None
    

def write_lines(filename, lines):
    """
    Записывает список строк в файл.

    Args:
        filename: Путь к файлу.
        lines: Список строк для записи.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    except FileNotFoundError:
        print(f"{Fore.RED} ❌ Файл не найден: {filename} ❌ {Style.RESET}")

def count_lines(filename):
    """
    Подсчитывает количество строк в файле.

    Args:
        filename: Путь к файлу.

    Returns:
        Количество строк в файле, если файл найден, иначе 0.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except FileNotFoundError:
        print(f"{Fore.RED} ❌ Файл не найден: {filename} ❌ {Style.RESET}")
        return 0
    
def find_line(filename, search_string):
    """
    Ищет строку в файле и возвращает номер строки (начиная с 1) или None, если строка не найдена.

    Args:
        filename: Путь к файлу.
        search_string: Строка для поиска.

    Returns:
        Номер строки (начиная с 1), если строка найдена, иначе None.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if search_string in line:
                    return i + 1
        return None
    except FileNotFoundError:
        print(f"{Fore.RED} ❌ Файл не найден: {filename} ❌ {Style.RESET}")
        return None

def delete_file(filename):
    """
    Удаляет файл.

    Args:
        filename: Путь к файлу.
    """
    try:
        os.remove(filename)
        print(f"Файл '{filename}' удален.")
    except FileNotFoundError:
        print(f"{Fore.RED} ❌ Файл не найден: {filename} ❌ {Style.RESET}")
    except OSError as e:
        print(f"{Fore.RED} ❌ Ошибка при удалении файла: {e} ❌ {Style.RESET}")

def file_exists(filename):
    """
    Проверяет, существует ли файл.

    Args:
        filename: Путь к файлу.

    Returns:
        True, если файл существует, иначе False.
    """
    return os.path.exists(filename)