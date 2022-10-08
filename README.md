# CheatSheet
This repository is tailored for my personal use, but I want to make it public because I hope this repo will serve as a useful reference for all who come hither.

That said, I will probably exclude things that I already know to heart, such as Vim and Eclipse bindings.

# Table of Contents
<!-- vim-markdown-toc GFM -->

* [Confluence](#confluence)
  * [Bullet List](#bullet-list)
  * [Heading 1](#heading-1)
  * [Link text](#link-text)
  * [Numbered List](#numbered-list)
* [Doxygen](#doxygen)
  * [Quick Start](#quick-start)
  * [Notes](#notes)
* [Emacs](#emacs)
  * [Delete a word](#delete-a-word)
  * [Move to beginning of line](#move-to-beginning-of-line)
  * [Move to end of line](#move-to-end-of-line)
  * [Move to beginning of word](#move-to-beginning-of-word)
  * [Move to end of word](#move-to-end-of-word)
* [Excel](#excel)
  * [Delete spreadsheet](#delete-spreadsheet)
  * [Rename Excel](#rename-excel)
* [GDB](#gdb)
  * [Define the user limit to allow for generation of core files with an unlimited maximum size](#define-the-user-limit-to-allow-for-generation-of-core-files-with-an-unlimited-maximum-size)
* [Git](#git)
  * [Auto-resolve merge conflicts on all unmerged files](#auto-resolve-merge-conflicts-on-all-unmerged-files)
    * [Take our changes](#take-our-changes)
    * [Take their changes](#take-their-changes)
  * [Branches](#branches)
    * [Create branch from another branch](#create-branch-from-another-branch)
    * [Create branch from current branch](#create-branch-from-current-branch)
    * [Delete branch upstream](#delete-branch-upstream)
  * [Checkout](#checkout)
    * [Checkout another file from another local branch](#checkout-another-file-from-another-local-branch)
    * [Checkout another file from another upstream branch](#checkout-another-file-from-another-upstream-branch)
  * [Cherry Pick](#cherry-pick)
    * [Grab commit from another branch](#grab-commit-from-another-branch)
    * [View lost commits after using git reset](#view-lost-commits-after-using-git-reset)
    * [Restore lost local commits](#restore-lost-local-commits)
  * [Remote](#remote)
    * [Changing a remote's URL](#changing-a-remotes-url)
  * [Reset](#reset)
    * [Reset to a commit as it was](#reset-to-a-commit-as-it-was)
    * [Reset to a commit but leave files staged](#reset-to-a-commit-but-leave-files-staged)
    * [Reset to a commit but leave files unstaged](#reset-to-a-commit-but-leave-files-unstaged)
    * [Reset local branch to match upstream branch exactly](#reset-local-branch-to-match-upstream-branch-exactly)
  * [Status](#status)
    * [Discard all untracked files](#discard-all-untracked-files)
* [IntelliJ IDEA](#intellij-idea)
  * [Close current file](#close-current-file)
  * [Delete current line](#delete-current-line)
  * [Find a class](#find-a-class)
  * [Find a file](#find-a-file)
  * [Find text in all files](#find-text-in-all-files)
  * [Find usages](#find-usages)
  * [Navigate to definition](#navigate-to-definition)
  * [Settings menu](#settings-menu)
  * [Switch tab](#switch-tab)
* [Linux](#linux)
  * [find](#find)
    * [Find a file](#find-a-file-1)
  * [grep](#grep)
    * [Grep by file extension and sort by date](#grep-by-file-extension-and-sort-by-date)
    * [Grep for environment variables](#grep-for-environment-variables)
  * [ls](#ls)
    * [Sort all files by time](#sort-all-files-by-time)
  * [tar](#tar)
    * [Create archive without compression](#create-archive-without-compression)
    * [Compress files via gzip](#compress-files-via-gzip)
    * [Preview tarball contents without extracting](#preview-tarball-contents-without-extracting)
    * [Extract tarball to current working directory](#extract-tarball-to-current-working-directory)
    * [Extract file to a target directory](#extract-file-to-a-target-directory)
    * [A note on tarball file extensions](#a-note-on-tarball-file-extensions)
  * [zip](#zip)
    * [Zip up multiple files](#zip-up-multiple-files)
    * [Unzip a file to the current working directory](#unzip-a-file-to-the-current-working-directory)
    * [Unzip a file to the target directory](#unzip-a-file-to-the-target-directory)
* [Outlook](#outlook)
  * [Bullet list](#bullet-list-1)
  * [Link text](#link-text-1)
* [Python](#python)
  * [Subprocess](#subprocess)
    * [subprocess.run()](#subprocessrun)
      * [Arguments](#arguments)
      * [Return Value](#return-value)
* [Qt Creator Cheat Sheet](#qt-creator-cheat-sheet)
  * [Go to function definition](#go-to-function-definition)
  * [Go to line number](#go-to-line-number)
  * [Search with the Locator tool](#search-with-the-locator-tool)
  * [Switch between header and source files](#switch-between-header-and-source-files)
* [Regex](#regex)
  * [Syntax Table](#syntax-table)
  * [Edge Cases](#edge-cases)
* [PyTest](#pytest)
  * [Loop a PyTest script](#loop-a-pytest-script)
* [Sublime](#sublime)
  * [Keyboard Shortcuts](#keyboard-shortcuts)
    * [Command Palette](#command-palette)
    * [Wrap selected lines that exceed past the first ruler](#wrap-selected-lines-that-exceed-past-the-first-ruler)
  * [Packages](#packages)
    * [Anaconda package](#anaconda-package)
      * [Display signature tooltips (Anaconda: Display Object Docs)](#display-signature-tooltips-anaconda-display-object-docs)
    * [DocBlockr](#docblockr)
    * [Markdown Preview](#markdown-preview)
    * [NeoVintageous](#neovintageous)
    * [ToggleNeoVintageous](#toggleneovintageous)
      * [Toggle NeoVintageous](#toggle-neovintageous)
* [Vim](#vim)
  * [Command mode](#command-mode)
    * [Change DOS to Unix text file format](#change-dos-to-unix-text-file-format)
    * [Convert 4 spaces to 2 spaces](#convert-4-spaces-to-2-spaces)
    * [Convert tabs to 2 spaces](#convert-tabs-to-2-spaces)
    * [Convert tabs to spaces](#convert-tabs-to-spaces)
    * [Jump to line number](#jump-to-line-number)
  * [Insertion Mode](#insertion-mode)
    * [Append by inserting after the cursor](#append-by-inserting-after-the-cursor)
    * [Insert before the cursor](#insert-before-the-cursor)
    * [Append to the end of the line](#append-to-the-end-of-the-line)
    * [Insert before the first word of the line](#insert-before-the-first-word-of-the-line)
  * [Normal Mode](#normal-mode)
    * [Find all matches of word under cursor](#find-all-matches-of-word-under-cursor)
    * [Jump to line number](#jump-to-line-number-1)
    * [Movement](#movement)
      * [Center page around cursor](#center-page-around-cursor)
* [Change/delete next instance of enclosed characters within double quotation marks](#changedelete-next-instance-of-enclosed-characters-within-double-quotation-marks)
* [Change/delete next instance of enclosed characters within single quotation marks](#changedelete-next-instance-of-enclosed-characters-within-single-quotation-marks)
      * [Move cursor to the next instance of 'a'](#move-cursor-to-the-next-instance-of-a)
      * [Move cursor to right before the next instance of 'a'](#move-cursor-to-right-before-the-next-instance-of-a)
      * [Move cursor to the previous instance of 'a'](#move-cursor-to-the-previous-instance-of-a)
      * [Move cursor to right after the previous instance of 'a'](#move-cursor-to-right-after-the-previous-instance-of-a)
      * [Move to next match](#move-to-next-match)
      * [Skip to previous blank line](#skip-to-previous-blank-line)
      * [Skip to next blank line](#skip-to-next-blank-line)
  * [Visual Mode](#visual-mode)
    * [Select characters](#select-characters)
    * [Select a whole line](#select-a-whole-line)
    * [Select a whole block](#select-a-whole-block)
  * [Plugins](#plugins)
    * [plantuml-syntax](#plantuml-syntax)
    * [python-syntax](#python-syntax)
    * [vim-markdown-toc](#vim-markdown-toc)
    * [vim-rainbow](#vim-rainbow)
* [Visual Studio Code](#visual-studio-code)
  * [Extensions](#extensions)
  * [Keyboard Shortcuts](#keyboard-shortcuts-1)
    * [Code Navigation](#code-navigation)
      * [Go back](#go-back)
      * [Navigate to function definition](#navigate-to-function-definition)
    * [Views](#views)
      * [Toggle fullscreen](#toggle-fullscreen)
  * [Setup Vim for Visual Studio Code](#setup-vim-for-visual-studio-code)
    * [Plugins](#plugins-1)
* [Windows](#windows)
  * [Close/minimize an application without an X button](#closeminimize-an-application-without-an-x-button)
* [YouTube](#youtube)
  * [Disable suggested videos at the end of a video](#disable-suggested-videos-at-the-end-of-a-video)

<!-- vim-markdown-toc -->

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

# Doxygen
## Quick Start
1. `doxygen -g`
1. Edit the newly generated Doxyfile to set the `RECURSIVE` tag to `YES`.
1. To show private members, set `EXTRACT_PRIVATE` to `YES`.
1. `doxygen Doxyfile`
1. Open up `html/index.html`.

## Notes
* `@file` and `@brief` matters in the top-level comment at the start of the file.
* `@brief` does not matter in classes and functions.
* A doxygen comment is required at the top of a namespace to generate doxygen for the members within.
* A doxygen comment is not required at the top of a class.
* Add `const` to the end of `@copydoc` if `const` is part of the method signature.
* `@param[in]` does matter.
* `@param [in]` also works.
* `@throw` and `@throws` both work. Be sure to specify the exception, e.g., `@throw RuntimeError upon ...`

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

# Excel
## Delete spreadsheet
`ALT + H + D + S`

## Rename Excel
`ALT + H + O + R`

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
## Close current file
`CTRL + F4`

## Delete current line
`CTRL + X`

## Find a class
`CTRL + N`

## Find a file
`CTRL + SHIFT + N`

## Find text in all files
`CTRL + SHIFT + F`

## Find usages
`ALT + F7`

## Navigate to definition
Any of these keys will work:

* `CTRL + Left Click`
* `CTRL + ALT + B`

## Settings menu
`CTRL + ALT + S`

## Switch tab
* `ALT + Left`
* `ALT + Right`

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
## Bullet list
`* + <space>`

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

## Plugins
### plantuml-syntax

### python-syntax

### [vim-markdown-toc](https://github.com/mzlogin/vim-markdown-toc)

### vim-rainbow

---

# Visual Studio Code
It should be noted that I rarely use Visual Studio Code these days.

## Extensions
* Bookmarks
* Bracket Pair Colorizer 2
* C/C++
* CMake
* CMake Tools
* CSS Peek
* Cython
* Material Icon Theme
* PlantUML
* Python
* Remote - WSL
* Trailing Spaces
    * Currently, for a reason that I've long forgotten, I am not using this extension.

## Keyboard Shortcuts
### Code Navigation
#### Go back
`CTRL + ALT + -`

#### Navigate to function definition
`F12`

### Views
#### Toggle fullscreen
`F11`

## Setup Vim for Visual Studio Code
Note that the setup below is still not as preferable as using the original Vim.

### Plugins
* Vim plugin installation
    * Vim Plug
* https://github.com/neoclide/coc.nvim
    * `ctrl+space` autocompletion
    * `gd` goto definition
    * `ctrl+o` to go back
    * `F2` rename
    * `K` show tooltip
    * additional features
        * autoimport
        * syntax errors
    * `:CocInstall coc-snippets` to install extensions
        * coc-snippets
            * `:CocCommand snippets.editSnippets`
        * coc-pairs
        * coc-prettier
            * autoformat on save
* https://github.com/preservim/nerdtree
    * `ctrl+n` toggle file tree
* https://github.com/Xuyuanp/nerdtree-git-plugin
    * icons for file tree git status
* https://github.com/tiagofumo/vim-nerdtree-syntax-highlight
* https://github.com/ryanoasis/vim-devicons
    * icons for file tree file extensions
* https://github.com/airblade/vim-gitgutter
    * color code modified lines
    * `]c` jump to next modified line
* https://github.com/ctrlpvim/ctrlp.vim
    * `ctrl+p` fuzzy find files
* https://github.com/preservim/nerdcommenter
    * `ctrl+/` comment out code
* https://github.com/christoomey/vim-tmux-navigator
    * `ctrl+l` switch to right pane
    * `ctrl+h` switch to left pane
* https://github.com/morhetz/gruvbox
    * VS Code theme

---

# Windows
## Close/minimize an application without an X button
1. Click on the application to gain focus
1. If you are confident that you have focus:
    * To close the application, press `ALT + F4`.
    * To minimize the application, press `n`.
1. Otherwise, press `ALT + SPACE` to bring up the context menu.

---

# YouTube
## Disable suggested videos at the end of a video
Bring up the browser console (F12 on Chrome), and inject:
```javascript
for(element of document.getElementsByClassName('ytp-ce-element')) {     element.style.display = 'none'; }  
```

