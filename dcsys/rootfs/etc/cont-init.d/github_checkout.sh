#!/usr/bin/with-contenv bashio
# shellcheck shell=bash
# ==============================================================================
# SSH Host keys
# ==============================================================================
readonly GITHUB_PATH=/share
declare github_repository

github_repository=$(bashio::config 'github_repository')
bashio::log.info  "GitHeb Checkout from ${github_repository} to ${GITHUB_PATH}"

if [ ! -d ${GITHUB_PATH}/dcsys_ha_config ]; then
    bashio::log.info "DCSys configuratie is er niet, GIT checkout"
    cd ${GITHUB_PATH}
    git clone ${github_repository}
else
    cd ${GITHUB_PATH}
    git pull
fi
