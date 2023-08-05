from SeminarAPI_1.task1.task1 import check_works


def test_step1(gut, bet):
    assert gut in check_works(bet)

