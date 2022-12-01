import pytest

from year_2019.challenge_8 import corrupt_check, render_image


@pytest.mark.parametrize(
    "bits, width, height, checksum",
    [
        ("123456789012", 3, 2, 1),
        ("120267890027", 3, 2, 2),
        ("100267810227", 3, 2, 2),
    ],
)
def test_corrupt_check(bits, width, height, checksum):
    assert corrupt_check(bits, width, height) == checksum


@pytest.mark.parametrize(
    "bits, width, height, image",
    [
        ("0222112222120004", 2, 2, [" 1", "14"]),
    ],
)
def test_render_image(bits, width, height, image):
    assert list(render_image(bits, width, height)) == image
