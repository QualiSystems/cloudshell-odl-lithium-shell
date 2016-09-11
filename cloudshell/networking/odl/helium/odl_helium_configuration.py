import re
from cloudshell.networking.sdn.autoload.sdn_generic_snmp_autoload import SDNGenericSNMPAutoload
from cloudshell.networking.sdn.static_flows.static_flows_configuration import InstallStaticFlows
from cloudshell.shell.core.context_utils import get_decrypted_password_by_attribute_name_wrapper, \
    get_attribute_by_name_wrapper
from cloudshell.shell.core.dependency_injection.context_based_logger import get_logger_with_thread_id




SUPPORTED_OPENFLOW = ['1.0','1.3']



CONNECTIVITY_OPERATIONS_CLASS = ''
CONFIGURATION_OPERATIONS_CLASS = ''
FIRMWARE_OPERATIONS_CLASS = ''
AUTOLOAD_OPERATIONS_CLASS = SDNGenericSNMPAutoload
SEND_COMMAND_OPERATIONS_CLASS = ''
CONTOLLER_HANDLER = 'controller_handler'
STATIC_FLOW = InstallStaticFlows


GET_LOGGER_FUNCTION = get_logger_with_thread_id
POOL_TIMEOUT = 300
