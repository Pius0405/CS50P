# Blackjack Python❤️ 💎 ♣️  ♠️
## About this project
- Creator : Pius
- GitHub username : Pius0405
> This is a Python Blackjack game created for the final project of the **CS50P: Introduction to programming with Python** course by **Havard University**. It applies most knowledges learned during the course so it's beginers friendly. Feel free to refer use this project as a resource in your learning :)
## Project requirements
1. Language used:
   - Python (Basic knowledge is required)
2. Third party libraries required:
   - pytest
     - install pytest with `pip install pytest` at the terminal
3. Libraries used:
   - random
     - Documentation: https://docs.python.org/3/library/random.html
   - sys
     - Documentation: https://docs.python.org/3/library/sys.html
   - pytest
     - Documentation: https://docs.pytest.org/en/7.4.x/
   - time
     - Documentation: https://docs.python.org/3/library/time.html
> *Import module using `import` command, for example `import random`

## Project description

>The whole game is implemented using Object-Oriented Programming (OOP). OOP is a **programming paradigm** that allows us to define our own **type** using the `class` command. We can then define the **attributes** and **methods** for objects from that class.

>Game details:
1. Classes used:
   - Card
     - To store each cards in the deck and encapsulate all functions related to the class as **class method** using `@classmethod` decorator
   - Player
     - A **superclass** for player (user player and dealer).
   - HumanPlayer
     - A **derived class** where the **superclass** is Player. A HumanPlayer is created when a user plays the game.
   - Dealer
     - A **derived class** where the **superclass** is Player. A Dealer is created when a user plays the game.

> *Create an object using the constructor method, for example `HumanPlayer(username)`

2. Game logic (In structred English):
```
* Both player and dealer each draw to cards
* Check if any party got Blackjack to decide the winner or tie (Both parties got Blackjack)
* Otherwise, back to the player's turn
* Player can decide whether to Hit ("H") or Stand ("S"), however if player's score is lower than 12 the player must Hit. Each time the player gets a new card, recalculate the score.
* If the player gets 21 or busted end the program immediately with appropriate message.
* If player stands and neither win nor lose, it's the dealer's turn. Dealer will randomly choose a move (If dealer's score less than 12, dealer will Hit too).
* Dealer can additionally choose to Open ("O") which is to reveal both parties card and the party with higher score wins.
* If the dealer gets 21 or busted end the program immediately with appropriate message.
```
```
Algorithm for calculating score based on cards on player's or dealer's hand:
* Loop through each card on the hand
* For cards that are not Ace, add face value to score
* For Ace cards, consider to add 11 if ended up the score does not exceed 21 otherwise add 1
* This ensures that the score is at maximum possible and if busted, lowest possible
```

3. Project testing
   -  execute `pytest test_project.py -s` at the terminal
   - `-s` is a flag to tell python that when testing `get_move` we have to manually provide an input for the function to be tested
>*For complete understanding, please watch the **video demo** below

## Video demo
> Video demo URL: https://www.youtube.com/watch?v=8Xno10RmjIY
