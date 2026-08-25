# 2.2 Methods and Special Methods

In the last section we gave our objects data through attributes. Now we'll
give them behavior, things they can actually do. We'll also look at a couple
of special methods Python looks for automatically, and use them to control
how our objects get printed.

## Methods

A method is just a function that lives inside a class and can use `self` to
work with that object's attributes.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Rex", "Labrador")
my_dog.bark()  # Rex says woof!
```

`bark` doesn't need to be told the dog's name, it already has access to it
through `self.name`, because `self` is that exact object. This is really the
whole point of OOP, the data and the behavior that uses that data live
together in the same place.

Methods can also take extra arguments, just like a regular function, they
just always take `self` first.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def greet(self, other_name):
        print(f"{self.name} sniffs {other_name} and wags his tail.")

my_dog = Dog("Rex", "Labrador")
my_dog.greet("Milo")  # Rex sniffs Milo and wags his tail.
```

## The `__str__` method

By default, if you try to print an object, Python gives you something not
very useful:

```python
print(my_dog)  # <__main__.Dog object at 0x000001A2B3C4D5E6>
```

You can control what gets printed by defining a `__str__` method. Python
calls this automatically whenever the object is turned into a string, like
when you `print()` it. It's called a special method because you never call it
yourself, Python calls it for you behind the scenes. You'll be able to spot
these by the double underscores on either side of the name, `__init__` from
the last section is another one.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} the {self.breed}"

my_dog = Dog("Rex", "Labrador")
print(my_dog)  # Rex the Labrador
```

Notice `__str__` has to `return` a string, not print one. Python takes
whatever it returns and uses that as the printed output.

## Quick reference

| Term | What it means |
| --- | --- |
| Method | A function defined inside a class, can access the object's attributes through `self` |
| Special method | A method Python calls automatically rather than you calling it directly, named with double underscores |
| `__str__` | Controls what gets shown when you `print()` an object, must return a string |

## Practice test

1. What's the difference between a regular function and a method?
2. Why do methods always take `self` as their first parameter?
3. Add a `read` method to a `Book` class that prints
   `"You start reading <title>."`
4. What happens if you print an object from a class that has no `__str__`
   method?
5. Add a `__str__` method to your `Book` class so printing a book shows
   `"<title> by <author>"`.
6. True or false: `__str__` should use `print()` inside it to display the
   text.

Next up is `2.03-combining-classes`, where we look at classes that hold
other objects, and the convention of giving each class its own file.
