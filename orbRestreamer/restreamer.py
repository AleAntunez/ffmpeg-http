from flask import Flask, Response, request, redirect
from requests import get
import subprocess
import time
import os
import fnmatch

app = Flask(__name__)

def find_files(base, pattern):
    '''Return list of files matching pattern in base folder.'''
    return [n for n in fnmatch.filter(os.listdir(base), pattern) if
        os.path.isfile(os.path.join(base, n))]

@app.route("/restream")
def restream():
    print("Request received")
    subprocess.call("killall -9 ffmpeg", shell = True)
    subprocess.call("rm -rf /var/www/html/*", shell = True)
    command = "ffmpeg -i '%s' -acodec ac3 -vcodec copy -f hls -hls_list_size 0 -hls_time 6 -hls_playlist_type event -hls_segment_type fmp4 /var/www/html/stream.m3u8" % request.args.get('url')
    process = subprocess.Popen(command, shell = True)
    print (find_files("/var/www/html", "stream0.*"))
    while len(find_files("/var/www/html", "stream0.*")) == 0:
        time.sleep(2)
        print("Waiting for ffmpeg to produce the first stream")
    return redirect("http://macpro1.casa.de:9081/stream.m3u8")

app.run(host='0.0.0.0', port=9080)