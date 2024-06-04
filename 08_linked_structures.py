"""Playing with different ways of implementing linked lists in Python."""

from __future__ import annotations
from typing import Any, Generic, NamedTuple, TypeVar, TypeVarTuple


T = TypeVar('T')
Ts = TypeVarTuple('Ts')


class Node(NamedTuple, Generic[T, *Ts]):
    """A base class for a linked list."""

    val: T
    nxt: None | Node[*Ts]

    def __repr__(self) -> str:
        """Render as string."""
        # get the type of value as a string
        val_type_str = ""
        grabbing = False
        # type(...) returns something like <class 'some class name'>
        # but we only want the name of the class, not the whole <...>
        for char in str(type(self.val)):
            # include a check that char isn't closing single quote
            # before grabbing the char
            if grabbing and char != "'":
                val_type_str += char
            # items inside single quotes need to be grabbed,
            # here we assume there won't be any nested single quotes
            # and that there will only be one single quoted substring
            if char == "'":
                grabbing = not grabbing

        # make sure strings are rendered as strings using quotes
        val_str = (
            f"\"{self.val}\""
            if isinstance(self.val, str)
            else self.val)

        return f"Node[{val_type_str}]({val_str}, {self.nxt})"


n1 = Node("a str", None)
n0 = Node(1, n1)

print(n0)
