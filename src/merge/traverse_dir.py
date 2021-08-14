import sys
import os
import os.path as path

import merge


def traverse_dir(dir_1: str, dir_2: str, export_dir: str = '.') -> None:
    """
    遍历两个目录下的文件，将同名文件合并
    :param dir_1: 目录1
    :param dir_2: 目录2
    :param export_dir: 输出目录
    """

    dir_1_file_list = os.listdir(dir_1)
    dir_2_file_list = os.listdir(dir_2)

    for i in range(0, len(dir_1_file_list)):
        file_name = dir_1_file_list[i]
        # 若在目录2中有同名文件
        if file_name in dir_2_file_list:
            file_1_path = path.join(dir_1, file_name)
            file_2_path = path.join(dir_2, file_name)
            export_filepath = path.join(export_dir, file_name)
            merge.merge_two_gene_mat(file_1_path, file_2_path, export_filepath)


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) == 3:
        traverse_dir(argv[1], argv[2])
    elif len(argv) == 4:
        traverse_dir(argv[1], argv[2], argv[3])
    else:
        print('参数错误')
