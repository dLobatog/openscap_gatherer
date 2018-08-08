from openscap_gatherer.uploader import Uploader
from openscap_gatherer.uploader import NoFilesAvailable
from tarfile import TarFile
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

    @mock.patch.object(TarFile, 'add')
    @mock.patch('tarfile.open')
    def test_zip_creates_tar_file(self, mocked_add, tarfile_open):
    #def test_zip_creates_tar_file(self, tarfile_open):
        uploader = Uploader(
            ['/tmp/filepath1', '/tmp/filepath2', '/tmp/filepath3'],
            '/tmp/openscap_gatherer/results.xml',
            ''
        )
        uploader.zip()
        mocked_add.assert_called_once_with('/tmp/filepath1')
        tarfile_open.assert_called_once_with('/tmp/openscap_gatherer/results.xml.tar.gz',
                                             'w:gz')
