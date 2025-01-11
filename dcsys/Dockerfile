# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
ARG TEMPIO_VERSION BUILD_ARCH
RUN curl -sSLf -o /usr/bin/tempio "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

RUN apk add --no-cache python3 py-pip
RUN pip install websockets
RUN apk add wget
RUN apk add libc6-compat
RUN apk add libpthread-stubs
RUN apk add libmodbus
RUN apk add git

# Copy root filesystem
COPY rootfs /
