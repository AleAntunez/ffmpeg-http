FROM ubuntu:22.04

# Install FFMPEG 5 from Savoury
RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:savoury1/ffmpeg4 -y
RUN add-apt-repository ppa:savoury1/ffmpeg5 -y
RUN apt-get update -y
RUN apt upgrade -y
RUN apt-get install -y ffmpeg

# Now nginx
RUN apt-get install nginx -y

# Install flask
RUN apt-get install python3-pip -y
RUN python3 -m pip install flask

# Install psmisc
RUN apt-get install psmisc -y

# Install requests
RUN python3 -m pip install requests

RUN echo "#!/bin/bash" > entrypoint.sh
RUN echo "python3 restreamer.py & service nginx start & sleep infinity" >> entrypoint.sh
RUN chmod +x entrypoint.sh

# Copy the restreamer
COPY restreamer.py .

ENTRYPOINT [ "./entrypoint.sh" ]