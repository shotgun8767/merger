class CommandParser:
    def __init__(self, unit_list):
        # 单元列表
        self.unit_list: list = []
        # 长选项列表
        self.long_option_list: list = []
        # 短选项与长选项映射
        self.option_map: dict = {}
        # 选定的选项
        self.selected_options: list = []
        # 参数
        self.arguments: dict = {}

        for u in unit_list:
            unit = u.strip()
            # 过滤掉空单元
            if len(unit) > 0:
                self.unit_list.append(unit)

    def set_options(self, long_option_list: list, option_map: dict):
        """
        设置选项
        :param long_option_list: 长选项列表
        :param option_map: 短选项列表
        :return self
        """
        self.long_option_list = long_option_list
        self.option_map = option_map
        return self

    def parse(self):
        """
        解析命令
        :return: self
        """
        curr_opt = None
        for unit in self.unit_list:
            if unit[:2] == '--':
                # 长选项
                curr_opt = unit[2:]
                self.selected_options.append(curr_opt)
                self.arguments[curr_opt] = []
            elif unit[0] == '-':
                # 短选项
                short_opts = unit[1:]
                for opt in short_opts:
                    long_opt = self.option_map.get(opt)
                    if long_opt is not None:
                        # 有对应的长选项
                        curr_opt = long_opt
                        self.selected_options.append(curr_opt)
                        self.arguments[curr_opt] = []
            else:
                # 参数
                self.arguments[curr_opt].append(unit)
                pass
        return self

    def get_selected_options(self):
        """
        :return: 选定的选项
        """
        return self.selected_options

    def is_selected(self, option: str) -> bool:
        """
        判断指定选项是否被选定。
        :param option:
        """
        return option in self.selected_options

    def get_arguments_of_option(self, option: str) -> list:
        """
        根据选项获取参数。
        :param option: 选项
        :return: 参数列表
        """
        return self.arguments.get(option)

    def require(self, option: str):
        """
        根据选项获取参数。若选项没有被选中，则抛出异常
        :param option:
        :return:
        """
        args = self.get_arguments_of_option(option)
        if args is None:
            raise Exception('Missing required option: [' + option + ']')
        return args
