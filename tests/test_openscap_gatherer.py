from openscap_gatherer.openscap_gatherer import OpenscapGatherer


class TestOpenscapGatherer:

    def test_read_config(self):
        gatherer = OpenscapGatherer('./tests/insights_file.sample.conf')
        config = gatherer.read_config()
        real_config = {
            'policy_uuid': '7f372d76-1f01-4031-ab03-7d81e5da181e',
            'profile': 'xccdf_org.ssgproject.content_profile_common',
            'content_path': '/usr/share/xml/scap/ssg/fedora/ssg-fedora-ds.xml'
        }
        assert('7f372d76-1f01-4031-ab03-7d81e5da181e' == gatherer.policy_uuid)
        assert('xccdf_org.ssgproject.content_profile_common' ==
               gatherer.profile)
        assert('/usr/share/xml/scap/ssg/fedora/ssg-fedora-ds.xml' ==
               gatherer.content_path)
        assert(real_config == config)
