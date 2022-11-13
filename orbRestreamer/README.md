# FFMPEG-HTTP

This repo defines a Dockerfile and a python capable of restreaming an URL containing a MKV file and producing a stable HLS streaming, suitable, for example, for tvOS/iOS/macOS or any other OS capable of playing HLS streams.

## Usage

1. Build the Docker image
   docker build -t ffmpeg-http

2. Run the docker image
   docker run -it -p 9080:9080 -p9081:80 ffmpeg-http

Dont forget of adapting the ports and hostname as appears in the Python

This is a very much draft state but took me a while to figure out how to play MKVs natively on an Apple TV, while preserving DV/HDR streams as I just wanted to demux MKVs. Keep in mind audio is encoded into AC3, pretty much the only format accepted by tvOS.

Also, keep in mind that even if the player is not playing the URL anymore, ffmpeg will keep transcoding to disk...