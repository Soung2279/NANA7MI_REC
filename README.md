# NANA7MI-可爱小七海语音♥

→→→ [查看更新](#更新日志)

*****

## 简介

“你爱我♥我爱你♥我爱七海娜娜米~~~”

随时随地听 [七海Nana7mi](https://space.bilibili.com/434334701) 的语音条哦~

“ 这个好诶！”

不知道 **七海Nana7mi** 是谁？

<a href="https://baike.baidu.com/item/%E4%B8%83%E6%B5%B7Nana7mi/24150477?fr=aladdin">
  <img align="left" alt="Weibo" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@5.10.0/icons/baidu.svg" />

[七海Nana7mi - 百度百科](https://baike.baidu.com/item/%E4%B8%83%E6%B5%B7Nana7mi/24150477?fr=aladdin)
</a>

<a href="https://weibo.com/u/7198559139">
  <img align="left" alt="Weibo" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@5.10.0/icons/sinaweibo.svg" />

[七海Nana7mi的微博_微博](https://weibo.com/u/7198559139)
</a>

<a href="https://space.bilibili.com/434334701">
  <img align="left" alt="Bilibili" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@5.10.0/icons/bilibili.svg" />

[七海Nana7mi的个人空间_哔哩哔哩_Bilibili](https://space.bilibili.com/434334701)
</a>

<a href="https://zh.moegirl.org.cn/%E4%B8%83%E6%B5%B7(%E8%99%9A%E6%8B%9FUP%E4%B8%BB)#">
  <img align="left" alt="Bilibili" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@5.10.0/icons/youtube.svg" />

[七海 - 萌娘百科 万物皆可萌的百科全书](https://zh.moegirl.org.cn/%E4%B8%83%E6%B5%B7(%E8%99%9A%E6%8B%9FUP%E4%B8%BB)#)


适用于 [HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot) 的娱乐插件，群聊中发送 [七海Nana7mi](https://space.bilibili.com/434334701) 有关的 **切片语音/古神语/怪话合集/各种不能转的二创**
</a>
*****

## 安装
- **步骤一** : 直接下载/克隆本项目，将文件夹放入 ``hoshino/modules`` 路径下, 在 ``hoshino/config/__bot__.py`` 里的 ``MODULES_ON`` 中添加 "nana7mi"

```python
# 启用的模块
MODULES_ON = {
    'xxx',
    'nana7mi',  #注意英文逗号
    'xxx',
}
```

- **步骤二** : 在本页面 **[Releases](https://github.com/Soung2279/NANA7MI_REC/releases)** 处下载语音资源包，将语音资源放在 **Hoshinobot的资源库文件夹/record** 下，并重命名文件夹为 **“nana7mi”** ，该文件夹可在在 ``hoshino/config/__bot__.py`` 里的 ``RES_DIR`` 处修改

```python
# 资源库文件夹，需可读可写，windows下注意反斜杠转义
RES_DIR = r'X:/xxx/'
```

最终的路径应该呈现为：
``X:/xxx/record/nana7mi/... ``

或者

``./root/xxx/record/nana7mi/...``

如果Release下载速度不理想，可尝试下列途径：
<details>
  <summary>百度网盘</summary>

- [可爱小七海语音资源](https://pan.baidu.com/s/1PhuagtKJ4jvJmtVaAvkRaQ)
> 提取码：2279

</details>

<details>
  <summary>qq群文件</summary>

[SoungBot交流群（free edition](https://jq.qq.com/?_wv=1027&k=rKLpjTPz)
> 推荐在百度网盘不可用 or 下载过于缓慢的时候使用

</details>

- **步骤三** : 前往仓库 **[HoshinoBot增强-语音调用支持](https://github.com/Soung2279/advance_R)** 处下载 ``R.py`` ，并替换至 ``/hoshino`` 处。

<br>如果按照步骤正常安装，重启 HoshinoBot 即可开始使用本功能。</br>

*****

## 指令表

- **来点不能转的/来点优质二创 + 编号（当前1-19）**   发一首娜娜米的优质二创，如果不加编号则随机发送

- **不能转的列表/娜娜米单曲列表**   查看优质二创列表

- **来点滑了/来点烧0娜娜米**   发一点娜娜米的怪叫合集（滑了~~嘿嘿~~嘿嘿） ##慎用！

- **来点小火车/来点铁轨难题**   发经典小火车，包括小火车的其它版本

- **来点古神语**   发点娜娜米台词回古神语

- **来点可爱小七海**   随机发送语音，选取范围不含小火车/怪叫/二创/古神语

- **来点可爱大七海**   随机发送语音，选取范围包含所有项目

*****

## 额外说明

可在 ``nana7mi_record.py`` 的第32行，设置 发送语音（优质二创）时是否附带发送原曲链接

True为附带  False为不附带

```python
USE_BILIURL = True  #发送语音（优质二创）时是否附带发送原曲链接，True为附带False为不附带
```

语音文件的路径设置在 ``nana7mi_record.py`` 的第68-73行，若您有其它资源路径，请在此处进行更改

```python
nana7mi_songs_folder = R.rec('nana7mi/精品单曲/').path   #鬼畜歌曲的文件路径
sexy_nana7mi_folder = R.rec('nana7mi/怪叫/').path    #怪叫合集的文件路径
train_folder = R.rec('nana7mi/小火车/').path     #各种小火车的文件路径
ottolanguage_nana7mi_folder = R.rec('nana7mi/古神语特辑/').path  #七海nana7mi特供古神语
record_nnm_folder = R.rec('nana7mi/切片语音').path  #各种切片语音
```

本项目后续将保持更新，可在本页面 [更新日志](#更新日志) 与 Release 处 查看更新的资源内容。若您想自行添加更新，请按照 ``nana7mi_record_data.py`` 里的模板进行字典的添加。

```python
#若需更新本字典（如果本项目未重构），请按照以下格式更新：
#SONGS_DATA = {编号:["文件名","原曲链接","原视频标题","评价"]}
vtbName_SONGS_DATA = {ID:["filename","url","title","content"]}
#以下是示范例
NANA7MI_SONGS_DATA = {
8:["你爱我我爱你我爱七海娜娜米.mp3","https://www.bilibili.com/video/BV1af4y1b7Ne/","我爱七海娜娜米♡","官  方  鬼  畜"],  #注意末尾逗号
}
```
*****

### 其它

本人非专业程序员，业余写着玩玩，代码很菜，大佬们看看就好QwQ。

made by [Soung2279@Github](https://github.com/Soung2279/)

### 鸣谢

[HoshinoBot项目地址](https://github.com/Ice-Cirno/HoshinoBot)

### 更新日志

##### 2021/9/19

首次上传

进行 Linux 环境的适配，资源包更新至2021-9-19.
