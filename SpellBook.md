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
`CTRL+L`

## Search with the Locator tool
`CTRL+K`

## Switch between header and source files
`F4`

--- 

# Regex
## Match whitespace character
`\s`

---

# PyTest
## Loop a PyTest script
Add a loop inside the main.

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
