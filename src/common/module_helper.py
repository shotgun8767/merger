def get_attrs(module) -> dict:
    """
    获取指定模块中的所有变量（不包括全局变量）
    :param module: 指定模块
    :return: 字典（映射关系：变量名 => 值）
    """
    keys = module.__dict__.keys()
    ret = {}
    for key in keys:
        if key[0:2] == '__' and key[-2:] == '__':
            # 全局变量
            continue
        else:
            ret[key] = getattr(module, key)
    return ret
