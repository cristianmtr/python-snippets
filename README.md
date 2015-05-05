# PYTHON-SNIPPETS
Re-usable pieces of python source code

## Process_handler: ##
Handles creation of processes.
- Reading from stdout and stderr
```

from process_handler import Process
p = Process("dir")
p.run()
output = p.stdout
error = p.stderr

p = Process("git status", dir="path\to\your\dir")
p.run()
output = p.stdout
error = p.stderr

```

## TODO ##
- handle reading salts correctly
- simple wsgi
- simple multiprocessing with queue
- how to interact with process created in background;
- reference the performance test-case comparing lists and sets;
