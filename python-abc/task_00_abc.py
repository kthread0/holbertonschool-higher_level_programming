#!/usr/bin/env python3
"""Abstract Animal class and simple subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base for animals requiring a sound method."""

    @abstractmethod
    def sound(self):
        """Return the sound this animal makes."""


class Dog(Animal):
    """Dog implements Animal.sound to bark."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat implements Animal.sound to meow."""

    def sound(self):
        return "Meow"
