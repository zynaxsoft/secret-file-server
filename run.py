from flask import Flask, request, send_from_directory, make_response

import datetime


app = Flask(__name__, static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


FILE_NAME = 'some_file_to_serve'
SECRET_PATH = 'secret_path'  # localhost/secret_path to get the file
MY_SECRET = 'some_secret'  # secret to enter in the query variable "key"
# localhost/secret_path?key=some_secret


global counter
counter = 0


@app.route('/secret/<path:path>', methods=['GET'])
def download(path):
    global counter
    if path == SECRET_PATH and request.args.get('key') == MY_SECRET:
        if counter > 0:
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
