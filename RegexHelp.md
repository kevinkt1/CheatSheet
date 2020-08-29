# Regex Cheat Sheet

## Syntax Table
| **Syntax** | **Description** |
|---|---|
| a | Match 'a' |
| \. | Match '.' |
| . | Match any single character except newline |
| | |
| | |
| **Category** | **Character Class** |
| [aeiou] | Match one of the given characters |
| [^aeiou] | Match any other character that is not given |
| [0-9] | Match digits 0 through 9 |
| [a-z] | Match letters a through z |
| [a-zA-Z] | Match any letter (order does not matter) |
| | |
| | |
| **Category** | **Expression** |
| \d | Match digits 0 through 9 |
| \D | Match any non-digit character |
| \s | Match any whitespace character [ \r\n\t\f ] |
| \S | Match any non-whitespace character |
| \w | Match any word character [a-z, A-Z, 0-9, underscores] |
| \W | Match any non-word character |
| | |
| | |
| **Category** | **Quantifier** |
| [xy]{5} | Match a string of length 5 consisting of characters {x,y} |
| f{1,3} | Match 'f' 1, 2, or 3 times |
| \d{4,} | Match at least 4 digit characters |
| c* | Match 'c' 0 or more times |
| t+ | Match 't' 1 or more times |
| | |
| | |
| **Category** | **Operator** |
| [a\|b] | Match 'a' or 'b' |
| ([A-Z]\|[0-9]){2} | Apply quantifier to grouping of [A-Z] or [0-9] |
| | |
| | |
| **Category** | **Anchor** |
| ^ | Beginning of string |
| $ | End of string |

## Python Syntax Table
| Syntax | Description |
| --- | --- |
| `r'\b'` | Word boundary special character |

#### Cases
**----------**
> `s1 = True`, `s2 = True`, `s3 = True`
```regex
s[0-9] = True
```

**----------**
> `123.456.abc.def`
```regex
^.{3}\..{3}\..{3}\..{3}$
```

**----------**
> `the hackerrank team`
```regex
r'\b' + 'hackerrank' + r'\b'
```
