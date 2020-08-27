from foo_pkg import A
from dataclasses import dataclass


@dataclass
class B(A):
    attr_in_b: int


B(attr_in_a=0, attr_in_b=1)
