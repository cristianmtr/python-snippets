#! /usr/bin/python
import subprocess
import os

class Process(object):
    def __init__(self, command, bg=False, dir=""):
        self.command = command
        self.bg = bg
        self.cwd = ""
        if dir == "":
            self.cwd = os.getcwd()
        else:
            self.cwd = dir
        self.stdout = ""
        self.stderr = ""
    def _shell_command(self):
        self.output = subprocess.check_output(self.command, shell=True,cwd=self.cwd)
    def _execute_and_return(self):
        split_command = self.command.split()
        # windows limitation
        shell_commands = ["dir"]
        if split_command[0] in shell_commands:
            self._shell_command()
        else:
            try:
                p = subprocess.Popen(
                    split_command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=self.cwd,
                )
                self.stdout = p.stdout.read()
                self.stderr = p.stderr.read()
            except Exception as e:
                self.stderr = e
    def _start_and_return_pid(self):
        raise RuntimeError
    def run(self):
        if self.bg == True:
            self._start_and_return_pid()
        else:
            self._execute_and_return()
        

            
