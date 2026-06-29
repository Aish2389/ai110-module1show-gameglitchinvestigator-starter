# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
      The purpose of the game is to simulate a number guessing game where the user attempted to guess a randomly generated secret number with a limited number of attempts. The game provides feedback after each guess and tracks the user's attempts and score.

- [ ] Detail which bugs you found.
      1. The hints were reversed. When the guess was higher than the secret number, the game incorrectly told the user to guess lower, and vice versa.
      2. The number of attempts was not being tracked correctly. In some cases, the game ended early and showed "Out of attempts" even when attempts were still remaining.
      3. The score was inconsistent and did not follow a clear pattern. Score updates changed unpredictably depending on attempt number, making it difficult to interpret or match expected behavior.
- [ ] Explain what fixes you applied.
      1. I corrected the hint logic so that the hints correctly reflect the relationship between the guess and secret number by refactoring game logic to ensure consistent behavior and game flow
      2. I fixed the attempt tracking by ensuring the attempt counter is properly updated correctly across game interactions, improving reliability of state updates across user interactions.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User starts the game
2. User enter guess: 40
   - Game Output: "Too Low" and score
   - Attempts: 1
3. User enters guess: 70
   - Game Output: "Too High"
   - Attempts: 2
4. User correctly guesses: 60
   - Game Output: "Correct!" and score
   - Game ends successfully
5. OR User incorrectly guesses: 50
   - Game Output: "Out of attempts" & reveals secret number and score
   - Game is over


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# =================================================================== test session starts ===================================================================
platform win32 -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\pazha\AI110\Game Investigator\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 5 items                                                                                                                                          

tests\test_game_logic.py .....                                                                                                                       [100%]

==================================================================== 5 passed in 3.24s ====================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
