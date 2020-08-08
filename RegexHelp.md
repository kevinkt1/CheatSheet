# Regex Cheat Sheet

## Syntax Table
| Syntax | Description |
|---|---|
| [0-9] | Match digits 0 through 9 |
| a | Match 'a' |
| f{2} | Quantifier to match exactly two consecutive 'f' |
| . | Match any single character except newline |
| \. | Match '.' |
| * | Match all characters |
| ^ | Anchor for beginning of string |
| $ | Anchor for end of string |

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
