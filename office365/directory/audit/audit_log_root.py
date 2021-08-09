from office365.directory.audit.directory_audit import DirectoryAudit
from office365.directory.audit.provisioningObjectSummary import ProvisioningObjectSummary
from office365.directory.audit.signIn import SignIn
from office365.entity import Entity
from office365.entity_collection import EntityCollection
from office365.runtime.resource_path import ResourcePath


class AuditLogRoot(Entity):
    """Contains different types of audit logs. This resources returns a singleton auditLog resource.
    It doesn't contain any usable properties.
    """

    @property
    def directory_audits(self):
        """
        Get the list of audit logs generated by Azure Active Directory. This includes audit logs generated
        by various services within Azure AD, including user, app, device and group Management,
        privileged identity management (PIM), access reviews, terms of use, identity protection,
        password management (self-service and admin password resets), and self- service group management, and so on.

        :rtype: EntityCollection
        """
        return self.get_property('directoryAudits',
                                 EntityCollection(self.context, DirectoryAudit,
                                                  ResourcePath("directoryAudits", self.resource_path)))

    @property
    def signins(self):
        """
        Retrieve the Azure AD user sign-ins for your tenant. Sign-ins that are interactive in nature
        (where a username/password is passed as part of auth token) and successful federated sign-ins are currently
        included in the sign-in logs. The maximum and default page size is 1,000 objects and by default,
        the most recent sign-ins are returned first.

        :rtype: EntityCollection
        """
        return self.get_property('signIns',
                                 EntityCollection(self.context, SignIn, ResourcePath("signIns", self.resource_path)))

    @property
    def provisioning(self):
        """
        Get all provisioning events that occurred in your tenant, such as the deletion of a group in
        a target application or the creation of a user when provisioning user accounts from your HR system.

        :rtype: EntityCollection
        """
        return self.get_property('provisioning',
                                 EntityCollection(self.context, ProvisioningObjectSummary,
                                                  ResourcePath("provisioning", self.resource_path)))

    def get_property(self, name, default_value=None):
        if default_value is None:
            property_mapping = {
                "directoryAudits": self.directory_audits
            }
            default_value = property_mapping.get(name, None)
        return super(AuditLogRoot, self).get_property(name, default_value)