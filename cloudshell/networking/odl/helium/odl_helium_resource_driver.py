import inject

from cloudshell.networking.generic_bootstrap import NetworkingGenericBootstrap
from cloudshell.networking.networking_resource_driver_interface import NetworkingResourceDriverInterface
from cloudshell.shell.core.context_utils import context_from_args
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.driver_utils import GlobalLock

import cloudshell.networking.odl.helium.odl_helium_configuration as driver_config

from cloudshell.networking.sdn.controller.controller_connection_handler import SDNController

class ODLHeliumResourceDriver(ResourceDriverInterface, NetworkingResourceDriverInterface, GlobalLock):
    def __init__(self):
        super(ODLHeliumResourceDriver, self).__init__()
        bootstrap = NetworkingGenericBootstrap()
        bootstrap.add_config(driver_config)
        bootstrap.initialize()


    @context_from_args
    def initialize(self, context):
        """Initialize method
        :type context: cloudshell.shell.core.context.driver_context.InitCommandContext
        """

        return 'Finished initializing'



    def cleanup(self):
        pass
#
    def restore(self):pass
    def save(self):pass
    def send_custom_command(self):pass
    def send_custom_config_command(self):pass
    def shutdown(self):pass
    def update_firmware(self):pass
    @context_from_args

    def Install_Static_Flows(self, context, flow_name, switch_id,port):
        static_flow = driver_config.STATIC_FLOW()
        response = static_flow.static_flow_pusher(flow_name, switch_id,port)

        return response

    @context_from_args
    def get_inventory(self, context):
        """Return device structure with all standard attributes

        :return: response
        :rtype: string
        """

        autoload_operations = inject.instance("autoload_operations")
        response = autoload_operations.discover()
        autoload_operations.logger.info('Autoload completed')

        return response



    @context_from_args
    def ApplyConnectivityChanges(self, context, request):
        connectivity_operations = inject.instance('connectivity_operations')

        return ""
