import ctypes
from ctypes.util import find_library

class AppstreamError(Exception):
    pass

# Load the appstream-glib library
appstream = ctypes.CDLL(find_library('appstream-glib'))

# Initialize the library
appstream.as_init()

# Create a store
store = appstream.as_store_new()

# Load AppStream data from a file
xml_file = "path/to/appstream.xml"
error = ctypes.c_void_p()
if not appstream.as_store_load(store, xml_file, None, ctypes.byref(error)):
    error_msg = ctypes.cast(error, ctypes.c_char_p).value.decode('utf-8')
    raise AppstreamError(f"Failed to load AppStream data: {error_msg}")

# Get the root node
root_node = appstream.as_store_get_root(store)

# Iterate through nodes
node = root_node
while node:
    app_id = ctypes.cast(appstream.as_node_get_id(node), ctypes.c_char_p).value.decode('utf-8')
    icon = ctypes.cast(appstream.as_node_get_icon(node), ctypes.c_char_p).value.decode('utf-8')
    release = ctypes.cast(appstream.as_node_get_version(node), ctypes.c_char_p).value.decode('utf-8')

    print(f"App ID: {app_id}")
    print(f"Icon: {icon}")
    print(f"Release: {release}")

    node = appstream.as_node_next(node)

# Cleanup and release resources
appstream.as_store_free(store)
appstream.as_cleanup()
