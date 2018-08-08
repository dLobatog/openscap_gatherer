from openscap_gatherer.uploader import Uploader
from openscap_gatherer.uploader import NoFilesAvailable
import pytest
import mock


class TestUploader:

    def test_zipped_filepath_is_results_path_plus_targz(self):
        uploader = Uploader([], '/tmp/openscap_gatherer/results.xml', '')
        assert('/tmp/openscap_gatherer/results.xml.tar.gz' ==
               uploader.zipped_filepath())

    def test_does_not_create_zippedfile_with_no_files_or_path(self):
        uploader = Uploader([], '/tmp/openscap_gatherer/results.xml', '')
        with pytest.raises(NoFilesAvailable) as e_info:
            uploader.zip()
        assert 'Files are not available' in str(e_info)
        assert 'might not exist' in str(e_info)
        assert 'unreadable' in str(e_info)

    @mock.patch('tarfile.open')
    def test_zip_creates_tar_file(self, tarfile_open):
        uploader = Uploader(
            ['/tmp/filepath1', '/tmp/filepath2', '/tmp/filepath3'],
            '/tmp/openscap_gatherer/results.xml',
            ''
        )
        tar_mock = mock.Mock()
        tarfile_open.return_value = tar_mock
        with mock.patch.object(tar_mock, 'add') as tar_add_mock:
            uploader.zip()
            tar_add_mock.assert_any_call('/tmp/filepath1', arcname='filepath1')
            tar_add_mock.assert_any_call('/tmp/filepath2', arcname='filepath2')
            tar_add_mock.assert_any_call('/tmp/filepath3', arcname='filepath3')

        tarfile_open.assert_called_once_with(
            '/tmp/openscap_gatherer/results.xml.tar.gz',
            'w:gz'
        )
