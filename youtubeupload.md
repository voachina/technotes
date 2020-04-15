# About

How to upload file to your youtube channel from command line.

# Steps

## Install `youtube-upload`

Go to `https://github.com/tokland/youtube-upload` and install the python package following the instruction. 
Python virtual environment is recommended.

```
python3 -m venv youtube
source youtube/bin/activate
wget https://github.com/tokland/youtube-upload/archive/master.zip
unzip master.zip
cd youtube-upload-master
python setup.py install
pip install google-api-python-client progressbar2 oauth2client
```

> Fix an oauth2client error by changing the `import oauth2client` in file `youtube-upload-master/youtube_upload/main.py` to `from oauth2client import file`.

## Configure the google youtube api

- Go to `https://console.developers.google.com/` and login
- Create a project for the youtube upload purpose
- Enable the youtube APIs.
- Configure the consent screen
- Create OAuth credentials and download the json file

## Start uplaoding

```bash
$ youtube-upload-master/bin/youtube-upload --client-secrets=client_secret.json --privacy=unlisted --playlist="test" --title="test" test.mp4
```

Copy the url and accept the permission requests. On success, copy the code and paste it to the command line. Your upload should work.



