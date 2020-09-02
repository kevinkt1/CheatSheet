# Regex Cheat Sheet

## Syntax Table
| **Syntax** | **Description** |
|---|---|
| a | Match 'a' |
| \. | Match '.' |
| . | Match any single character except newline |
| | |
| | |
| **Character Class** | **Description** |
| [aeiou] | Match one of the given characters |
| [^aeiou] | Match any other character that is not given |
| [0-9] | Match digits 0 through 9 |
| [a-z] | Match letters a through z |
| [a-zA-Z] | Match any letter (order does not matter) |
| \d | Match digits 0 through 9 |
| \D | Match any non-digit character |
| \s | Match any whitespace character [ \r\n\t\f ] |
| \S | Match any non-whitespace character |
| \w | Match any word character [a-z, A-Z, 0-9, underscores] |
| \W | Match any non-word character |
| | |
| | |
| **Quantifier** | **Description** |
| [xy]{5} | Match a string of length 5 consisting of characters {x,y} |
| f{1,3} | Match 'f' 1, 2, or 3 times |
| \d{4,} | Match at least 4 digit characters |
| c* | Match 'c' 0 or more times |
| t+ | Match 't' 1 or more times |
| | |
| | |
| **Operator** | **Description** |
| [a\|b] | Match 'a' or 'b' |
| ([A-Z]\|[0-9]){2} | Apply quantifier to grouping of [A-Z] or [0-9] |
| | |
| | |
| **Anchor** | **Description** |
| ^ | Beginning of string |
| $ | End of string |
| | |
| | |
| **Grouping and Capturing** | **Description** |
| r'\b' | Word boundary special character (r is needed in Python to avoid confusion with the backspace character) |
| () | Capture a group |
| ? | Optionally capture this group |
| (?\|regex1\|regex2) | Known as a 'branch reset group' that matches one of these groups or nothing |
| \1 | Matches the same text as previously matched by the first capturing group |

## Edge Cases
* `(b?)o\1`
    * Successfully matches 'o' because the backreference matches the nothing captured by the group
* `(b)?o\1`
    * In most regex flavors (excluding JavaScript), this regex pattern fails to match 'o' because the backreference references a group that did not participate in the match at all

