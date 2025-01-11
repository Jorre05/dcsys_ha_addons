#!/usr/bin/with-contenv bashio
# shellcheck shell=bash
# ==============================================================================
# SSH Host keys
# ==============================================================================
readonly GITHUB_PATH=/data
declare github_repository

github_repository=$(bashio::config 'github_repository')
bashio::log.info  "GitHeb Checkout from ${github_repository} to ${GITHUB_PATH}"
cd ${GITHUB_PATH}
git clone ${github_repository}

