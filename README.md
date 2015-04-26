# PYTHON-SNIPPETS
Re-usable pieces of python source code

## Process_handler: ##
Handles creation of processes.
- Reading from stdout and stderr
```

from process_handler import Process
p = Process("dir")
output = p.run()

p = Process("git status", dir="path\to\your\dir")
output = p.run()
```

## TODO ##
- how to interact with process created in background;
- refactor Process: store stdout and stderr in variable, run() should return void;
- reference the performance test-case comparing lists and sets;
