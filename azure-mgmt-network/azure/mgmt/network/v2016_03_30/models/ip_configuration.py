# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class IPConfiguration(SubResource):
    """IPConfiguration.

    :param id: Resource Id
    :type id: str
    :param private_ip_address: Gets or sets the privateIPAddress of the IP
     Configuration
    :type private_ip_address: str
    :param private_ip_allocation_method: Gets or sets PrivateIP allocation
     method (Static/Dynamic). Possible values include: 'Static', 'Dynamic'
    :type private_ip_allocation_method: str or :class:`IPAllocationMethod
     <azure.mgmt.network.v20160330.models.IPAllocationMethod>`
    :param subnet: Gets or sets the reference of the subnet resource
    :type subnet: :class:`Subnet <azure.mgmt.network.v20160330.models.Subnet>`
    :param public_ip_address: Gets or sets the reference of the PublicIP
     resource
    :type public_ip_address: :class:`PublicIPAddress
     <azure.mgmt.network.v20160330.models.PublicIPAddress>`
    :param provisioning_state: Gets or sets Provisioning state of the
     PublicIP resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'private_ip_address': {'key': 'properties.privateIPAddress', 'type': 'str'},
        'private_ip_allocation_method': {'key': 'properties.privateIPAllocationMethod', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'Subnet'},
        'public_ip_address': {'key': 'properties.publicIPAddress', 'type': 'PublicIPAddress'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, private_ip_address=None, private_ip_allocation_method=None, subnet=None, public_ip_address=None, provisioning_state=None, name=None, etag=None):
        super(IPConfiguration, self).__init__(id=id)
        self.private_ip_address = private_ip_address
        self.private_ip_allocation_method = private_ip_allocation_method
        self.subnet = subnet
        self.public_ip_address = public_ip_address
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
