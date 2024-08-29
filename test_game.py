import pytest
import game


def test_check_validity():
    assert game.check_validity("rock") == 2
    assert game.check_validity("scissors") == 1
    assert game.check_validity("paper") == 0
    with pytest.raises(ValueError):
        game.check_validity("invalid")


def test_check_winner():
    assert game.check_winner(2, 2) == 0
    assert game.check_winner(0, 0) == 0
    assert game.check_winner(1, 1) == 0

    assert game.check_winner(2, 1) == 1
    assert game.check_winner(1, 0) == 1
    assert game.check_winner(0, 2) == 1

    assert game.check_winner(1, 2) == 2
    assert game.check_winner(0, 1) == 2
    assert game.check_winner(2, 0) == 2

    with pytest.raises(ValueError):
        game.check_winner(3, 0)
    with pytest.raises(ValueError):
        game.check_winner(0, 3)


if __name__ == "__main__":
    pytest.main()
