# Blackjack
A blackjack game programmed in Python which can be played in your Terminal.


## Installation & Requirements

Download or Copy the **Blackjack.py** file and call the Blackjack function.
The script uses three packages which are available in every enviromnent: random, time and sys.

## Usage
```python
def blackjack(deckcount):
```
Deckcount takes an integer value which can give you multiple decks.

## Example

```python
from Blackjack import blackjack
blackjack(1)
```

gives
```python
########################
Your current hand: [19]
s9
hQ


The dealers hand: [2]
d2


What would you like to do? [h/s]: s


########################
You stood on 19. The Dealers face-down card was:
dJ


The Dealers hand is: [12]
The dealer gives himself a card.
His score is now 22
d2
dJ
hJ


########################
Hurray! The dealer Busted with a score of 22! Congratulations!


Your final hand: [19]
s9
hQ


The Dealers final hand: [22]
d2
dJ
hJ


########################
Would you like to continue playing? [y/n] n
Thanks for playing! Created by skathii; (http://www.github.com/skathii)
The program will terminate in three seconds.
```
