# Tomuhs_Blackjack is a blackjack card game 
...that im trying to build with python, as im learning it, to exercise and learn.
  The game is now "finished", the code i wrote is probably bad and a lot of things could be automatized, but i did it
  by my best skills. So i would really apprecciate any comments or thoughts about making the code for this more 
  efficent or less long. Thank you.

 # The game:
   You start by the Dealer asking you, if you want to take a card. By typing in replies "y" or "n", you simply play.
   Cards you take have points. There are four cards for each number (card numbers are from 2 to 10, so for example: there are four 2s,)
   When you take the card, you are keeping it, and it doesn't return to the pack, so when you are given one 4 and two 2s, there are two 2s left in the pack, three 4s, and four cards of any other number.
   The card number represents the number of points you receive to your "total points".

   The aim of the game is to keep picking up cards, until your total points get as much close as possible, to the number 21.
   When you exceed the number 21, you lose.
   When your points are exactly 21, you automatically stop picking up cards, and the Dealer is on the move.
   Everytime you are given a card, and you haven't lost yet, you are given the option, to pick another card, or stop picking.
   When you stop picking, the dealer is on the move.

   You win, when the dealer with his cards exceeds 21.
   You lose, when the dealer's points are higher than yours (and are under 21)  
   When both the player, and the dealer hits exactly 21, its a draw.
