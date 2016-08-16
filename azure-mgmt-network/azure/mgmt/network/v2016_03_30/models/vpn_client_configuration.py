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


class VpnClientConfiguration(Model):
    """VpnClientConfiguration for P2S client.

    :param vpn_client_address_pool: Gets or sets the reference of the Address
     space resource which represents Address space for P2S VpnClient.
    :type vpn_client_address_pool: :class:`AddressSpace
     <azure.mgmt.network.v20160330.models.AddressSpace>`
    :param vpn_client_root_certificates: VpnClientRootCertificate for Virtual
     network gateway.
    :type vpn_client_root_certificates: list of
     :class:`VpnClientRootCertificate
     <azure.mgmt.network.v20160330.models.VpnClientRootCertificate>`
    :param vpn_client_revoked_certificates: VpnClientRevokedCertificate for
     Virtual network gateway.
    :type vpn_client_revoked_certificates: list of
     :class:`VpnClientRevokedCertificate
     <azure.mgmt.network.v20160330.models.VpnClientRevokedCertificate>`
    """ 

    _attribute_map = {
        'vpn_client_address_pool': {'key': 'vpnClientAddressPool', 'type': 'AddressSpace'},
        'vpn_client_root_certificates': {'key': 'vpnClientRootCertificates', 'type': '[VpnClientRootCertificate]'},
        'vpn_client_revoked_certificates': {'key': 'vpnClientRevokedCertificates', 'type': '[VpnClientRevokedCertificate]'},
    }

    def __init__(self, vpn_client_address_pool=None, vpn_client_root_certificates=None, vpn_client_revoked_certificates=None):
        self.vpn_client_address_pool = vpn_client_address_pool
        self.vpn_client_root_certificates = vpn_client_root_certificates
        self.vpn_client_revoked_certificates = vpn_client_revoked_certificates
