#!/usr/bin/env python3
"""Multiple inheritance example: Fish, Bird, and FlyingFish."""


class Fish:
    """Simple Fish with swim and habitat methods."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Simple Bird with fly and habitat methods."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A creature that can both swim and fly; overrides parents."""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
