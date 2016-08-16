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

from msrest.serialization import Model


class StorageAccountListKeysResult(Model):
    """The ListKeys operation response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar keys: Gets the list of account keys and their properties.
    :vartype keys: list of :class:`StorageAccountKey
     <azure.mgmt.storage.v20160101.models.StorageAccountKey>`
    """ 

    _validation = {
        'keys': {'readonly': True},
    }

    _attribute_map = {
        'keys': {'key': 'keys', 'type': '[StorageAccountKey]'},
    }

    def __init__(self):
        self.keys = None
