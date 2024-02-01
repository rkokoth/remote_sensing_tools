# 1. Base image
FROM python
FROM ghcr.io/osgeo/gdal:ubuntu-full-latest

# 2. Copy files
COPY . /src

# 3. Install dependencies

# update the image linux system then install python3-pip
RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip

RUN pip3 install -r ./src/requirements.txt
CMD [ "./src/getHansenData.py" ]

# explore pulling the files inot local directory once they are ready
# docker cp 2347:/var/www/html/data/ /home/user/archive/data