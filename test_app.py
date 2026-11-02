from app import is_valid_port

def test_normal_port_is_valid():
    assert is_valid_port(8080)

def test_low_port_is_invalid():
    assert not is_valid_port(80)

def test_high_port_is_invalid():
    assert not is_valid_port(70000)

def test_min_port_is_valid():
    assert is_valid_port(1024)

def test_max_port_is_valid():
    assert is_valid_port(65535)

def test_none_is_invalid():
    assert not is_valid_port(None)

def test_string_port_is_invalid():
    assert not is_valid_port("8080")
