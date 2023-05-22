from src.main import DisplayDate
from datetime import datetime

def test_main():
    str_a = 'Sample String'
    str_b = 'Sample String'
    assert str_a == str_b

def test_display_current_timestamp():
    pass
    # expected_output = datetime.now()
    # returned_output = DisplayDate().display_current_timestamp()
    # assert returned_output.date == expected_output.date
