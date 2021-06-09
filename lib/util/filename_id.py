def get_id(filename: str) -> str:
    split_name = filename.split("_")
    # print(split_name)
    try:
        if split_name[2]:
            return split_name[0]
        else:
            return None
    except Exception:
        return None
