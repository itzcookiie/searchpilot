from find_winner import find_winner


def test_row():
    assert (
        find_winner(
            [
                ["R", "R", "R", "R", "L", "L", "L"],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
            ]
        )
        == "R"
    )


def test_col():
    assert (
        find_winner(
            [
                [None, "R", None, None, "L", "L", "L"],
                [None, "R", None, None, None, None, None],
                [None, "R", None, None, None, None, None],
                [None, "R", None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
            ]
        )
        == "R"
    )


def test_right_diagonal():
    assert (
        find_winner(
            [
                [None, "R", None, None, "L", "L", "L"],
                [None, "L", "R", None, None, None, None],
                [None, "L", None, "R", None, None, None],
                [None, None, None, None, "R", None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
            ]
        )
        == "R"
    )


def test_left_diagonal():
    assert (
        find_winner(
            [
                [None, "R", None, None, "L", "L", "L"],
                [None, "L", "R", None, None, "L", None],
                [None, "L", None, "R", "L", None, None],
                [None, None, None, "L", None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
            ]
        )
        == "L"
    )


def test_no_winner():
    assert (
        find_winner(
            [
                ["R", "R", "R", "L", "R", None, "R"],
                [None, None, "R", None, None, None, None],
                ["R", "R", "R", None, "R", "R", "R"],
                ["L", None, None, None, "L", "R", None],
                ["R", "L", "R", "R", "L", "L", "R"],
                ["R", "L", "R", "R", "L", "L", "R"],
            ]
        )
        is None
    )


def test_right_diagonal_going_down():
    assert (
        find_winner(
            [
                [None, "R", None, None, "L", "L", "L"],
                [None, "L", "R", None, None, "L", None],
                [None, "L", None, "R", "L", None, None],
                [None, None, "R", None, None, None, None],
                [None, "R", None, None, None, None, None],
                ["R", None, None, None, None, None, None],
            ]
        )
        == "R"
    )


def test_left_diagonal_going_down():
    assert (
        find_winner(
            [
                [None, "R", None, None, "L", "L", "L"],
                [None, "L", "R", None, None, "L", None],
                [None, "L", None, "L", "L", None, None],
                [None, None, None, None, "L", None, None],
                [None, None, None, None, None, "L", None],
                [None, None, None, None, None, None, "L"],
            ]
        )
        == "L"
    )
