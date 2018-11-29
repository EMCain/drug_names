from drug_name import is_offensive, is_duplicate

bad_words = ['gosh', 'knucklehead', 'toot']

def test_is_offensive_banned_words():
    assert is_offensive("gosh", bad_words) == True
    assert is_offensive("bygosh", bad_words) == True
    assert is_offensive("toot", bad_words) == True
    assert is_offensive("rooty tooty", bad_words) == True


def test_is_offensive_harmless_words():
    assert is_offensive("mom", bad_words) == False
    assert is_offensive("baby", bad_words) == False
    assert is_offensive("smile", bad_words) == False
    assert is_offensive("chewbacca", bad_words) == False


def test_is_duplicate_existing_drugs():
    assert is_duplicate("Venlafaxine") == True
    assert is_duplicate("Metoprolol") == True
    assert is_duplicate("Lorazepam") == True


def test_is_duplicate_fictional_drugs():
    assert is_duplicate("Spice Melange") == False
    assert is_duplicate("Substance D") == False
    assert is_duplicate("Ketracel-white") == False
