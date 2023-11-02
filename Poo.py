import gi
gi.require_version('AppStream', '1.0')
from gi.repository import AppStream

def parse_metadata(metadata_path):
    context = AppStream.Context()
    context.set_flags(AppStream.ContextFlags.NONE)
    context.setup()

    metadata = AppStream.Metadata()
    if context.load_metadata(metadata_path, metadata) != AppStream.ErrorCode.NONE:
        return None

    app_data = {}
    for app in metadata.get_apps():
        app_id = app.get_id()
        app_data[app_id] = {
            'id': app_id,
            'icon': app.get_icon(),
            'release': app.get_release()
        }

    return app_data

metadata_path = "path_to_metadata.xml"  # Replace with the actual path to your XML metadata file
parsed_data = parse_metadata(metadata_path)

if parsed_data:
    for app_id, app_details in parsed_data.items():
        print(f"App ID: {app_id}")
        print(f"App Icon: {app_details['icon']}")
        print(f"App Release: {app_details['release']}")
