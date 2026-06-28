# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

When I first ran the game, it looked like a normal guessing game where the AI asked the user to guess a number between 1 and 100 and told me I had 8 attempts in total. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

However, I found 3 bugs upon playing the game, the first being that the guessing bar said I could "press enter to apply" but wouldn't apply the guess unless I clicked the button "Submit Guess". Next, the hints are opposite, for example if the guess was higher than the correct number, the hint would tell me to guess lower and vice versa when my guess was lower than the number. Lastly, the "New Game" button doesn't actual start a new game and it doesn't reset the page.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                            | Expected Behavior                           | Actual Behavior                                 | Console Output / Error |
|----------------------------------|---------------------------------------------|-------------------------------------------------|------------------------|
|Type guess and press Enter        |Guess is submitted automcatically            |Nothing happens unless "Submit button" is clicked| None                   |
|Guess is lower than target number |Hint provided is "Go HIGHER!"                |Hint provided is "GO LOWER!"                     | None                   |
|Guess is higher than target number|Hint provided is "Go LOWER!"                 |Hint provided is "GO HIGHER!"                    | None                   |
|Click "New Game" button           |Game resets with new number and cleared state|Game does not reset and nothing changes          | None                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude for AI-guided assistance in debugging the game and verifying that test cases passed. I also used ChatGPT to help set up the project and interpret error messages in VS.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

For bug #1, Claude correctly identified that the check_guess function returned a tuple and that tests were incorrectly comparing the full tuple to a string, consequently outputting incorrect hints
It was correct and I verified the result by running pytest and observing assertion failures. I updated tests to unpack (outcome, message) for the return statement, and all tests passed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For bug #2, Claude suggested changing the entire attempts model from "guesses used" to "remaining guesses" which was misleading because the rest of the UI display and game-over logic was built around "attempts used". Additionally, it tried to make changes to code outside the area of the error". I avoided this change and instead kept the original model, only fixing the inconsistant updata behavior.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I checked if a bug was fixed by running pytest (or python -m pytest if that didn't work) to ensure all test cases passes. I also tested the game manually using Streamlit and entered guesses around the range of the secret number to check if the hints were correct.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

Using pytest, the first test I ran showed that only two of the four cases passed. The error message told me that the problem was specifically in the test_winning_guess and test_guess_too_high functions in the test_game_logic.py file. This helped me find the location of the error and fix it to have all four of the cases pass.

- Did AI help you design or understand any tests? How?

Claude helped me understand why some of my tests were failing by explaining the difference between a function returning a single value verses returning a tuple (outcome, message). It explained that my original tests were incorrectly comparing the entire tuple to a string which causes assertion errors.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
