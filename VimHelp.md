# Vim Cheat Sheet

## Command mode
### [Change DOS to Unix text file format](https://til.hashrocket.com/posts/hu3jlszfrf-change-dos-to-unix-text-file-format-in-vim)
In normal mode, type `:set ff?` to see what the file format is. If it is DOS, then type `:set ff=unix` to change it to Unix.

### [Convert tabs to spaces](https://stackoverflow.com/questions/426963/replace-tabs-with-spaces-in-vim)
```vim
:retab
```

### [Convert 4 spaces to 2 spaces](https://gist.github.com/ericdouglas/72621cb47b368297feaa)
```vim
%s;^\(\s\+\);\=repeat(' ', len(submatch(0))/2);g
```
## Key bindings
* Opening VIM
* Exiting VIM
* Save without quitting
* Move with h,j,k,l
* Going into insert mode
* Going back to command mode
* dd for delete line
* Use arrow keys to move (not recommended)
* G and gg for top and bottom lines
* {,} to skip blocks of code
* Using numbers to loop command
* u for undo and redo
* Cntrl+r for redo
* yy for copying line 
* p for pasting line below
* P for pasting line above
* using dd to cut a line for pasting
* use V for visual line mode to select lines
* Do stuff with selected lines
* o for inserting the new line below
* O for inserting new line above
* d+<command> to delete characters
* w to jump forward words and b to jump backward
* :<num> to jump to specific line
* 0 for the beginning of the line and $ for the end of the line. 
* ^ for beginning word
* W for jumping forward a word (ignore punctuation)
* t+<char> and f+<char> to go to specific character in a line
* % to go to specific block parenthesis
* c+<command> for changing characters
* D to delete from cursor to end of line
* \* to search for other instances
* ; to go to the next instance of a character when using t,f
* zz to center your page based on the cursor's position
* a to insert from the right of the character, i to insert from left
* A to insert from the end of the line, I to insert from the beginning of the line
* x to delete a character which cursor is on
* ~ to change the case of a letter
* . to repeat the last executed command
* r to replace a letter, R to go to replace mode
* Commend combo to move a chunk of code from bottom to top
* Commend combo to wrap a chunk of code
* >> to indent line, << to unindent
* macros
* Rafactoring example
* v for selecting chunks of characters
* Cntrl+v to select in a block format
* /<chars> to search for words in the document,n goto next occurrence
* Removing multiple occurrences using macros
*:45 VScode Emulation
*:50 Rebinding <Esc> in VSCode
*:38 Chrome emulation

* Opening VIM
* Exiting VIM
* Save without quitting
* Move with h,j,k,l
* Going into insert mode
* Going back to command mode
* dd for delete line
* Use arrow keys to move (not recommended)
* G and gg for top and bottom lines
* {,} to skip blocks of code
* Using numbers to loop command
* u for undo and redo
* Cntrl+r for redo
* yy for copying line 
* p for pasting line below
* P for pasting line above
* using dd to cut a line for pasting
* use V for visual line mode to select lines
* Do stuff with selected lines
* o for inserting the new line below
* O for inserting new line above
* d+<command> to delete characters
* w to jump forward words and b to jump backward
* :<num> to jump to specific line
* 0 for the beginning of the line and $ for the end of the line. 
* ^ for beginning word
* W for jumping forward a word (ignore punctuation)
* t+<char> and f+<char> to go to specific character in a line
* % to go to specific block parenthesis
* c+<command> for changing characters
* D to delete from cursor to end of line
* * to search for other instances
* ; to go to the next instance of a character when using t,f
* zz to center your page based on the cursor's position
* a to insert from the right of the character, i to insert from left
* A to insert from the end of the line, I to insert from the beginning of the line
* x to delete a character which cursor is on
* ~ to change the case of a letter
* . to repeat the last executed command
* r to replace a letter, R to go to replace mode
* Commend combo to move a chunk of code from bottom to top
* Commend combo to wrap a chunk of code
* >> to indent line, << to unindent
* macros
* Rafactoring example
* v for selecting chunks of characters
* Cntrl+v to select in a block format
* /<chars> to search for words in the document,n goto next occurrence
* Removing multiple occurrences using macros
