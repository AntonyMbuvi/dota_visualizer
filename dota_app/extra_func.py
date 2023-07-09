import os
from flask import session
from dota_app import app

def delete_saved_plots():
    # Get the list of image names from the session
    my_images = session.get('my_images', [])

    # Delete the saved plot files
    for image_name in my_images:
        file_path = os.path.join(app.root_path, 'static', 'images', image_name)
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error deleting file {file_path}: {e}")

