# AutoRepoSlicer--自动化的仓库克隆与代码分片系统

## 项目简介

此项目旨在简化模型微调的数据集构建，自动完成仓库克隆、代码提取和分片，以便更轻松地组织代码数据。

## 功能清单

- [x] 支持传入仓库地址，自动克隆至本地
- [x] 支持遍历某个仓库的代码结构，并提取出所有.cj源代码
- [x] 支持按函数体进行分片并导出为jsonl格式
- [ ] 支持一次性传入多个仓库地址
- [ ] 使用flask，构建api服务
- [ ] 封装为一个docker容器，便于服务部署

## 如何使用

首先，克隆本仓库至你的本地

``` shell
git clone https://github.com/JimmyPowell/AutoCodeSlicer
```
然后，在项目根目录下运行以下代码来安装所依赖的库
```shell
pip install -r requirements.txt
```
然后运行main.py，输入仓库地址即可。处理好后的文件以jsonl的格式保存在了output文件夹下。


### 注：对于Linux用户，建议使用虚拟环境的运行方式

### 使用虚拟环境运行程序：

首先确保系统已经安装了python和nenv模块。你可以通过以下指令安装
``` shell
sudo apt update
sudo apt install python3 python3-venv
```

在项目根目录下，创建一个虚拟环境
``` shell
python3 -m venv myenv
```
激活虚拟环境
``` shell
source myenv/bin/activate
```
在虚拟环境中安装依赖
``` shell
pip install -r requirements.txt
```
运行main.py
```shell
python3 main.py
```
退出虚拟环境：
``` shell
deactivate
```