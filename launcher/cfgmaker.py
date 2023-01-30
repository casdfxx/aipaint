args_ok = ""

bat_content = '''@echo off
set TRANSFORMERS_CACHE=.cache\\huggingface\\transformers
set XDG_CACHE_HOME=.cache
set MATPLOTLIBRC=.cache

set GIT=git\\bin\\git.exe
set GIT_PYTHON_GIT_EXECUTABLE=git\\bin\\git.exe
set PYTHON=py310\\python.exe
set COMMANDLINE_ARGS=<args>

%PYTHON% launch.py
pause
exit /b'''

def end():
    print(f"最终使用的启动参数: {args_ok}")
    final = bat_content.replace("<args>", args_ok)
    with open("A启动脚本.bat", "w", encoding="utf-8") as f:
        f.write(final)
    print("生成完成~ 请使用A启动脚本.bat启动")

print('''
============================
    webui启动脚本生成器
============================
本生成脚本运行一次即可，无需多次运行。

请先选择你的显存大小

1) 4G 及以下
2) 6G
3) 8G 及以上
4) 我没有Nvidia的独立显卡，使用CPU生成
''')

vram_choice = input("请输入上面的数字后按回车: ")

if vram_choice == "1":
    args_ok += "--lowvram "
elif vram_choice == "2":
    args_ok += "--medvram "
elif vram_choice == "3":
    pass
elif vram_choice == "4":
    args_ok += "--use-cpu all --precision full --no-half --skip-torch-cuda-test"
    end()
    exit(0)
else:
    print("选择的不对捏 重开吧!")
    exit(0)

print('''
=============================================
           请选择你需要的启动参数

===================常用参数===================
1) deepdanbooru (识别tag用, 训练可能会用到)
2) xformers (可能会让你生成图片变快)
3) 16系显卡生成图片黑的选我 (单精度)

================一般不用的参数，没事别选================
4) --no-half-vae (生成超大图防止黑图, 拖慢生成速度一般不要选这个)
5) --listen 允许公网访问
6) --api 启用api (如果你搭建bot, 需要选择这个)
7) --disable-safe-unpickle (!!!! 不安全的加载模型方式，部分大模型必须开启这个选项才可以加载，后果自负 !!!!)
提示: 如果你想同时选择1和2只需要输入12就可以了
''')

args_choice = input("请输入上面的数字后按回车(1-6): ")

arg_dic = {
    "1": "--deepdanbooru ",
    "2": "--xformers ",
    "3": "--precision full --no-half ",
    "4": "--no-half-vae ",
    "5": "--listen ",
    "6": "--api ",
    "7": "--disable-safe-unpickle "
}

for c in args_choice:
    if c in arg_dic:
        args_ok += arg_dic[c]
    else:
        print(f"无法识别这个参数: {c}")

end()