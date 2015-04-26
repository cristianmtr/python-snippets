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
    def _shell_command(self):
        self.output = subprocess.check_output(self.command, shell=True,cwd=self.cwd)
        return self.output
    def _execute_and_return(self):
        split_command = self.command.split()
        # windows limitation
        shell_commands = ["dir"]
        if split_command[0] in shell_commands:
            return self._shell_command()
        else:
            self.stdout = ""
            self.stderr = ""
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
            return self.stdout, self.stderr
    def _start_and_return_pid(self):
        raise RuntimeError
    def run(self):
        if self.bg == True:
            return self._start_and_return_pid()
        else:
            return self._execute_and_return()
        

            
