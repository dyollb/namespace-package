
def run():
    print(f"Hello from {__package__} : {__name__} : {__file__}")

def run_all():
    import pkgutil
    import mynamespace as ns

    for module_info in pkgutil.walk_packages(path=ns.__path__, prefix=ns.__name__+'.', onerror=lambda x: None):
        if module_info.name.endswith(".module"):
            pkgutil.resolve_name(module_info.name).run()
