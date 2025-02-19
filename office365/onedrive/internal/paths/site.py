from office365.runtime.paths.entity import EntityPath
from office365.runtime.compat import urlparse, is_absolute_url
from office365.runtime.paths.resource_path import ResourcePath


class SitePath(EntityPath):
    """Resource path for addressing Site resource"""

    @property
    def segments(self):
        if is_absolute_url(self.key):
            url_result = urlparse(self.key)
            return [self.delimiter, url_result.hostname, ":", url_result.path]
        else:
            return super(SitePath, self).segments

    @property
    def collection(self):
        if self._collection is None:
            self._collection = ResourcePath("sites")
        return self._collection
