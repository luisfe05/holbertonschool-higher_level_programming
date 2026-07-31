# Python - Everything is object

## Description
This project is a set of short conceptual exercises on Python's object model: what `id()`, `type()`, `==`, and `is` actually reveal about objects, the difference between mutable and immutable types, how CPython interns small integers and certain string/tuple constants, how list mutation vs. reassignment behaves, and how arguments are actually passed to functions (by object reference, not by value or by reference in the C/Pascal sense). Each numbered task is a one-line answer file, verified against real Python 3 execution rather than assumption. Task 19 is a short `copy_list` function.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Who am I?** | Function used to print the type of an object. | `0-answer.txt` |
| **1. Where are you?** | Function used to get a variable's identifier (memory address in CPython). | `1-answer.txt` |
| **2. Right count** | Do `a = 89` and `b = 100` point to the same object? | `2-answer.txt` |
| **3. Right count =** | Do `a = 89` and `b = 89` point to the same object? | `3-answer.txt` |
| **4. Right count =** | Do `a = 89` and `b = a` point to the same object? | `4-answer.txt` |
| **5. Right count =+** | Do `a = 89` and `b = a + 1` point to the same object? | `5-answer.txt` |
| **6. Is equal** | What `s1 == s2` prints for `s2 = s1` on a string. | `6-answer.txt` |
| **7. Is the same** | What `s1 is s2` prints for `s2 = s1` on a string. | `7-answer.txt` |
| **8. Is really equal** | What `s1 == s2` prints for two separately-created equal strings. | `8-answer.txt` |
| **9. Is really the same** | What `s1 is s2` prints for two separately-created equal strings. | `9-answer.txt` |
| **10. And with a list, is it equal** | What `l1 == l2` prints for two separately-created equal lists. | `10-answer.txt` |
| **11. And with a list, is it the same** | What `l1 is l2` prints for two separately-created equal lists. | `11-answer.txt` |
| **12. And with a list, is it really equal** | What `l1 == l2` prints for `l2 = l1`. | `12-answer.txt` |
| **13. And with a list, is it really the same** | What `l1 is l2` prints for `l2 = l1`. | `13-answer.txt` |
| **14. List append** | What prints after aliasing a list and calling `.append()` on the alias. | `14-answer.txt` |
| **15. List add** | What prints after aliasing a list and reassigning one name via `+`. | `15-answer.txt` |
| **16. Integer incrementation** | What prints after passing an int to a function that does `n += 1`. | `16-answer.txt` |
| **17. List incrementation** | What prints after passing a list to a function that calls `.append()`. | `17-answer.txt` |
| **18. List assignation** | What prints after passing a list to a function that reassigns the local name. | `18-answer.txt` |
| **19. Copy a list object** | 3-line `copy_list(a_list)` function that returns a shallow copy of a list, no imports. | `19-copy_list.py` |
| **20-23. Tuple or not?** | Whether `()`, `(1, 2)`, `(1)`, and `(1, )` are actually tuples. | `20-answer.txt` … `23-answer.txt` |
| **24. Who I am?** | What `a is b` prints for `a = (1)` and `b = (1)`. | `24-answer.txt` |
| **25. Tuple or not** | What `a is b` prints for `a = (1, 2)` and `b = (1, 2)`. | `25-answer.txt` |
| **26. Empty is not empty** | What `a is b` prints for two separately-created empty tuples. | `26-answer.txt` |
| **27. Still the same?** | Whether `id(a)` stays the same after `a = a + [5]`. | `27-answer.txt` |
| **28. Same or not?** | Whether `id(a)` stays the same after `a += [4]`. | `28-answer.txt` |

Task 29 (a blog post on mutability/immutability, published externally on Medium/LinkedIn) isn't a repo file and isn't tracked here.

## Author
* **Luis Gonzalez** - Holberton School
