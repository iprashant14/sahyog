import os


def upload_image(instance, filename):
    return os.path.join(instance._meta.model_name, '_'.join(filename.split()))

