import datetime
import os

from flask import Flask, request, send_from_directory, make_response


app = Flask(__name__, static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


FILE_NAME = os.environ.get('SS_FILE_NAME', 'some_file_to_serve')
# localhost/secret_path to get the file
SECRET_PATH = os.environ.get('SS_SECRET_PATH', 'secret_path')
# secret to enter in the query variable "key"
MY_SECRET = os.environ.get('SS_MY_SECRET', 'some_secret')
MAX_DOWNLOAD = os.environ.get('SS_MAX_DOWNLOAD', 1)


global counter
counter = 0


@app.route('/secret/<path:path>', methods=['GET'])
def download(path):
    global counter
    if path == SECRET_PATH and request.args.get('key') == MY_SECRET:
        if counter > MAX_DOWNLOAD - 1:
            return 'Link expired.'
        counter += 1
        with open('downloaded', 'a') as f:
            f.write(f'ip: {request.remote_addr},'
                    f' date: {datetime.datetime.now()}\n')
        return send_from_directory('.', FILE_NAME)
    response = make_response()
    response.status = '400'
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=9990,
            )
