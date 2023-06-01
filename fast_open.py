
import os
import sys
import subprocess
import logging

# 设置日志级别和格式
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 设置脚本
python_script = "main.py"

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# #强制更新
# logging.info("获取最新代码")
# subprocess.check_call(["git", "pull"])

# #安装额外的仓库
# git_url = "https://github.com/OpenLMLab/MOSS.git"
# sub_dir = os.path.join("request_llm", "moss")
# if not os.path.exists(sub_dir):
#     subprocess.check_call(["git", "clone", git_url, sub_dir])
# else:
#     logging.info(f"{sub_dir} already exists, updating with git pull.")
#     subprocess.check_call(["git", "-C", sub_dir, "pull"])

	
# # 安装 requirements.txt 中指定版本的依赖项
# requirements_path = "requirements.txt"
# aliyun_pypi_mirror = "https://mirrors.aliyun.com/pypi/simple/"
# subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path, "-i", aliyun_pypi_mirror])

# # 安装 request_llm/requirements_chatglm.txt 中的依赖项
# logging.info("获取chatglm.txt 中的依赖项")
# requirements_chatglm_path = os.path.join("request_llm", "requirements_chatglm.txt")
# subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_chatglm_path])

# # 安装 request_llm/requirements_newbing.txt 中的依赖项
# logging.info("获取newbing.txt 中的依赖项")
# requirements_newbing_path = os.path.join("request_llm", "requirements_newbing.txt")
# subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_newbing_path])

# # 安装 request_llm/requirements_moss.txt 中的依赖项 复旦MOSS
# logging.info("获取moss.txt 中的依赖项")
# requirements_moss_path = os.path.join("request_llm", "requirements_moss.txt")
# subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_moss_path])


# # 安装指定版本的 torch, torchvision 和 torchaudio
# torch_stable_url = "https://download.pytorch.org/whl/cu121/torch_stable.html"
# subprocess.run([sys.executable, "-m", "pip", "install", "torch", "torchvision", "torchaudio", "-f", torch_stable_url])

subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pdfminer", "torchaudio", "beautifulsoup4"])

# 运行主 Python 脚本
subprocess.run([sys.executable, python_script])