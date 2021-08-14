import sys
import importlib

from src.common.command_parser import *
from src.common.module_helper import *

# 命令行参数
argv = sys.argv[1:]

if len(argv) == 0:
    # 缺少命令
    print('Missing command.')
    exit()
command = argv[0]  # command - 命令
unit_list = argv[1:]  # unit list - 单元（选项或参数）列表

# 进入 src 目录下与命令同名的包（目的包）
# 读取 options 模块
target_package_path = 'src.' + command
options_module_path = target_package_path + '.options'
options_module = importlib.import_module(options_module_path)
attrs = get_attrs(options_module)
long_option_list = attrs['long_option_list']
option_map = attrs['option_map']

# 构建命令解析器
parser = CommandParser(unit_list) \
    .set_options(long_option_list, option_map) \
    .parse()

# 读取 main 模块
main_module_path = target_package_path + '.main'
main_module = None
try:
    main_module = importlib.import_module(main_module_path)
except ModuleNotFoundError:
    print('Missing `main` module in target package: <' + main_module_path + '>')
    exit()

if hasattr(main_module, 'main'):
    main = getattr(main_module, 'main')
    main(parser)
else:
    print('Missing `main` function in: <' + main_module_path + '>')
