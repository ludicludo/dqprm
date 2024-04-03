from extract_suv import extract_infos


def test_extraction_OK():
    assert extract_infos(".*", "SUV") is not None
    assert extract_infos(".*", "HU") is not None
    assert extract_infos(".*", "suv") is not None


def test_extraction_NON_OK():
    assert extract_infos(".*", "toto") is None
