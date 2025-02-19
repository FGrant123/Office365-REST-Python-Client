from office365.entity_collection import EntityCollection
from office365.onedrive.termstore.groups.group import Group


class GroupCollection(EntityCollection):

    def __init__(self, context, resource_path=None):
        super(GroupCollection, self).__init__(context, Group, resource_path)

    def add(self, display_name):
        """
        Create a new group object in a term store.

        :param str display_name: Name of the group to be created.
        :rtype: Group
        """
        props = {"displayName": display_name}
        return super(GroupCollection, self).add(**props)

    def get_by_name(self, name):
        """Returns the group with the specified name.

        :param str name: Group name
        :rtype: Group
        """
        return self._find_by_unique_prop("displayName", name)
