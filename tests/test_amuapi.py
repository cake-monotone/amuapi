import os

import pytest


def test_check_environ():
    """
    SECRET_KEY 체킹
    """
    os.environ.clear()

    with pytest.raises(RuntimeError) as error:
        from amuapi import app
    assert "SECRET_KEY" in str(error.value)

