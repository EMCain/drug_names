from lib.drug_name import is_offensive, is_duplicate

bad_words = ['gosh', 'knucklehead', 'toot']


def test_is_offensive_banned_words():
    assert is_offensive("gosh", bad_words)
    assert is_offensive("bygosh", bad_words)
    assert is_offensive("toot", bad_words)
    assert is_offensive("rooty tooty", bad_words)


def test_is_offensive_harmless_words():
    assert not is_offensive("mom", bad_words)
    assert not is_offensive("baby", bad_words)
    assert not is_offensive("smile", bad_words)
    assert not is_offensive("chewbacca", bad_words)


def test_is_duplicate_existing_drugs():
    assert is_duplicate("Venlafaxine")
    assert is_duplicate("Metoprolol")
    assert is_duplicate("Lorazepam")


def test_is_duplicate_fictional_drugs():
    assert not is_duplicate("Spice Melange")
    assert not is_duplicate("Substance D")
    assert not is_duplicate("Ketracel-white")
