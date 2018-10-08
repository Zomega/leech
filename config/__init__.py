import json
import requests
import logging

logger = logging.getLogger(__name__)

CONFIG_FILENAME = 'leech.json'

try:
    with open(CONFIG_FILENAME) as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    config = None
    logger.info("Unable to locate " + CONFIG_FILENAME + ". Continuing assuming it does not exist.")

def get_configured_site_options(site):
    if config is None:
        return {}
    return config.get('site_options', {}).get(site.__name__, {})

def get_login(site):
    if config is None:
        return False
    return config.get('logins', {}).get(site.__name__, False)

def get_cover_options():
    if config is None:
        return {}
    return config.get('cover', {})
