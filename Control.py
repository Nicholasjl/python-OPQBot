plugin_list={}
def on_command(command):
    def wrapper(func):
        plugin_list[command]=func
        def deco(*args, **kwargs):
            func(*args, **kwargs)
        return deco
    return wrapper