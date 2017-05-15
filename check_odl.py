#!/usr/bin/python
# -*- coding: utf-8 -*-
from __driver import ODLHeliumResourceDriver

from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails, \
    ConnectivityContext


def create_context():
    context = ResourceCommandContext()
    context.connectivity = ConnectivityContext()
    context.connectivity.server_address = "192.168.85.7"
    context.connectivity.cloudshell_api_port = 8029
    context.connectivity.admin_auth_token = ""

    context.resource = ResourceContextDetails()
    context.resource.name = 'odl1'
    context.reservation = ReservationContextDetails()
    context.reservation.reservation_id = '5695cf87-a4f3-4447-a08a-1a99a936010e'
    context.reservation.owner_user = 'admin'
    context.reservation.owner_email = 'fake@qualisystems.com'
    context.reservation.environment_path = 'Environment-6-7-2016 15-25'
    context.reservation.environment_name = 'Environment-6-7-2016 15-25'
    context.reservation.domain = 'Global'
    context.resource.attributes = {}

    context.resource.attributes['User'] = 'admin'
    context.resource.attributes['AdminUser'] = 'admin'

    context.resource.attributes['Password'] = 'DxTbqlSgAVPmrDLlHvJrsA=='

    context.resource.address = '192.168.42.157'
    context.resource.attributes['Port'] = '8080'

    context.resource.attributes['Model'] = 'OpenDayLight Helium'
    context.resource.attributes['AdminPassword'] = 'admin'
    context.resource.attributes['Vendor'] = 'OpenDayLight'
    return context


'''
    nodeid = '00:00:00:00:00:00:00:02'
    port = 1
    ether_type = 0x800
    dst_mac = '00:00:00:00:00:02'
    dst_ip = '10.0.0.1'
    src_ip = '10.0.0.4'
    fname = 'test11113'
    '''

if __name__ == '__main__':
    context = create_context()
    driver = ODLHeliumResourceDriver()
    # res = driver.get_inventory(context)
    # print "EXIT script"
    # import ipdb;ipdb.set_trace()
    # import sys;sys.exit(0)
    # res = driver.Install_Static_Flows(context, 'sw2p1', '00:00:00:00:00:00:00:02', 1)
    # res = driver.Install_Static_Flows(context, 'sw3p1', '00:00:00:00:00:00:00:03', 1)


    """ "eth1" address us 479889742"""
    """ ""SDN Switch 479889733" address is 479889733"""
    "SDN Switch 479889733/eth1"

    request = """{"driverRequest": {"actions": [{"connectionId": "09faa654-9189-4b99-973c-01f5222f1db9",
                                              "connectionParams": {"vlanId": "2", "mode": "Access",
                                                                   "vlanServiceAttributes": [
                                                                       {"attributeName": "Allocation Ranges",
                                                                        "attributeValue": "2-4094",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Isolation Level",
                                                                        "attributeValue": "Exclusive",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Access Mode",
                                                                        "attributeValue": "Access",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "VLAN ID",
                                                                        "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Pool Name",
                                                                        "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Virtual Network",
                                                                        "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Default VLAN",
                                                                        "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "QnQ",
                                                                        "attributeValue": "False",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "CTag", "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"}],
                                                                   "type": "setVlanParameter"}, "connectorAttributes": [
            {"attributeName": "Selected Network", "attributeValue": "2", "type": "connectorAttribute"}],
                                              "actionId": "09faa654-9189-4b99-973c-01f5222f1db9_103b5867-caec-4c78-a891-90ae750098c4",
                                              "actionTarget": {"fullName": "SDN ODL2/SDN Switch 479889733/eth1",
                                                               "fullAddress": "192.168.42.157/00:00:00:00:00:00:00:02/1",
                                                               "type": "actionTarget"}, "customActionAttributes": [],
                                              "type": "setVlan"},
                                             {"connectionId": "09faa654-9189-4b99-973c-01f5222f1db9",
                                              "connectionParams": {"vlanId": "2", "mode": "Access",
                                                                   "vlanServiceAttributes": [
                                                                       {"attributeName": "Allocation Ranges",
                                                                        "attributeValue": "2-4094",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Isolation Level",
                                                                        "attributeValue": "Exclusive",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Access Mode",
                                                                        "attributeValue": "Access",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "VLAN ID",
                                                                        "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Pool Name",
                                                                        "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Virtual Network",
                                                                        "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "Default VLAN",
                                                                        "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "QnQ",
                                                                        "attributeValue": "False",
                                                                        "type": "vlanServiceAttribute"},
                                                                       {"attributeName": "CTag", "attributeValue": "",
                                                                        "type": "vlanServiceAttribute"}],
                                                                   "type": "setVlanParameter"}, "connectorAttributes": [
                                                 {"attributeName": "Selected Network", "attributeValue": "2",
                                                  "type": "connectorAttribute"}],
                                              "actionId": "09faa654-9189-4b99-973c-01f5222f1db9_884f8bbc-7984-4db6-ae10-574cfa7b31b2",
                                              "actionTarget": {"fullName": "SDN ODL2/SDN Switch 479889734/eth3",
                                                               "fullAddress": "192.168.42.157/00:00:00:00:00:00:00:03/1",
                                                               "type": "actionTarget"}, "customActionAttributes": [],
                                              "type": "setVlan"}]}}"""

    res = driver.ApplyConnectivityChanges(context, request)

    print res
