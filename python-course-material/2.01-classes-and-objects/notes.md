# 2.1 Classes and Objects

This course picks up where course 1.00 left off and covers object oriented
programming, or OOP for short. Up to now everything we've written has been
data in one place (variables, lists, dictionaries) and functions somewhere
else that act on that data. OOP is a different way of organizing a program.
Instead of keeping data and functions separate, we bundle them together into
one thing called an object.

This is a big topic, so we're spreading it across a few sections. This first
one is just about the basic idea, classes, objects, and how to give an object
its own data.

## Why bother with objects

Say you are building a card game. Without OOP you might represent a card as a
dictionary:

```python
card = {"suit": "Hearts", "rank": "Ace", "value": 14}
```

That works, but it gets messy fast. Nothing stops you from writing
`card["value"] = "banana"`, there's no obvious place to put a function like
"print this card nicely", and if you need fifty two of these things you end up
with fifty two dictionaries floating around with no real structure holding
them together.

A class lets you define what a card *is* (a suit, a rank, a value) all in one
place. Once the class exists, you can stamp out as many cards as you want from
it, and every one of them will keep that same structure.

## Classes and objects

A class is basically a blueprint. It doesn't do anything by itself, it just
describes what something should look like. An object (also called an
instance) is an actual thing built from that blueprint.

Think of it like a cookie cutter and the cookies. The cookie cutter is the
class, it defines the shape. Each cookie you cut out is an object, a real
cookie you can actually eat. You can use the same cutter to make as many
cookies as you like, and every one of them will have that shape, but each
cookie is still its own cookie.

Here's the smallest class we can write:

```python
class Dog:
    pass

my_dog = Dog()
```

`class Dog:` defines the blueprint. `my_dog = Dog()` creates an actual object
from that blueprint. Right now the class doesn't do anything interesting, so
let's give it some data.

## The `__init__` method and attributes

Most classes need some way to set up their data as soon as an object is
created. That's what `__init__` is for. It runs automatically the moment you
create a new object from the class.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

my_dog = Dog("Rex", "Labrador")
print(my_dog.name)   # Rex
print(my_dog.breed)  # Labrador
```

A couple of things to notice here:

- `self` refers to the specific object being created. Every method inside a
  class takes `self` as its first parameter, even though you never actually
  type it in when you call the method. Python passes it in for you.
- `self.name = name` is what actually saves the value onto the object.
  Anything attached to `self` like this is called an attribute, it's a piece
  of data that belongs to that specific object.
- Two different `Dog` objects can have completely different names and
  breeds, because each one gets its own separate copy of these attributes.

```python
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Milo", "Beagle")

print(dog1.name)  # Rex
print(dog2.name)  # Milo
```

Every object created from `Dog` follows the same blueprint, name and breed,
but the actual values living inside each object are independent of one
another.

## Quick reference

| Term | What it means |
| --- | --- |
| Class | A blueprint that describes what an object looks like |
| Object / instance | An actual thing created from a class |
| `__init__` | Runs automatically when a new object is created, used to set up attributes |
| `self` | Refers to the specific object a method is being called on |
| Attribute | A piece of data that belongs to an object, e.g. `self.name` |

## Practice test

1. What is the difference between a class and an object?
2. What does `self` refer to inside `__init__`?
3. What is the purpose of the `__init__` method, and when does it run?
4. Write a class called `Book` with a title and an author, set through
   `__init__`.
5. Create two different `Book` objects and print out each one's title.
6. True or false: two objects created from the same class always share the
   exact same attribute values.

<details>
<summary>Answers</summary>

1. A class is a blueprint that describes what an object should look like.
   An object (instance) is an actual thing built from that blueprint —
   you can make many objects from the same class.
2. `self` refers to the specific object the method is currently running
   on — the exact instance being created or worked with.
3. `__init__` sets up an object's initial data (its attributes). It runs
   automatically the instant a new object is created from the class.
4. ```python
   class Book:
       def __init__(self, title, author):
           self.title = title
           self.author = author
   ```
5. ```python
   book1 = Book("Dune", "Frank Herbert")
   book2 = Book("1984", "George Orwell")

   print(book1.title)  # Dune
   print(book2.title)  # 1984
   ```
6. False — each object gets its own independent copy of the attributes.
   Two `Book` objects can easily have different titles and authors.

</details>

Once you're comfortable with the questions above, move on to
`2.02-methods-and-special-methods`, where we teach objects to actually do
things.
