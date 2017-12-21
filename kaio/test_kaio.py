import pytest

from .options import get_root_path


def test_root():
    assert get_root_path('/path1/path2/path3/') == '/'
    assert get_root_path('C:\\path1\\path2\\path3\\') == 'C:\\'
