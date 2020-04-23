#!/usr/bin/python

import subprocess
import sys

def show_help():
    print 'Usage: '
    print './streamer.py url destination <stream_name/stream_code>'
    print './streamer.py https://www.youtube.com/watch?v=9cQT4urTlXM rtmp://x.rtmp.youtube.com/live2 <stream_name/stream_code>'
    return

def streamer() :
    url = sys.argv[1]
    if not url :
        print 'Error: url is empty'
        return
    destination = sys.argv[2]
    if not destination:
        print 'Error: destination is empty'
        return
    stream_id = sys.argv[3]
    if not stream_id:
        print 'Error: stream name is empty'
        return
    

    _youtube_process = subprocess.Popen(('youtube-dl','-f','','--prefer-ffmpeg', '--no-color', '--no-cache-dir', '--no-progress','-o', '-', '-f', '22/18', url, '--reject-title', stream_id),stdout=subprocess.PIPE)
    _ffmpeg_process = subprocess.Popen(('ffmpeg','-re','-i', '-','-preset', 'ultrafast','-vcodec', 'copy', '-acodec', 'copy','-threads','1', '-f', 'flv',destination + "/" + stream_id), stdin=_youtube_process.stdout)
    return

if len(sys.argv) < 4:
    show_help()
else:
    streamer()
