from typing import Literal
import pytest
from string_utils import StringUtils

utils = StringUtils()

# Проверки Capitalize
def test_capitalize():
    # Позитивные
    assert utils.capitalize("almet") == "Almet"
    assert utils.capitalize("седьмое августа") == "Седьмое августа"
    assert utils.capitalize("123") == "123"
    # Негативные
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("1almet") == "1almet"

# Проверки Trim
@pytest.mark.parametrize("line, result", [(" Almet", "Almet"),(" Positive", "Positive"),("My name", "My name")])
def test_trim(line: Literal[' Almet'] | Literal[' Positive'] | Literal['My name'], result: Literal['Almet'] | Literal['Positive'] | Literal['My name']):
    assert utils.trim(line) == result

@pytest.mark.xfail()
def test_trim_for_numbers():
    assert utils.trim(987654321) == "987654321"

# Проверки To_list
@pytest.mark.parametrize("string, delimeter, result", [
    # Позитивные
    ("Альметьевск,Казань,Челны", ",", ["Альметьевск", "Казань", "Челны"]),
    ("5;4;3;2;1", ";", ["5", "4", "3", "2", "1"]),
    ("!^@^+^%^&^*", "^", ["!", "@", "+", "%", "&", "*"]),
    # Негативные
    ("", None, []),
    ("5 4,3,2,1", None, ["5 4", "3", "2", "1"])])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

# Проверки Contains
@pytest.mark.parametrize("string, symbol, result", [
    ("Альметьевск", "А", True),
    (" kurs", "u", True),
    ("Казань", "ь", True),
    ("Анна-Мария", "-", True),
    ("128", "8", True),
    ("", "", True),
    ("Сатурн", "с", False),
    ("Hello", "k", False),
    ("барс", "%", False),
    ("", "s", False),
    ("54321", "ы", False),
    ("clip", "", False) # Система выдаёт True - запись в дефекты (defects.txt)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

# Проверки Delete_symbol
@pytest.mark.parametrize("string, symbol, result", [
    # Позитивные
    ("Альметьевск", "А", "льметьевск"),
    (" kurs", "u", " krs"),
    ("Казань", "ь", "Казан"),
    ("Анна-Мария", "-", "АннаМария"),
    ("128", "8", "12"),
    # Негативные
    ("", "", ""),
    ("Сатурн", "з", "Сатурн"),
    ("", "k", ""),
    ("барс", "", "барс"),
    ("рукав ", " ", "рукав")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

# Проверки Starts_with
@pytest.mark.parametrize("string, symbol, result", [
    # Позитивные
    ("Альметьевск", "А", True),
    (" kurs", " ", True),
    ("Казань", "К", True),
    ("Анна-Мария", "А", True),
    ("128", "1", True),
    ("", "", True),
    # Негативные
    ("Сатурн", "c", False),
    ("hello", "H", False),
    ("барс", "%", False),
    ("", "s", False),
    ("54321", "ы", False)
    ])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

# Проверки End_with
@pytest.mark.parametrize("string, symbol, result", [
    # Позитивные
    ("Альметьевск", "к", True),
    (" kurs", "s", True),
    ("Казань", "ь", True),
    ("Анна-Мария", "я", True),
    ("128", "8", True),
    ("", "", True),
    # Негативные
    ("Сатурн", "c", False),
    ("hello", "H", False),
    ("барс", "%", False),
    ("", "s", False),
    ("54321", "ы", False)
    ])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

# Проверки Is_empty
@pytest.mark.parametrize("string, result", [
    # Позитивные
    ("", True),
    (" ", True),
    ("  ", True),
    # Негативные
    ("Сатурн", False),
    (" hello", False),
    ("54321", False)
    ])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

# Проверки List_to_string
@pytest.mark.parametrize("lst, joiner, result", [
    # Позитивные
    (["Альметьевск", "Казань", "Челны"], ",", "Альметьевск,Казань,Челны"),
    (["5", "4", "3", "2", "1"], ";", "5;4;3;2;1"),
    (["Евпатий", "Коловратий"], "-", "Евпатий-Коловратий"),
    # Негативные
    ([], None, ""),
    ([], "@", ""),
    ([], "bug", "")])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result