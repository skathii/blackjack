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
Your current hand: [16]
d5
sA


The dealers hand: [2]
d2


What would you like to do? [h/s]: h


########################
The dealer passes you a card.
Your current hand: [12]
d5
sA
s6


What would you like to do? [h/s]: h


########################
The dealer passes you a card.


########################
Oops! You busted with a score of 23. Better luck next time!


Your final hand:
d5
sA
s6
cA


########################
Would you like to continue playing? [y/n] n
Thanks for playing! Created by skathii; (http://www.github.com/skathii)
The program will terminate in three seconds.
```
