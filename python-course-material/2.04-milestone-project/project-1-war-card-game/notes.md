# Milestone Project: War Card Game

A two player terminal version of the classic card game War, built using
classes instead of one big script.

## The rules

Each player gets half the deck, dealt face down. Every round both players
flip their top card and whoever flipped the higher card wins the round and
takes both cards, adding them to the bottom of their pile. If both cards
match in value, it's a war, three more cards each get thrown in and another
card is flipped to break the tie. Whoever runs out of cards first loses.

## How the project is organized

Instead of putting everything in one file, the project is split into a
class for each of the three things the game actually needs:

| File | Class | What it represents |
| --- | --- | --- |
| `Classes/Card.py` | `Card` | A single playing card, its suit, rank, and value |
| `Classes/Deck.py` | `Deck` | A full deck of 52 `Card` objects, can shuffle itself |
| `Classes/Player.py` | `Player` | A player, holds their current cards and the cards they've won |
| `main.py` | — | Ties everything together and runs the game |

`Card` is the simplest class, it just stores a suit and a rank and looks up
the matching value from a dictionary of ranks to values. `Deck` builds a full
set of `Card` objects when it's created and knows how to shuffle its own
`cards` list, this is the composition idea from 2.3, a `Deck` is really just
an object holding a list of `Card` objects. `Player` keeps track of two
piles, the cards currently in hand and the cards won during play, and can
draw from the top of their hand.

`main.py` doesn't know or care how any of these classes work internally, it
just creates a `Deck`, shuffles it, deals it out to two `Player` objects, and
runs the game loop, comparing cards and handling wars when they happen. That
separation is the whole point of doing this with classes, `main.py` stays
short and readable because all the messy details are tucked away inside the
classes that actually own them.

## Running it

From inside this folder, run:

```
python main.py
```

You'll be asked for both players' names, then the game plays itself out
round by round in the terminal until one player runs out of cards.

## Things to try once you understand it

- Add a running counter that prints how many rounds have been played
- Track and print how many wars have happened by the end of the game
- Let the user choose a deck size, for a shorter or longer game
- Add a `strongest_card` method to `Player` that returns their highest value
  card
