from openscap_gatherer.runner import Runner
from openscap_gatherer.runner import RunnerError
import re
import pytest


class TestRunner:

    def test_run_creates_basic_command(self):
        runner = Runner(
            {
                'profile': 'foo',
                'dirpath': '/tmp/insights-compliance',
                'content_path':
                '/usr/share/xml/scap/ssg/fedora/ssg-fedora-ds.xml'
            }
        )
        expected_command = re.compile(
            "oscap xccdf eval --profile foo --results-arf "
            "/tmp/insights-compliance/\d+.xml "
            "/usr/share/xml/scap/ssg/fedora/ssg-fedora-ds.xml"
        )
        assert re.match(expected_command, runner.scan_command())

    def test_run_does_not_pass_profile_if_undefined(self):
        runner = Runner(
            {
                'profile': '',
                'dirpath': '/tmp/insights-compliance',
                'content_path':
                '/usr/share/xml/scap/ssg/fedora/ssg-fedora-ds.xml'
            }
        )
        expected_command = re.compile(
            "oscap xccdf eval --results-arf "
            "/tmp/insights-compliance/\d+.xml "
            "/usr/share/xml/scap/ssg/fedora/ssg-fedora-ds.xml"
        )
        assert re.match(expected_command, runner.scan_command())

    def test_run_does_not_work_without_content_path(self):
        runner = Runner(
            {
                'profile': '',
                'dirpath': '/tmp/insights-compliance',
                'content_path': ''
            }
        )
        with pytest.raises(RunnerError) as e_info:
            runner.scan_command()
        assert 'without content_path' in str(e_info)

#    def test_scan_shells_out(self):
#        runner = Runner(
#            {
#                'profile': 'foo',
#                'dirpath': '/tmp/insights-compliance',
#                'content_path':
#                '/usr/share/xml/scap/ssg/fedora/ssg-fedora-ds.xml'
#            }
#        )
#        runner.scan()
