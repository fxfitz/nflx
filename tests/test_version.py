import nflx.version


def test_version_defined():
    assert getattr(nflx.version, '__version__', None)
