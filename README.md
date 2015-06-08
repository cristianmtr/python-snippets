# PYTHON-SNIPPETS
Re-usable pieces of python source code

## Process_handler: ##
Handles creation of processes.
- Reading from stdout and stderr

```
#!python
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

## Simple_encryption: ##
Encrypt and decrypt files using a passphrase, with salts and bcrypt

```
#!bash
echo "test text to encrypt" > input
python test_encryption.py -i input -o output -p passphrase encrypt
cat output
*encrypted gibbersh here*
./test_encryption.py -i output -o input_check -p test decrypt
*NOTE: you will be asked to provide the salt generated during the encryption process*
cat input_check
test text to encrypt

```

## TODO ##
- SQLAlchemy auto-mapping
- handle reading salts correctly from command-line options
- simple wsgi
- simple multiprocessing with queue
- how to interact with process created in background;
- reference the performance test-case comparing lists and sets;
