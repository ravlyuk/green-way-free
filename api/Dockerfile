FROM --platform=linux/amd64 nginx/unit:1.29.1-python3.11

# Our Debian with Python and Nginx for python apps.
# See https://hub.docker.com/r/nginx/unit/



# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./config/config.json /docker-entrypoint.d/config.json

# Ok, this is something we get thanks to the Nginx Unit Image.
# We don't need to call stuff like
# curl -X PUT --data-binary @config.json --unix-socket \
#       /path/to/control.unit.sock http://localhost/config/
# to set our configuration
# Becouse as stated in docs https://unit.nginx.org/installation/#docker-images,
# configuration snippets are 
# uploaded as to the config section of Unit’s configuration
# That means we only have to copy our config.json file to the folder
# /docker-entrypoint.d/

RUN mkdir build

# set work directory
WORKDIR /build

RUN apt update && apt install -y python3-pip                                  \
    && apt remove -y python3-pip                                              \
    && apt autoremove --purge -y                                              \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

RUN pip install --upgrade pip

COPY . .

COPY ./requirements.txt .

# install dependencies.
RUN pip install -r requirements.txt


# OK, that looks strange but here's a explanation from Nginx docs
# https://unit.nginx.org/howto/docker/:

# """ PIP isn't installed by default, so we install it first.
# Next, we install the requirements, remove PIP, and perform image cleanup. """

# Note we use /build/requirements.txt since this is our file

# Instruction informs Docker that the container listens on port 80





