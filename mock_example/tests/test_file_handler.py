import os 
from mock_example.file_handler import create_file, remove_file

def test_create_file():
    create_file('delete_me.txt')
    assert os.path.exists('delete_me.txt')


def test_remove_file():
    create_file('delete_me.txt')
    remove_file('delete_me.txt')
    assert not os.path.exists('delete_me.txt')


def test_create_file_with_mock(mocker):
    filename = 'mock_delete_me.txt'
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)
    create_file(filename)
    
    mock_file.assert_called_once_with(filename, 'w', encoding='utf-8')
    # mock_file as a function 
    mock_file().write.assert_called_once_with('Hello')


def test_remove_file_with_mock(mocker):
    filename = 'mock_delete_me.txt'
    mock_remove = mocker.patch("os.remove")
    
    remove_file(filename)

    mock_remove.assert_called_once_with(filename)
    # isfile = path exists
    mocker.patch("os.path.isfile", return_value=False)

    assert not os.path.isfile(filename)