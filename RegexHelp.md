# Regex Cheat Sheet

## Syntax Table
| Syntax | Description |
|---|---|
| a | Match 'a' |
| f{2} | Quantifier to match exactly two consecutive 'f' |
| \. | Match '.' |
| . | Match any single character except newline |
| * | Match all characters |
| | |
| | |
| | |
| Category | Character Class |
| [0-9] | Match digits 0 through 9 |
| [aeiou] | Match one of the given characters |
| [^aeiou] | Match any other character that is not given |
| | |
| | |
| | |
| Category | Expression |
| \d | Match digits 0 through 9 |
| \D | Match any non-digit character |
| \s | Match any whitespace character [ \r\n\t\f ] |
| \S | Match any non-whitespace character |
| \w | Match any word character [a-z, A-Z, 0-9, underscores] |
| \W | Match any non-word character |
| | |
| | |
| | |
| Category | Anchor |
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
