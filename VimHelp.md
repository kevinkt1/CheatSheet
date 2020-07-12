# Vim Cheat Sheet

###### [Change DOS to Unix text file format](https://til.hashrocket.com/posts/hu3jlszfrf-change-dos-to-unix-text-file-format-in-vim)
In normal mode, type `:set ff?` to see what the file format is. If it is DOS, then type `:set ff=unix` to change it to Unix.

###### [Convert tabs to spaces](https://stackoverflow.com/questions/426963/replace-tabs-with-spaces-in-vim)
```vim
:retab
```

###### [Convert 4 spaces to 2 spaces](https://gist.github.com/ericdouglas/72621cb47b368297feaa)
```vim
%s;^\(\s\+\);\=repeat(' ', len(submatch(0))/2);g
```

