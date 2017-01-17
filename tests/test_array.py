import pytest

import nflx.arrays


@pytest.mark.parametrize('current,target,expected', [
    ([1, 3, 5, 6, 8, 9], [1, 2, 5, 7, 9], ([2, 7], [3, 6, 8])),  # from sample
    ([], [1, 2, 3, 4, 5], ([1, 2, 3, 4, 5], [])),  # test only additions
    ([1, 2, 3, 4, 5], [], ([], [1, 2, 3, 4, 5])),  # test only subtractions
    ([3, 1, 2], [5, 2], ([5], [1, 3])),  # test ordering
])
def test_array_diff_v1(current, target, expected):
    assert nflx.arrays.diff_v1(current, target) == expected
