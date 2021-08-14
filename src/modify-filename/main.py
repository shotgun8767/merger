import os

from src.common.command_parser import CommandParser


def main(parser: CommandParser):
    target_dir = parser.require('target-dir')[0]
    map_dependency = parser.require('map-dependency')[0]

    # 读取映射依赖文件
    _map = {}
    flag = True
    for line in open(map_dependency, 'r', encoding='utf8'):
        # 跳过首行
        if flag:
            flag = False
            continue

        # 逐行读取，提取 sample_accession 和 gen_dataset_id ，放入映射中
        sp = line.split()
        sample_accession = sp[5]
        gen_dataset_id = sp[4]
        _map[sample_accession] = gen_dataset_id

    # 遍历目标文件夹下的所有文件
    for file in os.listdir(target_dir):
        (basename, ext) = os.path.splitext(file)
        word_list = basename.split('_')
        modified = False
        for i in range(0, len(word_list)):
            word = word_list[i]
            if word[0:3] == 'SRS':
                # 该单词需要更改
                replace = _map.get(word)
                if replace is not None:
                    word_list[i] = replace
                    modified = True
        if modified:
            # 更改文件名
            new_filename = '_'.join(word_list) + ext
            old_filepath = os.path.join(target_dir, file)
            new_filepath = os.path.join(target_dir, new_filename)
            os.rename(old_filepath, new_filepath)
