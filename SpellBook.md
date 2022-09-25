# Confluence
## Bullet List
`CTRL + SHIFT + 8`

## Heading 1
`CTRL + ALT + 0`

## Link text
`CTRL + K`

## Numbered List
`CTRL + SHIFT + 7`

---

# Emacs
## Delete a word
`ESC + d`

## Move to beginning of line
`CTRL + a`

## Move to end of line
`CTRL + e`

## Move to beginning of word
`ESC + b`

## Move to end of word
`ESC + f`

--- 

# GDB
## Define the user limit to allow for generation of core files with an unlimited maximum size
Command-line:

`ulimit -c unlimited`

# Git
## Auto-resolve merge conflicts on all unmerged files
### Take our changes
`grep -lr '<<<<<<<' . | xargs git checkout --ours`
### Take their changes
`grep -lr '<<<<<<<' . | xargs git checkout --theirs`

## Branches
### Create branch from another branch
`git checkout -b new-branch old-branch`

### Create branch from current branch
`git checkout -b new branch`

### Delete branch upstream
`git push --delete origin branch-name`

## Checkout
### Checkout another file from another local branch
`git checkout local-branch-name -- local-file.txt`

### Checkout another file from another upstream branch
`git checkout origin/upstream-branch-name -- upstream-file.txt`

## Cherry Pick
### Grab commit from another branch
`git cherry-pick commit-number-from-other-branch`

### View lost commits after using git reset
`git reflog`

### Restore lost local commits
1. `git reflog`

1. `git cherry-pick local-commit-number`

1. Merge the changes

1. `git cherry-pick continue`

## [Remote](https://docs.github.com/en/github/using-git/changing-a-remotes-url)
### Changing a remote's URL
`git remote set-url origin https://github.com/USERNAME/REPOSITORY.git`

## Reset
### Reset to a commit as it was
`git reset --hard commit-number`

### Reset to a commit but leave files staged
`git reset --soft commit-number`

### Reset to a commit but leave files unstaged
`git reset --mixed commit-number`

### Reset local branch to match upstream branch exactly
```bash
git pull
git reset --hard origin/branch-name
```

## Status
### Discard all untracked files
`git clean -fdn`
* `f` is force
* `d` is directory
* `n` is to preview changes (remove the `n` flag to actually clean)
* `x` is to remove ignored files

---

# IntelliJ IDEA
## Settings menu
`CTRL + ALT + S`

## Find a file
`CTRL + SHIFT + N`

---

# Linux
## find
### Find a file
`find ./ -name filename.txt`
* `-iname` can be used for case insensitivity

## grep
### Grep by file extension and sort by date
`ls -rt *.txt | xargs grep -lr --include=\*.txt 'searchterm' ./`

### Grep for environment variables
`env | grep ENV_VAR_NAME`

## ls
### Sort all files by time
`ls -lta`

## tar
### Create archive without compression
`tar -cvf sample.tar file1 file2 file3`

### Compress files via gzip
`tar -zcvf sample.tgz file1 file2 file3`

### Preview tarball contents without extracting
`tar -tvf file.tgz`
* `-t` is shorthand for `--test`

### Extract tarball to current working directory
`tar -xvf file.tar`
* `-xvf` is shorthand for `--extract --verbose --file`

### Extract file to a target directory
`tar -C target-directory file.tgz`
* `-C` changes to the target directory before extracting the tar file

### A note on tarball file extensions
* `.tar` is the conventional file extension to indicate the tarball is storing uncompressed data.
* `.tgz`, `.tar.gz`, and `.gz` are the conventional file extensions indicating the tarball is storing compressed data.

## zip
### Zip up multiple files
`zip sample.zip file1 file2 file3`
* Add `-r` flag to zip a directory

### Unzip a file to the current working directory
`unzip file.zip`

### Unzip a file to the target directory
`unzip -d target-directory file.zip`

---

# Outlook
## Link text
`CTRL + K`

---

# Python
## Subprocess
### subprocess.run()
```python
# Python 3.5+
p = subprocess.run(fullCmdStr,
                   shell=True,
                   check=False,
                   executable='/bin/bash')
```

#### Arguments
* `executable` defaults to `sh` instead of `bash`.
* `check` throws an exception if the command failed.

#### Return Value
* `p.returncode` is set to 0 if the command completed successfully.

---

# Qt Creator Cheat Sheet
## Go to function definition
`F2`

## Go to line number
`CTRL + L`

## Search with the Locator tool
`CTRL + K`

## Switch between header and source files
`F4`

--- 

# Regex
## Syntax Table
| **Syntax** | **Description** |
|---|---|
| a | Match 'a' |
| \\. | Match '.' |
| . | Match any single character except newline |
| | |
| | |
| **Character Class** | **Description** |
| [0-9] | Digits within this range |
| \d | Digits 0 through 9 |
| \D | Non-digits |
| [aeiou] | Match one of the given characters |
| [^aeiou] | Match any other character that is not given |
| [a-zA-Z] | Letter within this range (a-ZA-Z or A-Za-z) |
| \s | Whitespace [\r\n\t\f] |
| \S | Non-whitespace |
| \w | Word [a-z, A-Z, 0-9, underscores] |
| \W | Non-word |
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
| \1 | Matches the same text as previously matched by the first capturing group |
| (?\|regex1\|regex2) | Known as a 'branch reset group' that matches one of these groups or nothing |
| (\2two|(one))+ | Forward reference that creates a backreference to a regex that would appear later; matches 'oneonetwo' |
| | |
| | |
| **Lookahead** | **Description** |
| a(?!b) | Negative lookahead to notate that 'a' cannot be followed by 'b' |
| a(?=b) | Positive lookahead to notate that 'a' must be followed by 'b' |
| (?<=a)b |  Positive lookbehind to notate that 'a' must precede 'b' |
| (?<!a)b | Negative lookbehind to notate that 'a' cannot precede 'b' |

## Edge Cases
* `(b?)o\1`
    * Successfully matches 'o' because the backreference matches the nothing captured by the group
* `(b)?o\1`
    * In most regex flavors (excluding JavaScript), this regex pattern fails to match 'o' because the backreference references a group that did not participate in the match at all

---

# PyTest
## Loop a PyTest script
Add a loop inside the main.

---

# Sublime
## Keyboard Shortcuts
### Command Palette
`CTRL + SHIFT + P`

### Wrap selected lines that exceed past the first ruler
`ALT + Q`

## Packages
### Anaconda package
#### Display signature tooltips (Anaconda: Display Object Docs)
`CTRL + ALT + D`

### DocBlockr

### Markdown Preview

### [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous)

### [ToggleNeoVintageous](https://github.com/NeoVintageous/ToggleNeoVintageous)
#### Toggle NeoVintageous
`CTRL + ALT + T`

---

# Vim
## Command mode
### [Change DOS to Unix text file format](https://til.hashrocket.com/posts/hu3jlszfrf-change-dos-to-unix-text-file-format-in-vim)
```vim
" Determine the current file format
:set ff?

" If the current file format is DOS, change the file format to Unix
:set ff=unix
```

### [Convert 4 spaces to 2 spaces](https://gist.github.com/ericdouglas/72621cb47b368297feaa)
```vim
:%s;^\(\s\+\);\=repeat(' ', len(submatch(0))/2);g
```

### [Convert tabs to 2 spaces](https://gist.github.com/ericdouglas/72621cb47b368297feaa)
```vim
:%s/\t/  /g
```

### [Convert tabs to spaces](https://stackoverflow.com/questions/426963/replace-tabs-with-spaces-in-vim)
```vim
:retab
```

### Jump to line number
```vim
" Jump to line 25
:25
```

## Insertion Mode
### Append by inserting after the cursor
`a`

### Insert before the cursor
`i`

### Append to the end of the line
`A`

### Insert before the first word of the line
`I`

## Normal Mode
### Find all matches of word under cursor
`*`

### Jump to line number
```vim
" Jump to line 25
25G
```

### Movement
#### Center page around cursor
`zz`

# Change/delete next instance of enclosed characters within double quotation marks
`ci"`
`di"`

# Change/delete next instance of enclosed characters within single quotation marks
`ci'`
`di'`

#### Move cursor to the next instance of 'a'
`fa`

#### Move cursor to right before the next instance of 'a'
`ta`

#### Move cursor to the previous instance of 'a'
`Fa`

#### Move cursor to right after the previous instance of 'a'
`Ta`

#### Move to next match
`;`

#### Skip to previous blank line
`{`

#### Skip to next blank line
`}`

## Visual Mode
### Select characters
`v`

### Select a whole line
`V`

### Select a whole block
`CTRL + v` OR `CTRL + q`

---

# Visual Studio Code
## Go back
`CTRL + ALT + -`

# Windows
## Close/minimize an application without an X button
1. Click on the application to gain focus
1. If you are confident that you have focus:
    * To close the application, press `ALT + F4`.
    * To minimize the application, press `n`.
1. Otherwise, press `ALT + SPACE` to bring up the context menu.
