class Configuration:
    _config = {}

    @classmethod
    def set_config(cls, key, value):
        cls._config[key] = value

    @classmethod
    def get_config(cls, key):
        return cls._config.get(key, None)


Configuration.set_config("debug", True)
print(Configuration.get_config("debug"))
