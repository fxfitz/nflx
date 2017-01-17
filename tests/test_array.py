import pytest

import nflx.arrays


@pytest.mark.parametrize('current,target,expected', [
    ([1, 3, 5, 6, 8, 9], [1, 2, 5, 7, 9], ([2, 7], [3, 6, 8]))
])
def test_array_diff(current, target, expected):
    assert nflx.arrays.diff(current, target) == expected
