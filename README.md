# secret-file-server

## Installation

1. `pip3 install -r requirements.txt`
2. Provide a config for the server with the configuration below.
3. ./run.sh
4. the download url is `http://yourdomain/SS_SECRET_PATH?key=SS_MY_SECRET`

## Configuration
* `SS_FILE_NAME`: file path to serve
* `SS_SECRET_PATH`: the path to serve the file, e.g. localhost/d813fda9
* `SS_MY_SECRET`: the secret key for accessing the file
* `SS_MAX_DOWNLOAD`: maximum try of download. default=1
