def module_import():
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
    return storage

global storage
storage = module_import()