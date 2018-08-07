from __future__ import print_function
import tempfile
import time
import subprocess


class Runner:
    """This class deals with creating the command for
    the OpenSCAP run and actually running it, checking it did not
    fail, etcetera
    """

    def __init__(self, options, debug=False):
        self.debug = debug
        self.profile = options['profile']
        self.content_path = options['content_path']
        self.timestamp = int(time.time())
        if 'dirpath' in options:
            self.dirpath = options['dirpath']
        else:
            self.dirpath = tempfile.mkdtemp()

    def results_path(self):
        return self.dirpath + '/' + str(self.timestamp) + '.xml'

    def scan_command(self):
        command = 'oscap xccdf eval '
        if self.profile:
            command += ('--profile ' + self.profile + ' ')

        command += ('--results-arf ' + self.results_path() + ' ')
        if self.content_path:
            command += self.content_path
        else:
            raise(RunnerError(self, "Cannot scan without content_path"))
        if self.debug:
            print("[openscap_gatherer] - Running command - ", command)
        return command

    def scan(self):
        process = subprocess.Popen(self.scan_command().split(' '),
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        if self.debug:
            for stdout_line in iter(process.stdout.readline, ""):
                print(stdout_line, end='')

            process.stdout.close()
            errcode = process.wait()
        else:
            # wait for the process to terminate
            out, err = process.communicate()
            errcode = process.returncode

        if (errcode == 0 or errcode == 2):
            if self.debug:
                print("[openscap_gatherer] - Saved report at ", self.dirpath)
            return((True, out, err))
        else:
            if self.debug:
                print("[openscap_gatherer] - Report failed: status ", errcode)
                print("[openscap_gatherer] - stdout: ", out)
                print("[openscap_gatherer] - stderr: ", err)
            return((False, out, err))


class RunnerError(Exception):
    """ Basic exception for problems raised by the runner """

    def __init__(self, runner, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = "An error occured with runner %s" % runner
        super(RunnerError, self).__init__(msg)
        self.runner = runner
