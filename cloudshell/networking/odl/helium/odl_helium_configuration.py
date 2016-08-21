import re
from cloudshell.networking.sdn.autoload.sdn_generic_snmp_autoload import SDNGenericSNMPAutoload
from cloudshell.networking.huawei.huawei_configuration_operations import HuaweiConfigurationOperations
from cloudshell.networking.huawei.huawei_connectivity_operations import HuaweiConnectivityOperations
from cloudshell.networking.huawei.huawei_send_command_operations import HuaweiSendCommandOperations
from cloudshell.shell.core.context_utils import get_decrypted_password_by_attribute_name_wrapper, \
    get_attribute_by_name_wrapper
from cloudshell.shell.core.dependency_injection.context_based_logger import get_logger_with_thread_id
from cloudshell.networking.sdn.configuration.cloudshell_controller_configuration import create_controller_handler



BASE_URL = '/controller/nb/v2'



SUPPORTED_OPENFLOW = ['1.0','1.3']



CONNECTIVITY_OPERATIONS_CLASS = HuaweiConnectivityOperations
CONFIGURATION_OPERATIONS_CLASS = HuaweiConfigurationOperations
FIRMWARE_OPERATIONS_CLASS = HuaweiConfigurationOperations
AUTOLOAD_OPERATIONS_CLASS = SDNGenericSNMPAutoload
SEND_COMMAND_OPERATIONS_CLASS = HuaweiSendCommandOperations
CONTOLLER_HANDLER = 'controller_handler'


GET_LOGGER_FUNCTION = get_logger_with_thread_id
POOL_TIMEOUT = 300
