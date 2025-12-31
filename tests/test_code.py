from utils.code import up_first

def test_up_first():
    assert up_first('skypro') == 'Skypro'

def test_up_first_for_empty():
    assert up_first('') == ''
