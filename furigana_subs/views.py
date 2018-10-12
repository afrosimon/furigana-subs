import os
from flask import Flask, Blueprint, current_app, request
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest, MethodNotAllowed
from .engine import SubtitleEngine


index_page = Blueprint('index', __name__)
ALLOWED_EXTENSIONS = set(['txt', 'srt'])


# taken directly from the flask doc
def allowed_file(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@index_page.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            raise BadRequest('Must include a file field')

        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = os.path.join(
                current_app.config['UPLOAD_FOLDER'],
                secure_filename(file.filename)
            )

            file.save(filename)

            engine = SubtitleEngine(filename)
            output = engine.add_furigana()

            return output.read()
        else:
            raise BadRequest('Wrong format for the file')
    else:
        raise MethodNotAllowed('Must POST')
