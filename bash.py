# coding:utf-8
import os
import argparse

# 线上线下图床位置已经确定不变
path_offline = r"E:\我的坚果云\我的坚果云\博客图床\One-click-picgo\imgs" + '\\' # 本地图床目录
path_online = "https://raw.githubusercontent.com/your_github_id/repo_name/master/imgs/" # 线上图床目录

path_out = 'notes/' # 转换完成后的md文件保存路径
if not os.path.exists(path_out):
    os.mkdir(path_out)

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", help="the path of your md file")

if __name__ == '__main__':
    args = ap.parse_args()
    path_md = args.path

    # 被处理的md文件可以和本py文件处于同一目录，也可以处于py文件的下一级文件夹内
    if '\\' in path_md:
        folder, name = path_md.split('\\')
    else:
        name = path_md
    path_out_md = "notes\\" + name
    print("在线版markdown文件生成在目录：", path_out_md)

    with open(path_md, 'r', encoding='utf-8') as f: # 需要手动指定解码的格式
        lines = f.readlines()

    out = [l.replace(path_offline, path_online) for l in lines]

    with open(path_out_md, 'w', encoding='utf-8') as f:
        f.writelines(out)