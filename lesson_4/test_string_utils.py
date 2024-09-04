import pytest
from string_utils import StringUtils

# Инициализация экземпляра класса
string_utils = StringUtils()

# Позитивные тесты для метода capitalize 
@pytest.mark.positive
def test_capitalize_positive():
    assert string_utils.capitalize("skypro") == "Skypro"

# Негативные тесты для метода capitalize
@pytest.mark.negative
def test_capitalize_negative_empty_string():
    assert string_utils.capitalize("") == ""

@pytest.mark.negative
def test_capitalize_negative_already_capitalized():
    assert string_utils.capitalize("Skypro") == "Skypro"

# Позитивные тесты для метода trim
@pytest.mark.positive
def test_trim_positive():
    assert string_utils.trim("   skypro") == "skypro"

# Негативные тесты для метода trim
@pytest.mark.negative
def test_trim_negative_empty_string():
    assert string_utils.trim("") == ""

# Позитивные тесты для метода to_list
@pytest.mark.positive
def test_to_list_positive():
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]

# Негативные тесты для метода to_list
@pytest.mark.negative
def test_to_list_negative_empty_string():
    assert string_utils.to_list("") == []

# Позитивные тесты для метода contains
@pytest.mark.positive
def test_contains_positive():
    assert string_utils.contains("SkyPro", "S")

# Негативные тесты для метода contains
@pytest.mark.negative
def test_contains_negative():
    assert not string_utils.contains("SkyPro", "U")

# Позитивные тесты для метода delete_symbol
@pytest.mark.positive
def test_delete_symbol_positive():
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"

# Негативные тесты для метода delete_symbol
@pytest.mark.negative
def test_delete_symbol_negative():
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"

# Позитивные тесты для метода starts_with
@pytest.mark.positive
def test_starts_with_positive():
    assert string_utils.starts_with("SkyPro", "S")

# Негативные тесты для метода starts_with
@pytest.mark.negative
def test_starts_with_negative():
    assert not string_utils.starts_with("SkyPro", "P")

# Позитивные тесты для метода ends_with
@pytest.mark.positive
def test_ends_with_positive():
    assert string_utils.ends_with("SkyPro", "o")

# Негативные тесты для метода ends_with
@pytest.mark.negative
def test_ends_with_negative():
    assert not string_utils.ends_with("SkyPro", "y")

# Позитивные тесты для метода is_empty
@pytest.mark.positive
def test_is_empty_positive():
    assert string_utils.is_empty("")

# Негативные тесты для метода is_empty
@pytest.mark.negative
def test_is_empty_negative():
    assert not string_utils.is_empty("SkyPro")

# Позитивные тесты для метода list_to_string
@pytest.mark.positive
def test_list_to_string_positive():
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"

# Негативные тесты для метода list_to_string
@pytest.mark.negative
def test_list_to_string_negative_empty_list():
    assert string_utils.list_to_string([]) == ""
