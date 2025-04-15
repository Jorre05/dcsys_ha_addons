#!/usr/bin/with-contenv bashio
# shellcheck shell=bash
# ==============================================================================
# SSH Host keys
# ==============================================================================
declare github_repository
declare dcsys_config_root_dir
declare listen_on
declare dns_servers

github_repository=$(bashio::config 'github_repository')
listen_on=$(bashio::config 'listen_on')
dns_servers=$(bashio::config 'dns_servers')
dcsys_config_root_dir=$(bashio::config 'dcsys_config_root_dir')
bashio::log.info  "GitHub Checkout from ${github_repository} to ${dcsys_config_root_dir}"

rm -fr ${dcsys_config_root_dir}
mkdir -p ${dcsys_config_root_dir}
bashio::log.info "DCSys configuratie is er niet, GIT clone"
git clone ${github_repository} ${dcsys_config_root_dir}

cp -frp ${dcsys_config_root_dir}/dhcp/* /config
sed "s/#LISTEN_ON#/${listen_on}/g" /config/kea-dhcp4.conf -i
sed "s/#DNS_SERVERS#/${dns_servers}/g" /config/kea-dhcp4.conf -i
