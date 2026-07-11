from string_utils import StringUtils

string_utils = StringUtils()


# Тесты метода capitalize()


def test_capitalize_positive():
    result = string_utils.capitalize("skypro")
    assert result == "Skypro"


def test_capitalize_empty_string():
    result = string_utils.capitalize("")
    assert result == ""


def test_capitalize_already_uppercase():
    result = string_utils.capitalize("Skypro")
    assert result == "Skypro"


# Тесты метода trim()


def test_trim_positive():
    result = string_utils.trim("   skypro")
    assert result == "skypro"


def test_trim_without_spaces():
    result = string_utils.trim("skypro")
    assert result == "skypro"


def test_trim_only_spaces():
    result = string_utils.trim("   ")
    assert result == ""


# Тесты метода contains()


def test_contains_symbol_exists():
    result = string_utils.contains("SkyPro", "S")
    assert result is True


def test_contains_symbol_not_exists():
    result = string_utils.contains("SkyPro", "U")
    assert result is False


def test_contains_word():
    result = string_utils.contains("SkyPro", "Pro")
    assert result is True


# Тесты метода delete_symbol()


def test_delete_symbol_positive():
    result = string_utils.delete_symbol("SkyPro", "k")
    assert result == "SyPro"


def test_delete_substring():
    result = string_utils.delete_symbol("SkyPro", "Pro")
    assert result == "Sky"


def test_delete_symbol_not_exists():
    result = string_utils.delete_symbol("SkyPro", "A")
    assert result == "SkyPro"
