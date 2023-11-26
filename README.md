<h1>Referencable objects. <code>pip install ref_type</code></h1>


**Referencable objects in Python.**

```python
from ref_type import ref


ref1: ref[int] = ref(1)
ref2: ref[int] = ref(1)


def add(r1: ref[int], r2: ref[int]) -> None:
    r1 += r2


add(ref1, ref2)

print(ref1) # => 2
```

Use `.get()` to get value, `.ilshift(X)` to do LeftShiftEquals.
