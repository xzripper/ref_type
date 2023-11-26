"""Referencable objects for Python."""

from typing import TypeVar, Generic, Any


_p_r_v: str = '1.0.0'

ReferenceType = TypeVar('ReferenceType')

class ref(Generic[ReferenceType]):
    """Referencable object."""

    __object: ReferenceType = None

    def __init__(self, _object: ReferenceType) -> None:
        """Reference on object."""
        self.__object = _object

    def __add__(self, other: Any) -> Any:
        """Add overload."""
        return self.__object + other.__object if isinstance(other, ref) else other

    def __sub__(self, other: Any) -> Any:
        """Subtract overload."""
        return self.__object + other.__object if isinstance(other, ref) else other

    def __mul__(self, other: Any) -> Any:
        """Multiply overload."""
        return self.__object * other.__object if isinstance(other, ref) else other

    def __truediv__(self, other: Any) -> Any:
        """TrueDivision overload."""
        return self.__object / other.__object if isinstance(other, ref) else other

    def __floordiv__(self, other: Any) -> Any:
        """FloorDivision overload."""
        return self.__object // other.__object if isinstance(other, ref) else other

    def __pow__(self, other: Any) -> Any:
        """Power overload."""
        return self.__object ** other.__object if isinstance(other, ref) else other

    def __rshift__(self, other: Any) -> Any:
        """RightShift overload."""
        return self.__object >> other.__object if isinstance(other, ref) else other

    def __lshift__(self, other: Any) -> Any:
        """LeftShift overload."""
        return self.__object << other.__object if isinstance(other, ref) else other

    def __and__(self, other: Any) -> Any:
        """And overload."""
        return self.__object & other.__object if isinstance(other, ref) else other

    def __or__(self, other: Any) -> Any:
        """Or overload."""
        return self.__object | other.__object if isinstance(other, ref) else other

    def __xor__(self, other: Any) -> Any:
        """XOR overload."""
        return self.__object ^ other.__object if isinstance(other, ref) else other

    def __lt__(self, other: Any) -> Any:
        """Less overload."""
        return self.__object < other.__object if isinstance(other, ref) else other

    def __gt__(self, other: Any) -> Any:
        """More overload."""
        return self.__object > other.__object if isinstance(other, ref) else other

    def __le__(self, other: Any) -> Any:
        """LessEquals overload."""
        return self.__object <= other.__object if isinstance(other, ref) else other

    def __ge__(self, other: Any) -> Any:
        """MoreEquals overload."""
        return self.__object >= other.__object if isinstance(other, ref) else other

    def __eq__(self, other: Any) -> Any:
        """Equals overload."""
        return self.__object == other.__object if isinstance(other, ref) else other

    def __ne__(self, other: Any) -> Any:
        """NotEquals overload."""
        return self.__object != other.__object if isinstance(other, ref) else other

    def __isub__(self, other: Any) -> None:
        """SubtractEquals overload."""
        self.__object -= other.__object if isinstance(other, ref) else other

    def __iadd__(self, other: Any) -> None:
        """AddEquals overload."""
        self.__object += other.__object if isinstance(other, ref) else other

    def __imul__(self, other: Any) -> None:
        """MultiplyEquals overload."""
        self.__object *= other.__object if isinstance(other, ref) else other

    def __idiv__(self, other: Any) -> None:
        """DivisionEquals overload."""
        self.__object /= other.__object if isinstance(other, ref) else other

    def __ifloordiv__(self, other: Any) -> None:
        """FloorDivisionEquals overload."""
        self.__object //= other.__object if isinstance(other, ref) else other

    def __imod__(self, other: Any) -> None:
        """ModuloEquals overload."""
        self.__object %= other.__object if isinstance(other, ref) else other

    def __ipow__(self, other: Any) -> None:
        """PowerEquals overload."""
        self.__object **= other.__object if isinstance(other, ref) else other

    def __irshift__(self, other: Any) -> None:
        """RightShiftEquals overload."""
        self.__object >>= other.__object if isinstance(other, ref) else other

    def __ilshift__(self, other: Any) -> None:
        """LeftShiftEquals overload: set object."""
        self.__object = other

    def __iand__(self, other: Any) -> None:
        """AndEquals overload."""
        self.__object &= other.__object if isinstance(other, ref) else other

    def __ior__(self, other: Any) -> None:
        """OrEquals overload."""
        self.__object |= other.__object if isinstance(other, ref) else other

    def __ixor__(self, other: Any) -> None:
        """XOREquals overload."""
        self.__object >>= other.__object if isinstance(other, ref) else other

    def __neg__(self) -> Any:
        """Negative overload."""
        return -self.__object

    def __pos__(self, other: Any) -> Any:
        """Positive overload."""
        return +self.__object

    def __invert__(self, other: Any) -> Any:
        """Invert overload."""
        return ~self.__object

    def __repr__(self) -> ReferenceType:
        """Represent reference."""
        return str(self.__object)

    def get(self) -> ReferenceType:
        """Get object."""
        return self.__object

    def ilshift(self, other: Any) -> None:
        """LeftShiftEquals / Use this instead of operator."""
        self.__object <<= other
