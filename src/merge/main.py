from src.common.command_parser import CommandParser


def main(parser: CommandParser):
    target_file_list = parser.get_arguments_of_option('target')
    export_dir_path = parser.get_arguments_of_option('export-dir')[0]
    merge_two_gene_mat(target_file_list, export_dir_path)


def merge_two_gene_mat(merge_file_list: list, export_dir: str = '') -> None:
    """
    合并两个表格文件
    这两个表格文件的首列（ID）相同，但从第二列开始（样品名称）不同
    :param merge_file_list: 需要合并的文件列表
    :param export_dir: 输出文件的路径（默认为当前目录下的 'merge_export' 文件）
    """

    # 打开所有需要合成的文件并获得句柄
    handle_list = []
    for merge_file in merge_file_list:
        handle_list.append(open(merge_file, 'r', encoding='utf8'))

    # 拼接标题行（heading）
    heading_list = []
    for handle in handle_list:
        handle.readline()
    file_1_column_list = get_element_list(file_1.readline())
    file_2_column_list = get_element_list(file_2.readline())
    new_column_list = file_1_column_list + (file_2_column_list[1:])

    # 新文件的内容
    new_file = '\t'.join(new_column_list)

    # 循环拼接行
    while True:
        file_1_line = file_1.readline()
        file_2_line = file_2.readline()

        # 任一文件读完，退出循环
        if not file_1_line or not file_2_line:
            file_1.close()
            file_2.close()
            break

        file_1_line = get_element_list(file_1_line)
        file_2_line = get_element_list(file_2_line)[1:]
        new_file += '\n' + '\t'.join(file_1_line + file_2_line)
    pass

    if not export_filepath:
        export_filepath = 'merge_export'
    open(export_filepath, 'w+').write(new_file)


def get_element_list(string: str, separator: str = '\t') -> list:
    """
    根据字符串获得元素列表
    :param string: 指定字符串
    :param separator: 元素间的分隔符
    :return:
    """
    if string == '':
        return []
    string = string.split('\n')[0]  # 去除行尾的换行符。 Windows 的换行符为 \merge\n ，Linux 为 \n
    sp = string.split(separator)
    if sp[-1] == '':
        # 去除可能的行末空值
        sp = sp[0: -2]
    return sp
