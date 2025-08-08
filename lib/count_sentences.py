#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""            # internal variable
        self.value = value          # uses setter to validate

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            # Exactly matches what the test expects:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Normalize the string to a single delimiter for splitting
        normalized = self._value.replace("!", ".").replace("?", ".")
        # Split into parts and strip whitespace, ignoring empties
        parts = [chunk.strip() for chunk in normalized.split(".") if chunk.strip()]
        return len(parts)


