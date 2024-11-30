from hexlet_pytest.example import reverse
from pathlib import Path

def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert reverse('') == ''

def read_file(file):
    full_file_name = Path(__file__).parent / 'fixtures' / file
    with open(full_file_name, encoding='utf8') as f:
        long_text = f.read()
    return long_text

def test_reverse_long_text():
    source_file_text = read_file('long_text.txt')
    actual_reversed_text = reverse(source_file_text)
    expected_reversed_text = read_file('expected.txt')
    assert actual_reversed_text == expected_reversed_text