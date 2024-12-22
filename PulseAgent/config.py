
# Configuration settings for PulseAgent

DEFAULT_SETTINGS = {
    "log_level": "INFO",
    "data_dir": "./data",
}

def get_setting(key, default=None):
    return DEFAULT_SETTINGS.get(key, default)
