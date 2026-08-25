# Milestone Project: War Card Game

A two player terminal version of the classic card game War, built using
classes instead of one big script. This is a build-it-yourself project —
the notes below give you the pieces you need for each class, but you'll
write the actual code. Once you're happy with what you've got (or if you
get stuck), the finished, working version lives in
[`solution/`](solution) so you can check your work or see how it's done.

## The rules

Each player gets half the deck, dealt face down. Every round both players
flip their top card and whoever flipped the higher card wins the round and
takes both cards, adding them to the bottom of their pile. If both cards
match in value, it's a war, three more cards each get thrown in and another
card is flipped to break the tie. Whoever runs out of cards first loses.

## How to organize it

Build a class for each of the three things the game actually needs, one
class per file, the convention from 2.3:

| File | Class | What it represents |
| --- | --- | --- |
| `Classes/Card.py` | `Card` | A single playing card, its suit, rank, and value |
| `Classes/Deck.py` | `Deck` | A full deck of 52 `Card` objects, can shuffle itself |
| `Classes/Player.py` | `Player` | A player, holds their current cards and the cards they've won |
| `main.py` | — | Ties everything together and runs the game |

Create a `Classes` folder alongside `main.py` and build each piece below
inside it.

---

## Step 1 — `Card`

A `Card` just needs to remember its suit, its rank, and its numeric value
(so two cards can be compared to see which is higher). You'll need a
dictionary that maps each rank name to a value, this part you can copy
as-is:

```python
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
    'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
    'Ten': 10, 'Jack': 11, 'Queen': 12,
    'King': 13, 'Ace': 14
}
```

Now write the `Card` class itself. It needs:

- An `__init__` that takes `suit` and `rank`, stores both as attributes,
  and looks up the matching `value` from the dictionary above and stores
  that too. (Think back to 2.1 — how do you save something onto `self`?)
- A `__str__` method so printing a card shows something readable, like
  `"Ace of Spades"` (2.2 covered this).

**Things to think about**
- Where does `values[rank]` belong — inside `__init__`, so it runs once
  when the card is created?
- What does your `__str__` need to `return` to produce `"Ace of Spades"`
  from `self.rank` and `self.suit`?

---

## Step 2 — `Deck`

A `Deck` is composition in action (2.3): it's really just an object that
holds a list of 52 `Card` objects. You'll need to import your `Card` class
at the top of `Deck.py`:

```python
from Classes.Card import Card
```

You'll also need every suit and every rank to build a full deck. These you
can copy as-is:

```python
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
```

Now write the `Deck` class. It needs:

- An `__init__` that creates an empty list attribute (say, `self.cards`),
  then builds all 52 cards into it — one `Card` for every combination of
  suit and rank. (Hint: this means a loop inside a loop, one over `suits`,
  one over `ranks`, creating and appending a new `Card` each time round.)
- A `shuffle` method that shuffles `self.cards` in place. Python's
  built-in `random` module has a function for exactly this —
  `random.shuffle(some_list)` shuffles a list directly, it doesn't return
  a new one. Don't forget `import random` at the top of the file.

**Things to think about**
- Why does building the deck belong in `__init__` rather than a separate
  method?
- `random.shuffle()` doesn't return anything useful, it changes the list
  you hand it directly. What does that mean for how you call it?

---

## Step 3 — `Player`

A `Player` needs a name, a pile of cards currently in hand, and a pile of
cards they've won during play. Write the `Player` class with:

- An `__init__` that takes `name` and stores it, plus two empty list
  attributes to start: one for cards in hand, one for won cards.
- An `add_cards` method that takes a list of cards and adds all of them
  onto the player's hand. (Hint: `.extend()` adds every item from one
  list onto another, `.append()` would add the whole list as one item,
  which isn't what you want here.)
- A `draw_card` method that removes and returns the top card from the
  player's hand. (Hint: `.pop()` removes and returns the last item of a
  list.)
- A `total_cards` method that returns how many cards the player has in
  total, hand plus won pile combined.
- A `__str__` method that just returns the player's name, so `print()`ing
  a player shows their name directly.

---

## Step 4 — `main.py`

This is where everything comes together. Import what you need at the top:

```python
import random
from Classes.Deck import Deck
from Classes.Player import Player
```

Break it into three functions.

### `start_game()`

- Ask for both players' names with `input()` and create two `Player`
  objects.
- Create a `Deck` and shuffle it.
- Deal the deck out evenly between the two players. (Hint: loop over
  `deck.cards` with `enumerate()`, and use the index to alternate which
  player each card goes to — even index to player one, odd to player
  two, `add_cards` expects a list, so wrap each single card in `[card]`.)
- Call `play_game(player1, player2)` to start the game loop.

### `play_game(player1, player2)`

This function should loop forever until someone runs out of cards
entirely. On every pass through the loop, check:

- If a player has no cards in hand **and** no won cards, they're out —
  print that they lost and `break` out of the loop.
- If a player has no cards in hand but does have won cards, their hand
  just ran dry mid-game. Move their won pile back into their hand
  (`.extend()` then clear the won pile) and shuffle it, then `continue`
  back to the top of the loop.
- Otherwise, both players can play — call a `play_round(player1,
  player2)` function to run one round.

### `play_round(player1, player2)`

This is the trickiest part. Keep a running list of `battle_cards`, the
cards currently at stake in this round (it grows if there's a war).

- Both players `draw_card()` from their hand, and both cards get added to
  `battle_cards`.
- Compare the two cards' `.value`. Whoever is higher wins: give them
  every card in `battle_cards` (`.extend()` onto their `won_cards`) and
  print that they won the round.
- If the values are equal, it's a war: check both players still have at
  least 4 cards left (a war needs 3 "face-down" cards plus 1 to flip). If
  either doesn't, print that the game is over and stop. Otherwise, draw 3
  more cards from each player straight into `battle_cards` and loop back
  around to flip another card each and compare again.

**Things to think about**
- What loop structure fits `play_round`, given it might need to repeat
  itself if there's a war?
- Where exactly do the drawn cards need to end up if nobody wins the
  round yet?

Finally, tie it together at the bottom of the file:

```python
if __name__ == "__main__":
    start_game()
```

---

## Running it

Once you've built all four pieces, run it from inside this project's
folder:

```
python main.py
```

You'll be asked for both players' names, then the game plays itself out
round by round in the terminal until one player runs out of cards.

Stuck, or want to compare your version once it's working? The full,
working solution is in [`solution/`](solution) — same structure
(`solution/Classes/Card.py`, `solution/Classes/Deck.py`,
`solution/Classes/Player.py`, `solution/main.py`), runnable the same way
from inside the `solution/` folder.

## Things to try once you understand it

- Add a running counter that prints how many rounds have been played
- Track and print how many wars have happened by the end of the game
- Let the user choose a deck size, for a shorter or longer game
- Add a `strongest_card` method to `Player` that returns their highest value
  card
