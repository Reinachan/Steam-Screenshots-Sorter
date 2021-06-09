import os


def img_sort(folder_name, path):
    try:
        os.makedirs(f"./{folder_name}")
    except Exception:
        pass
        # print("already exists")
    finally:
        try:
            os.replace(path, f"./{folder_name}/{path}")
        except Exception:
            pass
            # print("already exist")
