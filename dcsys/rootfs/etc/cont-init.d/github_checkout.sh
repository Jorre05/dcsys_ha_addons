#!/usr/bin/with-contenv bashio
# shellcheck shell=bash
# ==============================================================================
# SSH Host keys
# ==============================================================================
readonly GITHUB_PATH=/data/dcsys_github
declare github_repository

if ! bashio::fs.directory_exists "${GITHUB_PATH}"; then
    bashio::log.info "GitHub pad maken..."

    mkdir -p "${GITHUB_PATH}"
fi

bashio::log.info  "GitHeb Checkout from ${github_repository} to ${GITHUB_PATH}"
cd ${GITHUB_PATH}
git checkout ${github_repository}

