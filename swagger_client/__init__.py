# coding: utf-8

"""


    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version:

    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into sdk package
from .models.types_uid import TypesUID
from .models.v1_api_resource import V1APIResource
from .models.v1_api_resource_list import V1APIResourceList
from .models.v1_address import V1Address
from .models.v1_alias import V1Alias
from .models.v1_bios import V1BIOS
from .models.v1_ballooning import V1Ballooning
from .models.v1_band_width import V1BandWidth
from .models.v1_boot import V1Boot
from .models.v1_boot_menu import V1BootMenu
from .models.v1_boot_order import V1BootOrder
from .models.v1_channel import V1Channel
from .models.v1_channel_source import V1ChannelSource
from .models.v1_channel_target import V1ChannelTarget
from .models.v1_clock import V1Clock
from .models.v1_cloud_init_data_source_no_cloud import V1CloudInitDataSourceNoCloud
from .models.v1_cloud_init_spec import V1CloudInitSpec
from .models.v1_console import V1Console
from .models.v1_console_target import V1ConsoleTarget
from .models.v1_devices import V1Devices
from .models.v1_disk import V1Disk
from .models.v1_disk_auth import V1DiskAuth
from .models.v1_disk_driver import V1DiskDriver
from .models.v1_disk_secret import V1DiskSecret
from .models.v1_disk_source import V1DiskSource
from .models.v1_disk_source_host import V1DiskSourceHost
from .models.v1_disk_target import V1DiskTarget
from .models.v1_domain_spec import V1DomainSpec
from .models.v1_entry import V1Entry
from .models.v1_filter_ref import V1FilterRef
from .models.v1_graphics import V1Graphics
from .models.v1_initializer import V1Initializer
from .models.v1_initializers import V1Initializers
from .models.v1_interface import V1Interface
from .models.v1_interface_source import V1InterfaceSource
from .models.v1_interface_target import V1InterfaceTarget
from .models.v1_link_state import V1LinkState
from .models.v1_list_meta import V1ListMeta
from .models.v1_listen import V1Listen
from .models.v1_mac import V1MAC
from .models.v1_memory import V1Memory
from .models.v1_migration import V1Migration
from .models.v1_migration_list import V1MigrationList
from .models.v1_migration_spec import V1MigrationSpec
from .models.v1_migration_status import V1MigrationStatus
from .models.v1_model import V1Model
from .models.v1_os import V1OS
from .models.v1_os_type import V1OSType
from .models.v1_object_meta import V1ObjectMeta
from .models.v1_owner_reference import V1OwnerReference
from .models.v1_read_only import V1ReadOnly
from .models.v1_sm_bios import V1SMBios
from .models.v1_serial import V1Serial
from .models.v1_serial_target import V1SerialTarget
from .models.v1_status import V1Status
from .models.v1_status_cause import V1StatusCause
from .models.v1_status_details import V1StatusDetails
from .models.v1_sys_info import V1SysInfo
from .models.v1_vm_condition import V1VMCondition
from .models.v1_vm_graphics import V1VMGraphics
from .models.v1_vm_selector import V1VMSelector
from .models.v1_vm_spec import V1VMSpec
from .models.v1_vm_status import V1VMStatus
from .models.v1_video import V1Video
from .models.v1_virtual_machine import V1VirtualMachine
from .models.v1_virtual_machine_list import V1VirtualMachineList

# import apis into sdk package
from .apis.apiskubevirtiovalpha_api import ApiskubevirtiovalphaApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
