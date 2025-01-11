#!/usr/bin/with-contenv bashio
# shellcheck shell=bash
# ==============================================================================
# SSH Host keys
# ==============================================================================
declare github_repository
declare dcsys_config_root_dir

github_repository=$(bashio::config 'github_repository')
dcsys_config_root_dir=$(bashio::config 'dcsys_config_root_dir')
bashio::log.info  "GitHeb Checkout from ${github_repository} to ${GITHUB_PATH}"

if [ ! -d ${dcsys_config_root_dir} ]; then
    bashio::log.info "DCSys configuratie is er niet, GIT checkout"
    git clone ${github_repository} ${dcsys_config_root_dir}
else
    cd ${dcsys_config_root_dir}
    git pull
fi
