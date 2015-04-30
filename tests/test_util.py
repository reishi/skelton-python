import reishi.util

def test_hello():
    assert reishi.util.hello() == 'Hello, world!'
    assert reishi.util.hello('Python') == 'Hello, Python!'
