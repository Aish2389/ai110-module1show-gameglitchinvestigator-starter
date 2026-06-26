from logic_utils import check_guess

# FIX (Bug 1): Updated tests to match tuple return format from check_guess
# Originally tests assumed single string return, but function returns (outcome, message)
# Verified fix using pytest (all 4 tests passed)
# AI-assisted debugging helped identify incorrect test assumptions
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_direction_is_correct():
    # Regression test for the reversed-hint bug.
    # check_guess returns (outcome, message). The outcome labels were always
    # correct; the bug was in the direction the MESSAGE told the player to go,
    # so we assert on both the outcome and the hint direction.

    # Guess lower than the secret -> "Too Low", and the hint must say go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

    # Guess higher than the secret -> "Too High", and the hint must say go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    # Correct guess -> win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message
