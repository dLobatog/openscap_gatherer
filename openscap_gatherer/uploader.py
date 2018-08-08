import tarfile
import os


class Uploader:
    """ Service to zip results (arbitrary files) and upload them
    to a certain URL
    """

    def __init__(self, files, results_path, url, debug=False):
        self.files = files
        self.results_path = results_path
        self.debug = debug

    def zipped_filepath(self):
        return(self.results_path + '.tar.gz')

    def zip(self):
        if not self.files:
            no_files_message = (
                'Files are not available. They might be unreadable by the '
                'current process or the path might not exist.'
            )
            raise(NoFilesAvailable(self, msg=no_files_message))

        tar = tarfile.open(self.zipped_filepath(), 'w:gz')
        try:
            for report in self.files:
                tar.add(report, arcname=os.path.basename(report))
        finally:
            tar.close()


class UploaderError(Exception):
    """ Basic exception for problems raised by the uploader """

    def __init__(self, uploader, msg=None):
        if msg is None:
            # Set some default useful error message
            msg = "An error occured with uploader %s" % uploader
        super(UploaderError, self).__init__(msg)
        self.uploader = uploader


class NoFilesAvailable(UploaderError):
    pass
