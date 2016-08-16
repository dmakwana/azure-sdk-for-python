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


class TagDetails(Model):
    """Tag details.

    :param id: The tag ID.
    :type id: str
    :param tag_name: The tag name.
    :type tag_name: str
    :param count: The tag count.
    :type count: :class:`TagCount
     <azure.mgmt.resource.resources.v20160701.models.TagCount>`
    :param values: The list of tag values.
    :type values: list of :class:`TagValue
     <azure.mgmt.resource.resources.v20160701.models.TagValue>`
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'tag_name': {'key': 'tagName', 'type': 'str'},
        'count': {'key': 'count', 'type': 'TagCount'},
        'values': {'key': 'values', 'type': '[TagValue]'},
    }

    def __init__(self, id=None, tag_name=None, count=None, values=None):
        self.id = id
        self.tag_name = tag_name
        self.count = count
        self.values = values
