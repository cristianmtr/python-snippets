# PYTHON SNIPPETS
Re-usable pieces of python code

## Python singleton

// TODO

## MODULE LOGGER

Usage:
```python
from get_logger import get_module_logger


my_logger = get_module_logger(__name__)
my_logger.info("Hello from module!")
my_logger.error("Oups, something went wrong")
```

Will look like:
```
INFO:__main__:Hello from module!
ERROR:__main__:Oups, something went wrong
```

## SQLAlchemy auto-mapping

Say you have a database somewhere and you want to use and/or add data, but you don't want to bother with writing complex SQL queries, or bother with each particular engine's different syntax.

Use SQLAlchemy's powerful auto-mapping and schema detection to use the data as Python objects.

First let's create a simple db in SQLite
```
sqlite3 foo.db
> .read schema.sql
> .quit
```

Now, you can either look at the code and apply it to your own needs.

Run the test scenario like this
```
python sqlalchemy_automap.py
```

Or the script to print out column names and types in the db
```
python show_columns.py
```


## Process_handler: ##
Handles creation of processes.

### Solution one ###

```python
from process_handler import popen_improved


node_version = popen_improved(["node.exe", "--version"])
print node_version.output
print node_version.err
print node_version.exit_code
```

Will look like:
```
In [5]: node_version.output
Out[5]: 'v5.7.1'

In [6]: node_version.err
Out[6]: ''

In [7]: node_version.exit_code
Out[7]: 0
```

### Solution two ###

Reading from stdout and stderr:

```python
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

### solution three ###

```python
from process_handler import shell_ex
return_code, stdout, stderr = shell_ex("dir")
print return_code, stdout, stderr
> (0,
> '#README.md#  process_handler.py   simple_encryption.py\nREADME.md    process_h
>andler.pyc  sqlalchemy_automap\n',
> '')
```

## Simple_encryption: ##
Encrypt and decrypt files using a passphrase, with salts and bcrypt

```
echo "test text to encrypt" > input
python test_encryption.py -i input -o output -p passphrase encrypt
cat output
*encrypted gibbersh here*
./test_encryption.py -i output -o input_check -p test decrypt
*NOTE: you will be asked to provide the salt generated during the encryption process*
cat input_check
test text to encrypt

```

## Function decorator
In func_decorator.py, you can find a simple example of how to do function decoration.

## Apache config reader

Example of how to use:

```python
a = ApacheConfig.parse_file("httpd.conf")
for chld in a.children:
  print chld.name, ": ", chld.values
```

Output example:
```
ServerRoot :  ['"d:/Apache24"']
LoadModule :  ['access_compat_module', 'modules/mod_access_compat.so']
LoadModule :  ['actions_module', 'modules/mod_actions.so']
[...]
IfModule :  ['unixd_module']
ServerAdmin :  ['admin@domain.com']
ServerName :  ['172.16.185.163:80']
Directory :  ['/']
DocumentRoot :  ['"d:/htdocs"']
Directory :  ['"d:/htdocs"']
[...]
```
            

## TODO ##
- sql: dump query for each step in the terminal
- handle reading salts correctly from command-line options
- simple wsgi
- simple multiprocessing with queue
- how to interact with process created in background;
- reference the performance test-case comparing lists and sets;
