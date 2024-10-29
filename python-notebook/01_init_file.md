[TOC]

# 如何使用 \_\_init__.py 创建 Python 包

## 什么是 Python 包？
Python 包只是 Python 模块的组织集合。Python 模块只是一个 Python 文件。


## 为什么我要使用 \_\_init__.py 创建包？
使用 \_\_init__.py 创建包是为了更轻松地开发更大的 Python 项目。

它为您提供了一种机制，可以将单独的 Python 脚本分组到单个可导入的模块中。

## 让我们来看一些例子
了解为什么要使用 \_\_init__.py 以及如何使用它来创建包的最佳方法是运行一些简单示例！最好的学习方法是实践！

本教程中的代码适用于 Python 2 或 3。请记住，如果您使用的是 2，那么您将需要使用 from \_\_future__ import print_function 功能。

假设我们创建了三个模块：
``` bash
someFolder
|-- stringLength.py
|-- stringToUpper.py
`-- stringToLower.py
```
记住，模块只是任何单个 Python 文件的另一个名称

对于我们的示例，这些文件的内容如下：
``` python
# stringLength.py

def stringLength(inStr):
    return len(inStr)
```

``` python
# stringToUpper.py

def stringToUpper(inStr):
    return inStr.upper()
```

``` python
# stringToLower.py

def stringToLower(inStr):
    return inStr.lower()
```
显然，这些函数是没用的，但它有助于作为基本概念的模型，即我们已经编写了一些以某种方式相关的 Python 模块。

那么，如果不创建包并使用 \_\_init__.py，我们如何使用这些文件中的函数呢？

好吧，我们可以在新的 Python 脚本中使用这些文件，但有一个关键的警告：
> The files must be in the same directory as the script we are trying to use them in.

为了说明这一点，让我们创建一个名为 example1.py 的文件来利用我们的模块：

``` python
# example1.py

import stringLength
import stringToLower
import stringToUpper

some_string = "Hello, Universe!"

print(stringLength.stringLength(some_string))
print(stringToLower.stringToLower(some_string))
print(stringToUpper.stringToUpper(some_string))
```

## 添加空白的 \_\_init__.py
如果我们想将这些脚本分离到一个文件夹中以使它们更有条理，该怎么办？

嗯，这就是 \_\_init__.py 文件发挥作用的地方。

首先，让我们将脚本移到一个新的子文件夹中并将其命名为：string_func。然后在该文件夹中创建一个名为\_\_init__.py 的空文件

这是我们的新文件/文件夹结构：
``` bash
someFolder
|-- string_func
|   |-- __init__.py
|   |-- stringToUpper.py
|   |-- stringToLower.py
|   `-- strengthLength.py
`-- example1.py
```

那么，现在让我们测试一下 \_\_init__.py 到底允许我们做什么
``` python
# example2.py

import string_func.stringLength
import string_func.stringToLower
import string_func.stringToUpper

some_string = "Hello, Universe!"

print(string_func.stringLength.stringLength(some_string))
print(string_func.stringToLower.stringToLower(some_string))
print(string_func.stringToUpper.stringToUpper(some_string))
```

现在，我们可以通过这种方式访问​​字符串函数。这很好，因为它们都在一个单独的文件夹中，但语法肯定不是很简洁。让我们看看是否可以通过编辑 \_\_init__.py 文件来清理一下。

## 向 init.py 添加导入
打开 \_\_init__.py 文件并进行以下更改：
``` python
# __init__.py
from .stringLength import stringLength
from .stringToLower import stringToLower
from .stringToUpper import stringToUpper
```
请注意，从 Python 3 开始，模块名称前面的 . 是必需的，因为它对于相对导入更加严格：[Click](https://stackoverflow.com/questions/12172791/changes-in-import-statement-python3?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)


因此，有了 \_\_init__.py 中的代码，我们现在可以将代码缩短为：
``` python
# example3.py

import string_func

some_string = "Hello, Universe!"

print(string_func.stringLength(some_string))
print(string_func.stringToLower(some_string))
print(string_func.stringToUpper(some_string))
```

现在语法短了很多，你可以看到 string_func 的行为就像它自己的模块一样。

所以，这基本上就是 \_\_init__.py 的作用！它允许您将目录视为 Python 模块。然后，您可以在 \_\_init__.py 文件中进一步定义导入，以使导入更简洁，或者您可以将文件留空。

## 调试导入问题
对于调试导入问题，我主要有 3 个技巧：
1. 使用交互式解释器（REPL）导入模块并查看是否得到了您所期望的结果。
2. 使用 `python -v -m my_scriptname.py` 启动您的脚本，然后检查输出以准确了解您的模块从何处导入。
3. 使用 Pycharm。Pycharm 出色的自省能力意味着您将立即知道您的模块是否被正确导入，因为如果没有，它会指示错误。它有时还会建议正确的更正。社区版是免费的，如果您是学生，您可以免费订阅他们的所有产品！

有关 Python 模块和包的更多信息，您可以查看 [Python 文档](https://docs.python.org/3/tutorial/modules.html)。

您还可以查看 David Beazley 的精彩 [Talk Python To Me 播客](https://talkpython.fm/episodes/show/12/deep-dive-into-modules-and-packages)，他在其中讨论了该主题，以及 [David 对同一主题的演讲](https://www.youtube.com/watch?v=0oTh1CXRaQ0)

与往常一样，如果您发现本文中有任何错误，请随时联系我


# Addition
[How to create a Python Package with \_\_init__.py](https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)
[What is `__init__.py` for in Python?](https://sentry.io/answers/what-is-init-py-for-in-python/)
[How to write python \_\_init__.py file for module](https://stackoverflow.com/questions/67100775/how-to-write-python-init-py-file-for-module)