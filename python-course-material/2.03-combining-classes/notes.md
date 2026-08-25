# 2.3 Combining Classes

So far every example has used a single class on its own. Real programs
usually need several classes working together, one object holding other
objects as attributes. We'll also cover the convention of giving each class
its own file, which becomes important the moment a project has more than one
or two of them.

## Classes that use other classes

Classes don't have to stand alone, one class can hold objects made from
another class. This is sometimes called composition, one object is made up of
other objects.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Owner:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

my_dog = Dog("Rex", "Labrador")
owner = Owner("Sam", my_dog)

print(owner.dog.name)  # Rex
```

`owner.dog` gives you back the actual `Dog` object, and from there you can
reach into that object's attributes as usual, `owner.dog.name`. This kind of
relationship shows up constantly. A `Car` might hold an `Engine`, a `Library`
might hold a list of `Book` objects, and in our milestone project a `Deck`
holds a list of `Card` objects.

Composition also works with lists of objects, not just a single one:

```python
class Library:
    def __init__(self, books):
        self.books = books

book1 = Book("Dune", "Frank Herbert")
book2 = Book("1984", "George Orwell")

library = Library([book1, book2])

for book in library.books:
    print(book)
```

## One class, one file

Once your program has more than a couple of classes, it gets hard to keep
track of everything if they're all crammed into one script. The convention,
and the one we'll follow from here on, is to give each class its own file,
named after the class. If you have a `Dog` class, it lives in `Dog.py`. If
you have an `Owner` class, it lives in `Owner.py`.

To use a class from another file, you import it, the same way you'd import
`random` or `math`:

```python
from Dog import Dog

my_dog = Dog("Rex", "Labrador")
```

If your classes live inside a folder, say a folder called `Classes`, you
include the folder name in the import too:

```python
from Classes.Dog import Dog
```

This might feel like overkill for a small program, but it becomes second
nature once you're working on anything bigger, and it means anyone reading
your project can find exactly what they're looking for without scrolling
through one giant file. It also keeps each class focused on doing one thing
well, since it isn't tangled up with a bunch of unrelated code around it.

## Quick reference

| Term | What it means |
| --- | --- |
| Composition | One object holding other objects as attributes |
| One class, one file | The convention of giving each class its own file, named after the class |
| `from file import Class` | How you bring a class defined in another file into the one you're working in |

## Practice test

1. Write a `Library` class that stores a list of `Book` objects.
2. Given a `Library` object called `library`, how would you print the title
   of the first book inside it?
3. Why does it help to give each class its own file once a project grows?
4. If `Owner.py` needs the `Dog` class from `Dog.py`, what line goes at the
   top of `Owner.py`?
5. If `Dog.py` lives inside a folder called `Classes`, how does that import
   line change?

That covers everything you need. Head over to `2.04-milestone-project` for
the project that puts all three sections together.
