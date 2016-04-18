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
        

def shell_ex(cmd, print_output=True, outputfile=None, outerrfile=None):
    """
    Executes a command and returns the exitcode, stdout output and stderr output
    """
    print "shell_ex - running '%s'" % cmd
    if outputfile and not outerrfile:
        outerrfile = '%s.err%s' % os.path.splitext(outputfile)
    import subprocess
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    exitcode = p.returncode
    print "Return code: %d" % exitcode
    if print_output:
        print "-------- stdout:"
        if stdout: print stdout
        print "-------- stderr:"
        if stderr: print stderr
        print "--------"
    if outputfile:
        try:
            with open(outputfile, 'w') as f:
                f.write(stdout)
        except:
            print "Failed to write stdout output to '%s'" % outputfile
    if outerrfile:
        try:
            with open(outerrfile, 'w') as f:
                f.write(stderr)
        except:
            print "Failed to write stderr output to '%s'" % outerrfile
    return exitcode, stdout, stderr            


def popen_improved(command, shell_cmd=False, print_output=False):
    """
    Parameters
    ----------
    command : array
        array holding each element of the command line to run e.g. ["npm",\
         "install"], ["npm","--version"]
    shell_cmd : bool, optional
        is the command a shell built-in and will it use env vars. Don't use\
         on POSIX.
        Windows only.
        e.g. for "set", or "dir", or "where"
    print_output : bool, optional
        print output, err, exit_code to stdout of current process
    Returns object with output, err, exit_code properties
    """
    class PopenReturn(object):
        """
        Attributes
        ----------
        err : string
            stderr from process, stripped
        exit_code : int
            exit_code from process, stripped
        output : string
            stdout from process, stripped
        """
        def __init__(self, output, err, exit_code):
            super(PopenReturn, self).__init__()
            self.output = output
            self.err = err
            self.exit_code = exit_code
    if print_output:
        logger.info("EXECUTING '{}'".format(" ".join(command)))
    process = Popen(command, stdout=PIPE, stderr=PIPE, shell=shell_cmd)
    output = ""
    err = ""
    for line in process.stdout.readlines():
        output += line
    for error_line in process.stderr.readlines():
        err += error_line
    exit_code = process.wait()
    if print_output:
        logger.info("OUTPUT: {}".format(output))
        logger.info("ERR: {}".format(err))
        logger.info("EXIT CODE: {}".format(exit_code))
    return PopenReturn(output.strip(), err.strip(), exit_code)
