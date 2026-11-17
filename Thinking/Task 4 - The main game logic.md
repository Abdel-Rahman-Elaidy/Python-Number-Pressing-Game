# Overview

Here we will create the main logic of the game. 

The main logic is: 
- user guesses a number
- algorithm finds weither number is larger or smaller number and displays the fiiting message. 

## Algorithim

goal:
- detect if the guessed number is smaller or bigger than the real number
- display the message


## Problem:

goal outcome: if the user doesn't get the correct answer, he gets a hint and a new prompt to guess the number and repeat till the user gets the write answer. 

this has 2 things: 
1. A loop that repeat the if-logic so long the user doesn't get the correct answer
2. The if-logic that checks if the number is correct and provides a feedback prompt. 

part 2 is solved, part 1 is the problem. 

goal of part 1: the loop should run the if-logic once everytime the user submits an answer until the user gets the correct answer. 

the logic is simple: 
1. run the if-logic once the user submits an answer 
2. the if-logic (function) does 4 things: 
    1. compares user answers to the random number generated
    2. if higher, drop hint to lower
    3. if lower, drop hint to increase
    4. if correct, drop congrats meesage and stop running the function

pic picture logic: 
1. prompt user
2. run the if-logic function
3. repeat step 1 and 2 until user gets the correct answer

this is where chances can ruin things but we will fix that problem at that time. 

## New Problem

The make your new guess prompt is being repeated at the end. 

End Goal: run game logic while not re-running the prompt

basically we want to keep running a function until we get the right answer. Once that happens we run a congrates message

**Satus**: Done



