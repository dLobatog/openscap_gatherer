from openscap_gatherer.openscap_gatherer import OpenscapGatherer


class TestOpenscapGatherer:

    def test_read_config(self):
        gatherer = OpenscapGatherer('./tests/insights_file.sample.conf')
        config = gatherer.read_config()
        real_config = {
            u'policy_uuid': u'7f372d76-1f01-4031-ab03-7d81e5da181e',
            u'profile': u'xccdf_org.ssgproject.content_profile_standard',
            u'content_path': u'/usr/share/xml/scap/ssg/content/'
            'ssg-fedora-ds.xml',
            u'tailoring_path': u''
        }
        assert('7f372d76-1f01-4031-ab03-7d81e5da181e' == gatherer.policy_uuid)
        assert('xccdf_org.ssgproject.content_profile_standard' ==
               gatherer.profile)
        assert('/usr/share/xml/scap/ssg/content/ssg-fedora-ds.xml' ==
               gatherer.content_path)
        assert('' == gatherer.tailoring_path)
        assert(real_config == config)
