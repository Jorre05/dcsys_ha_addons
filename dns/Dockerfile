# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache bind
RUN apk add --no-cache git

# Copy root filesystem
COPY rootfs /
