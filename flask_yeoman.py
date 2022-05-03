from flask import Blueprint, current_app, send_file, render_template_string
from werkzeug.exceptions import NotFound
from werkzeug.utils import safe_join

import os

flask_yeoman = Blueprint('flask_yeoman', __name__)


@flask_yeoman.route('/', defaults={'path': 'index.html'})
@flask_yeoman.route('/<path:path>')
def serve_index(path):
    flask_yeoman_debug = int(os.environ.get('FLASK_YEOMAN_DEBUG', False))
    fpath = 'dist'
    # While developing, we serve the app directory
    if flask_yeoman_debug:
        fpath = 'app'

    root_path = current_app.root_path
    default_path = os.path.join(root_path, fpath)

    default_path_abs = safe_join(default_path, path)

    if os.path.isfile(default_path_abs):
        if path == 'index.html':
            # If index.html is requested, we inject the Flask current_app config
            return render_template_string(open(default_path_abs).read().decode('utf-8'),
                                          config=current_app.config)
        return send_file(default_path_abs)

    # While development, we must check the .tmp dir as fallback
    if flask_yeoman_debug:
        # The .tmp dir is used by compass and for the template file
        alt_path = os.path.join(root_path, '.tmp')
        alt_path_abs = os.path.join(alt_path, path)
        if os.path.isfile(alt_path_abs):
            return send_file(alt_path_abs)

    raise NotFound()
