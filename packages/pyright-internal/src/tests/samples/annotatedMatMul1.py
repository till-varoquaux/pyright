from typing import Annotated, reveal_type

# Test 1: Simple Annotated with @
def func1(x: int @ "meta"):
    reveal_type(x, expected_text="int")

# Test 2: Chained @
def func2(x: int @ "m1" @ "m2"):
    reveal_type(x, expected_text="int")

# Test 3: Union with @
def func3(x: (int | str) @ "meta"):
    reveal_type(x, expected_text="int | str")

# Test 4: @ with forward ref
def func4(x: "A" @ "meta"):
    reveal_type(x, expected_text="A")

class A:
    pass

# Test 5: @ at runtime
x = int @ "meta"
reveal_type(x)

# Test 6: None @ M
def func5(x: None @ "meta"):
    reveal_type(x, expected_text="None")

# Test 7: Type aliases, cast, TypeVar, ParamSpec
from typing import Callable, ClassVar, Final, NotRequired, ParamSpec, ReadOnly, Required, TypeAlias, TypedDict, TypeVar, cast
from dataclasses import KW_ONLY, InitVar, dataclass

Alias1 = int @ "m1"
Alias2: TypeAlias = str @ "m2"
type Alias3 = bytes @ "m3"

T = TypeVar("T", bound=int @ "m4")
P = ParamSpec("P")

def func6(a: Alias1, b: Alias2, c: Alias3, obj: object, t: T) -> T:
    reveal_type(a, expected_text="int")
    reveal_type(b, expected_text="str")
    reveal_type(c, expected_text="bytes")
    y = cast(int @ "m5", obj)
    reveal_type(y, expected_text="int")
    return t

def deco(f: Callable[P, int]) -> Callable[P, int]:
    def wrapper(*args: P.args @ "m1", **kwargs: P.kwargs @ "m2") -> int:
        return f(*args, **kwargs)
    return wrapper

# Test 8: TypedDict and Dataclass qualifiers with @
class TD(TypedDict):
    a: NotRequired[int] @ "m1"
    b: Required[str] @ "m2"
    c: ReadOnly[int] @ "m3"

@dataclass
class DC:
    x: int @ "m1"
    y: InitVar[str] @ "m2"
    _: KW_ONLY @ "m_kw"
    z: int @ "m_z" = 0
    cv: ClassVar[int] @ "m3" = 1
    fin: Final[int] @ "m4" = 2

    def __post_init__(self, y: str) -> None:
        reveal_type(y, expected_text="str")

dc = DC(1, "hello", z=3)
reveal_type(dc.x, expected_text="int")

