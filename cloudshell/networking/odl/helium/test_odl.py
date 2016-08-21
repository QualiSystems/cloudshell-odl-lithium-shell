#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails,ConnectivityContext
from cloudshell.networking.odl.helium.odl_helium_resource_driver import ODLHeliumResourceDriver
import re


def create_context():
    context = ResourceCommandContext()
    context.resource = ResourceContextDetails()
    context.resource.name = 'odl1'
    context.reservation = ReservationContextDetails()
    context.reservation.reservation_id = '5695cf87-a4f3-4447-a08a-1a99a936010e'
    context.reservation.owner_user = 'admin'
    context.reservation.owner_email = 'fake@qualisystems.com'
    context.reservation.environment_path ='Environment-6-7-2016 15-25'
    context.reservation.environment_name = 'Environment-6-7-2016 15-25'
    context.reservation.domain = 'Global'
    context.resource.attributes = {}

    context.resource.attributes['User'] = 'admin'
    context.resource.attributes['AdminUser'] = 'admin'

    context.resource.attributes['Password'] = 'admin'

    context.resource.address = '192.168.42.203'
    context.resource.port = '8080'

    context.resource.attributes['Model'] = 'OpenDayLight Helium'
    context.resource.attributes['AdminPassword'] ='admin'
    context.resource.attributes['Vendor'] = 'OpenDayLight'
    return context



if __name__ == '__main__':
    context = create_context()
    driver = ODLHeliumResourceDriver()
    #Error: File can't be found "flash:/test".
    #response = driver.get_inventory(context)
    #res = driver.save(context, 'tftp://82.80.35.226', 'startup')

    res = driver.get_inventory(context)
    #
    #res = driver.save(context, 'flash:/config_backup/','startup')
    #C:/Users/Administrator/Desktop/test
    #tftp://12.30.245.98/test/test.txt
    #res = driver.restore(context,'flash:/config_backup/vrpcfg.zip', 'startup', 'override')

    #response = driver.get_inventory(context)
    #res = driver.save(context, 'tftp://82.80.35.226/test', 'startup')

    #res = driver.ApplyConnectivityChanges(context, request)
    print res
    #res=driver.update_firmware(context,'1.1.1.1','flash:/config_backup/')
    #print driver.send_custom_command(context, "display version")
    # print response


'''context:



resource.attributes=
{'CLI Connection Type': 'SSH', 'Enable Password': 'PgkOScppedeEbHGHdzpnrw==', 'NAT_Value_ManagementNetwork': '',
'System Name': '172.19.0.36', 'Console User': '', 'Location': 'Beijing China', 'OS Version': '5.160', 'Console Password': '3M3u7nkDzxWb0aJ/IZYeWw==',
'Power Management': 'False', 'Vendor': 'huawei', 'AdminUser': 'admin', 'Backup Location': '', 'Sessions Concurrency Limit': '1', 'User': 'telnet',
 'Password': 'PgkOScppedeEbHGHdzpnrw==', 'SNMP Version': '2', 'BaselineGroup': '0', 'Contact Name': 'R&D Beijing, huawei Technologies co.,Ltd.', 'SNMP V3 Private Key': '',
 'SNMP Read Community': 'esdkr0key', 'SNMP V3 Password': '', 'Model': 'Enterprises.2011.2.23.339', 'Console Port': '0', 'GuacServer': '', 'AdminPassword': 'DxTbqlSgAVPmrDLlHvJrsA==',
 'Console Server IP Address': '', 'BaselineConfigFilename': '', 'SNMP V3 User': '', 'SNMP Write Community': 'esdkw0key'}


reservation=
 reservation_id = {str} '5695cf87-a4f3-4447-a08a-1a99a936010e'
owner_user = {str} 'admin'
owner_email = {str} 'fake@qualisystems.com'
environment_path = {str} 'Environment-6-7-2016 15-25'
environment_name = {str} 'Environment-6-7-2016 15-25'
domain = {str} 'Global'
description = {NoneType} None

connectivity=

admin_auth_token = {str} 'T1dkw4LLJUSmWDpolusJdw=='
cloudshell_api_port = {str} '8029'
quali_api_port = {str} '9000'
server_address = {str} 'localhost'

description=
description = {NoneType} None
family = {str} 'Router'
fullname = {str} 'Huawei37'
id = {str} 'b476fa1f-379e-435a-b35c-65e892e1c306'
model = {str} 'Huaewi VRP Router'
name = {str} 'Huawei37'
type = {str} 'Resource'
'''