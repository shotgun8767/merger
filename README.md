# Merger

## 命令 - Command

本节简单说明`Linux`风格的命令（`command`）的使用方法。

在`Linux`等很多环境中（比如`npm`），设计者都会根据以下规范设计命令：

* 使用空格将选项（`option`）和参数（`argument`）隔开；

* 选项一般有长选项和短选项两种。长选项使用双横线（ ）作为前缀，单词之间用单短划线分隔；短选项则使用但短划线作为前缀，如：

    ~~~bash
    # 以下两个命令是等价的
    python --version
    python -v
    ~~~

    长选项和短选项有一套映射关系（有的长选项无对应的短选项，有的短选项也无对应的短选项），需要用户记忆（或查询手册）。

* 有的选项后可以连接参数（是否能连接以及能连接多少个，都是规定好的），如：

    ~~~bash
    node ./bin/www -p 12388 --babel "v5"
    ~~~

* 在某些情景下，长选项可以通过`=`与唯一的参数连接：

    ~~~bash
    node ./bin/www --port=12388
    ~~~
    
* 短选项可以进行复合，如下方命令所示，分别选中了三个短选项：`t`、`v`和`f`。

    ~~~bash
    tar -tvf my.tar
    ~~~

## Merger 使用手册 - Manual

### 原理

本框架有唯一的入口文件`index.py`（在根目录下），在命令行中输入以下格式的指令，即可启动框架。`command`是命令，框架会根据命令定位到`./src`目录下的同名目录。`options`是选项，`arguments`是参数。

~~~bash
python index.py <command> [options] [arguments]
~~~

如输入以下指令：

~~~bash
python index.py merge --target-dir ./data/ --export-dir ./data-export
~~~

命令为`command`，有两个选定选项`target-dir`和`export-dir`，对应的参数分别为`./data/`和`./data-export`。

### 指令

> 本节中所有指令省略`python index.py`前缀。

#### modify-filename

~~~bash
 modify-filename --target-dir <目标目录> --map-dependency <映射依赖文件>
~~~

