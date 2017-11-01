# kubevirt.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**console**](DefaultApi.md#console) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name}/console | Open a websocket connection to a serial console on the specified VM.
[**create_namespaced_migration**](DefaultApi.md#create_namespaced_migration) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/migrations | Create a Migration object.
[**create_namespaced_virtual_machine**](DefaultApi.md#create_namespaced_virtual_machine) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines | Create a VirtualMachine object.
[**create_namespaced_virtual_machine_replica_set**](DefaultApi.md#create_namespaced_virtual_machine_replica_set) | **POST** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets | Create a VirtualMachineReplicaSet object.
[**delete_namespaced_migration**](DefaultApi.md#delete_namespaced_migration) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/migrations/{name} | Delete a Migration object.
[**delete_namespaced_virtual_machine**](DefaultApi.md#delete_namespaced_virtual_machine) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name} | Delete a VirtualMachine object.
[**delete_namespaced_virtual_machine_replica_set**](DefaultApi.md#delete_namespaced_virtual_machine_replica_set) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets/{name} | Delete a VirtualMachineReplicaSet object.
[**deletecollection_namespaced_migration**](DefaultApi.md#deletecollection_namespaced_migration) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/migrations | Delete a collection of Migration objects.
[**deletecollection_namespaced_virtual_machine**](DefaultApi.md#deletecollection_namespaced_virtual_machine) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines | Delete a collection of VirtualMachine objects.
[**deletecollection_namespaced_virtual_machine_replica_set**](DefaultApi.md#deletecollection_namespaced_virtual_machine_replica_set) | **DELETE** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets | Delete a collection of VirtualMachineReplicaSet objects.
[**func1**](DefaultApi.md#func1) | **GET** /apis/kubevirt.io |
[**get_api_resources**](DefaultApi.md#get_api_resources) | **GET** /apis/kubevirt.io/v1alpha1 | Get KubeVirt API Resources
[**kube_connection_healthz_func**](DefaultApi.md#kube_connection_healthz_func) | **GET** /apis/kubevirt.io/v1alpha1/healthz | Health endpoint
[**list_migration_for_all_namespaces**](DefaultApi.md#list_migration_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/migrations | Get a list of all Migration objects.
[**list_namespaced_migration_list**](DefaultApi.md#list_namespaced_migration_list) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/migrations | Get a list of Migration objects.
[**list_namespaced_virtual_machine_list**](DefaultApi.md#list_namespaced_virtual_machine_list) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines | Get a list of VirtualMachine objects.
[**list_namespaced_virtual_machine_replica_set_list**](DefaultApi.md#list_namespaced_virtual_machine_replica_set_list) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets | Get a list of VirtualMachineReplicaSet objects.
[**list_virtual_machine_for_all_namespaces**](DefaultApi.md#list_virtual_machine_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/virtualmachines | Get a list of all VirtualMachine objects.
[**list_virtual_machine_replica_set_for_all_namespaces**](DefaultApi.md#list_virtual_machine_replica_set_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/virtualmachinereplicasets | Get a list of all VirtualMachineReplicaSet objects.
[**read_namespaced_migration**](DefaultApi.md#read_namespaced_migration) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/migrations/{name} | Get a Migration object.
[**read_namespaced_virtual_machine**](DefaultApi.md#read_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name} | Get a VirtualMachine object.
[**read_namespaced_virtual_machine_replica_set**](DefaultApi.md#read_namespaced_virtual_machine_replica_set) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets/{name} | Get a VirtualMachineReplicaSet object.
[**replace_namespaced_migration**](DefaultApi.md#replace_namespaced_migration) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/migrations/{name} | Update a Migration object.
[**replace_namespaced_virtual_machine**](DefaultApi.md#replace_namespaced_virtual_machine) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name} | Update a VirtualMachine object.
[**replace_namespaced_virtual_machine_replica_set**](DefaultApi.md#replace_namespaced_virtual_machine_replica_set) | **PUT** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets/{name} | Update a VirtualMachineReplicaSet object.
[**spice**](DefaultApi.md#spice) | **GET** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name}/spice | Returns a remote-viewer configuration file. Run &#x60;man 1 remote-viewer&#x60; to learn more about the configuration format.
[**update_namespaced_migration**](DefaultApi.md#update_namespaced_migration) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/migrations/{name} | Patch a Migration object.
[**update_namespaced_virtual_machine**](DefaultApi.md#update_namespaced_virtual_machine) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachines/{name} | Patch a VirtualMachine object.
[**update_namespaced_virtual_machine_replica_set**](DefaultApi.md#update_namespaced_virtual_machine_replica_set) | **PATCH** /apis/kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinereplicasets/{name} | Patch a VirtualMachineReplicaSet object.
[**watch_migration_list_for_all_namespaces**](DefaultApi.md#watch_migration_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/watch/migrations | Watch a MigrationList object.
[**watch_namespaced_migration**](DefaultApi.md#watch_namespaced_migration) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace}/migrations | Watch a Migration object.
[**watch_namespaced_virtual_machine**](DefaultApi.md#watch_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace}/virtualmachines | Watch a VirtualMachine object.
[**watch_namespaced_virtual_machine_replica_set**](DefaultApi.md#watch_namespaced_virtual_machine_replica_set) | **GET** /apis/kubevirt.io/v1alpha1/watch/namespaces/{namespace}/virtualmachinereplicasets | Watch a VirtualMachineReplicaSet object.
[**watch_virtual_machine_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/watch/virtualmachines | Watch a VirtualMachineList object.
[**watch_virtual_machine_replica_set_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_replica_set_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1alpha1/watch/virtualmachinereplicasets | Watch a VirtualMachineReplicaSetList object.


# **console**
> console(namespace, name, console=console)

Open a websocket connection to a serial console on the specified VM.

Open a websocket connection to a serial console on the specified VM.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource
console = 'console_example' # str | Name of the serial console to connect to (optional)

try:
    # Open a websocket connection to a serial console on the specified VM.
    api_instance.console(namespace, name, console=console)
except ApiException as e:
    print("Exception when calling DefaultApi->console: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |
 **console** | **str**| Name of the serial console to connect to | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_migration**
> create_namespaced_migration(body, namespace)

Create a Migration object.

Create a Migration object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1Migration() # V1Migration |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try:
    # Create a Migration object.
    api_instance.create_namespaced_migration(body, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Migration**](V1Migration.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine**
> create_namespaced_virtual_machine(body, namespace)

Create a VirtualMachine object.

Create a VirtualMachine object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachine() # V1VirtualMachine |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try:
    # Create a VirtualMachine object.
    api_instance.create_namespaced_virtual_machine(body, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachine**](V1VirtualMachine.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_replica_set**
> create_namespaced_virtual_machine_replica_set(body, namespace)

Create a VirtualMachineReplicaSet object.

Create a VirtualMachineReplicaSet object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachineReplicaSet() # V1VirtualMachineReplicaSet |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try:
    # Create a VirtualMachineReplicaSet object.
    api_instance.create_namespaced_virtual_machine_replica_set(body, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_migration**
> delete_namespaced_migration(namespace, name)

Delete a Migration object.

Delete a Migration object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # Delete a Migration object.
    api_instance.delete_namespaced_migration(namespace, name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine**
> delete_namespaced_virtual_machine(namespace, name)

Delete a VirtualMachine object.

Delete a VirtualMachine object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # Delete a VirtualMachine object.
    api_instance.delete_namespaced_virtual_machine(namespace, name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_replica_set**
> delete_namespaced_virtual_machine_replica_set(namespace, name)

Delete a VirtualMachineReplicaSet object.

Delete a VirtualMachineReplicaSet object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # Delete a VirtualMachineReplicaSet object.
    api_instance.delete_namespaced_virtual_machine_replica_set(namespace, name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_migration**
> deletecollection_namespaced_migration(field_selector=field_selector, label_selector=label_selector)

Delete a collection of Migration objects.

Delete a collection of Migration objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)

try:
    # Delete a collection of Migration objects.
    api_instance.deletecollection_namespaced_migration(field_selector=field_selector, label_selector=label_selector)
except ApiException as e:
    print("Exception when calling DefaultApi->deletecollection_namespaced_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_virtual_machine**
> deletecollection_namespaced_virtual_machine(field_selector=field_selector, label_selector=label_selector)

Delete a collection of VirtualMachine objects.

Delete a collection of VirtualMachine objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)

try:
    # Delete a collection of VirtualMachine objects.
    api_instance.deletecollection_namespaced_virtual_machine(field_selector=field_selector, label_selector=label_selector)
except ApiException as e:
    print("Exception when calling DefaultApi->deletecollection_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_virtual_machine_replica_set**
> deletecollection_namespaced_virtual_machine_replica_set(field_selector=field_selector, label_selector=label_selector)

Delete a collection of VirtualMachineReplicaSet objects.

Delete a collection of VirtualMachineReplicaSet objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)

try:
    # Delete a collection of VirtualMachineReplicaSet objects.
    api_instance.deletecollection_namespaced_virtual_machine_replica_set(field_selector=field_selector, label_selector=label_selector)
except ApiException as e:
    print("Exception when calling DefaultApi->deletecollection_namespaced_virtual_machine_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func1**
> func1()



### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try:
    api_instance.func1()
except ApiException as e:
    print("Exception when calling DefaultApi->func1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> get_api_resources()

Get KubeVirt API Resources

Get KubeVirt API Resources

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try:
    # Get KubeVirt API Resources
    api_instance.get_api_resources()
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kube_connection_healthz_func**
> kube_connection_healthz_func()

Health endpoint

Health endpoint

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try:
    # Health endpoint
    api_instance.kube_connection_healthz_func()
except ApiException as e:
    print("Exception when calling DefaultApi->kube_connection_healthz_func: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_migration_for_all_namespaces**
> list_migration_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Get a list of all Migration objects.

Get a list of all Migration objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Get a list of all Migration objects.
    api_instance.list_migration_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->list_migration_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_migration_list**
> list_namespaced_migration_list(namespace, export=export, exact=exact)

Get a list of Migration objects.

Get a list of Migration objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace' (optional)

try:
    # Get a list of Migration objects.
    api_instance.list_namespaced_migration_list(namespace, export=export, exact=exact)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_migration_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_list**
> list_namespaced_virtual_machine_list(namespace, export=export, exact=exact)

Get a list of VirtualMachine objects.

Get a list of VirtualMachine objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace' (optional)

try:
    # Get a list of VirtualMachine objects.
    api_instance.list_namespaced_virtual_machine_list(namespace, export=export, exact=exact)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_replica_set_list**
> list_namespaced_virtual_machine_replica_set_list(namespace, export=export, exact=exact)

Get a list of VirtualMachineReplicaSet objects.

Get a list of VirtualMachineReplicaSet objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace' (optional)

try:
    # Get a list of VirtualMachineReplicaSet objects.
    api_instance.list_namespaced_virtual_machine_replica_set_list(namespace, export=export, exact=exact)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_replica_set_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_for_all_namespaces**
> list_virtual_machine_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Get a list of all VirtualMachine objects.

Get a list of all VirtualMachine objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Get a list of all VirtualMachine objects.
    api_instance.list_virtual_machine_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_replica_set_for_all_namespaces**
> list_virtual_machine_replica_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Get a list of all VirtualMachineReplicaSet objects.

Get a list of all VirtualMachineReplicaSet objects.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Get a list of all VirtualMachineReplicaSet objects.
    api_instance.list_virtual_machine_replica_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_replica_set_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_migration**
> read_namespaced_migration(name, namespace, export=export, exact=exact)

Get a Migration object.

Get a Migration object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace' (optional)

try:
    # Get a Migration object.
    api_instance.read_namespaced_migration(name, namespace, export=export, exact=exact)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine**
> read_namespaced_virtual_machine(name, namespace, export=export, exact=exact)

Get a VirtualMachine object.

Get a VirtualMachine object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace' (optional)

try:
    # Get a VirtualMachine object.
    api_instance.read_namespaced_virtual_machine(name, namespace, export=export, exact=exact)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_replica_set**
> read_namespaced_virtual_machine_replica_set(name, namespace, export=export, exact=exact)

Get a VirtualMachineReplicaSet object.

Get a VirtualMachineReplicaSet object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace' (optional)

try:
    # Get a VirtualMachineReplicaSet object.
    api_instance.read_namespaced_virtual_machine_replica_set(name, namespace, export=export, exact=exact)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional]
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_migration**
> replace_namespaced_migration(body, namespace, name)

Update a Migration object.

Update a Migration object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1Migration() # V1Migration |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # Update a Migration object.
    api_instance.replace_namespaced_migration(body, namespace, name)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Migration**](V1Migration.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine**
> replace_namespaced_virtual_machine(body, namespace, name)

Update a VirtualMachine object.

Update a VirtualMachine object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachine() # V1VirtualMachine |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # Update a VirtualMachine object.
    api_instance.replace_namespaced_virtual_machine(body, namespace, name)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachine**](V1VirtualMachine.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_replica_set**
> replace_namespaced_virtual_machine_replica_set(body, namespace, name)

Update a VirtualMachineReplicaSet object.

Update a VirtualMachineReplicaSet object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachineReplicaSet() # V1VirtualMachineReplicaSet |
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # Update a VirtualMachineReplicaSet object.
    api_instance.replace_namespaced_virtual_machine_replica_set(body, namespace, name)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachineReplicaSet**](V1VirtualMachineReplicaSet.md)|  |
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spice**
> spice(namespace, name)

Returns a remote-viewer configuration file. Run `man 1 remote-viewer` to learn more about the configuration format.

Returns a remote-viewer configuration file. Run `man 1 remote-viewer` to learn more about the configuration format.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
name = 'name_example' # str | Name of the resource

try:
    # Returns a remote-viewer configuration file. Run `man 1 remote-viewer` to learn more about the configuration format.
    api_instance.spice(namespace, name)
except ApiException as e:
    print("Exception when calling DefaultApi->spice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **name** | **str**| Name of the resource |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_namespaced_migration**
> update_namespaced_migration()

Patch a Migration object.

Patch a Migration object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try:
    # Patch a Migration object.
    api_instance.update_namespaced_migration()
except ApiException as e:
    print("Exception when calling DefaultApi->update_namespaced_migration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json-patch+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_namespaced_virtual_machine**
> update_namespaced_virtual_machine()

Patch a VirtualMachine object.

Patch a VirtualMachine object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try:
    # Patch a VirtualMachine object.
    api_instance.update_namespaced_virtual_machine()
except ApiException as e:
    print("Exception when calling DefaultApi->update_namespaced_virtual_machine: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json-patch+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_namespaced_virtual_machine_replica_set**
> update_namespaced_virtual_machine_replica_set()

Patch a VirtualMachineReplicaSet object.

Patch a VirtualMachineReplicaSet object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try:
    # Patch a VirtualMachineReplicaSet object.
    api_instance.update_namespaced_virtual_machine_replica_set()
except ApiException as e:
    print("Exception when calling DefaultApi->update_namespaced_virtual_machine_replica_set: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json-patch+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_migration_list_for_all_namespaces**
> watch_migration_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Watch a MigrationList object.

Watch a MigrationList object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Watch a MigrationList object.
    api_instance.watch_migration_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_migration_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_migration**
> watch_namespaced_migration(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Watch a Migration object.

Watch a Migration object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Watch a Migration object.
    api_instance.watch_namespaced_migration(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine**
> watch_namespaced_virtual_machine(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Watch a VirtualMachine object.

Watch a VirtualMachine object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Watch a VirtualMachine object.
    api_instance.watch_namespaced_virtual_machine(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_replica_set**
> watch_namespaced_virtual_machine_replica_set(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Watch a VirtualMachineReplicaSet object.

Watch a VirtualMachineReplicaSet object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Watch a VirtualMachineReplicaSet object.
    api_instance.watch_namespaced_virtual_machine_replica_set(namespace, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects |
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_list_for_all_namespaces**
> watch_virtual_machine_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Watch a VirtualMachineList object.

Watch a VirtualMachineList object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Watch a VirtualMachineList object.
    api_instance.watch_virtual_machine_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_replica_set_list_for_all_namespaces**
> watch_virtual_machine_replica_set_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)

Watch a VirtualMachineReplicaSetList object.

Watch a VirtualMachineReplicaSetList object.

### Example
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)

try:
    # Watch a VirtualMachineReplicaSetList object.
    api_instance.watch_virtual_machine_replica_set_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_replica_set_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional]
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
