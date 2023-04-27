import json

from sentinel_3_winding.winding import get_winding


def test_chip() -> None:
    href = (
        "tests/data/S3A_SY_2_SYN_20230101T000030_20230101T000330_0179_094_016_2880.json"
    )
    with open(href, "r") as f:
        item = json.load(f)
    coords = item["geometry"]["coordinates"][0]
    assert get_winding(coords, max_delta_lon=120) == "CCW"
    coords_rev = coords[::-1]
    assert get_winding(coords_rev, max_delta_lon=120) == "CW"


def test_chip_crossing_antimeridian() -> None:
    href = (
        "tests/data/S3A_OL_2_LFR_20160425T203817_20160425T204117_0179_003_242_3780.json"
    )
    with open(href, "r") as f:
        item = json.load(f)
    coords = item["geometry"]["coordinates"][0]
    assert get_winding(coords, max_delta_lon=120) == "CCW"
    coords_rev = coords[::-1]
    assert get_winding(coords_rev, max_delta_lon=120) == "CW"


def test_simple_strip() -> None:
    href = (
        "tests/data/S3A_SY_2_VGP_20230101T012801_20230101T021201_2640_094_017_____.json"
    )
    with open(href, "r") as f:
        item = json.load(f)
    coords = item["geometry"]["coordinates"][0]
    assert get_winding(coords, max_delta_lon=120) == "CCW"
    coords_rev = coords[::-1]
    assert get_winding(coords_rev, max_delta_lon=120) == "CW"


def test_complex_strip() -> None:
    href = (
        "tests/data/S3A_SL_2_WST_20230101T002812_20230101T020911_6059_094_016_____.json"
    )
    with open(href, "r") as f:
        item = json.load(f)
    coords = item["geometry"]["coordinates"][0]
    assert get_winding(coords, max_delta_lon=120) == "CW"
    coords_rev = coords[::-1]
    assert get_winding(coords_rev, max_delta_lon=120) == "CCW"


def test_rectangle() -> None:
    href = (
        "tests/data/S3B_SY_2_V10_20230401T000000_20230410T235959_AFRICA___________.json"
    )
    with open(href, "r") as f:
        item = json.load(f)
    coords = item["geometry"]["coordinates"][0]
    assert get_winding(coords, max_delta_lon=300) == "CW"
    coords_rev = coords[::-1]
    assert get_winding(coords_rev, max_delta_lon=300) == "CCW"
