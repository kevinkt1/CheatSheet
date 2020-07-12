# Python CheatSheet

#### Subprocess
##### subprocess.run()
###### Example
```python
# Python 3.5+
p = subprocess.run(fullCmdStr,
                   shell=True,
                   check=False,
                   executable='/bin/bash')
```
###### Arguments
* `executable` defaults to `sh` instead of `Bash`
* `check` throws an exception if the command failed

###### Return Value
* `p.returncode` is set to 0 if the command completed successfully
  * _For example, `diff` returns 0 if there was no difference_

