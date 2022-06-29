from regextractor import extract


def test_extract():
    s1 = "abc$1250"
    s2 = "xby#340"
    s3 = "sbs@00000"
    print(extract([s1, s2, s3]))

    s1 = "skull"
    s2 = "school"
    print(extract([s1, s2]))

    s1 = "<div></div>"
    s2 = "<span></span>"
    print(extract([s1, s2]))

    supertags = [
        "prefix_898999898_substring_323_suffix",
        "prefix_598993898_substring_123_suffix",
        "prefix_898999498_substring_223_suffix",
        "prefix_998999899_substring_423_suffix",
    ]
    print(extract(supertags))
