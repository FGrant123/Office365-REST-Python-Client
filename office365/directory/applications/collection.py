from office365.delta_collection import DeltaCollection
from office365.directory.applications.application import Application


class ApplicationCollection(DeltaCollection):
    """DirectoryObject's collection"""

    def __init__(self, context, resource_path=None):
        super(ApplicationCollection, self).__init__(context, Application, resource_path)

    def get_by_app_id(self, app_id):
        """Retrieves application by Application client identifier

        :param str app_id: Application client identifier

        :rtype: Application
        """
        return self._find_by_unique_prop("appId", app_id)
