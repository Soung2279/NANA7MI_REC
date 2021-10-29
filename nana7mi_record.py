# -*- coding: utf-8 -*-
from time import time
import os, random, time
from nonebot import MessageSegment
from nonebot.exceptions import CQHttpError
import hoshino
from hoshino import Service, priv, R
from hoshino.util import FreqLimiter, DailyNumberLimiter

from . import nana7mi_recore_data

SONG_LIST = nana7mi_recore_data.NANA7MI_SONGS_DATA
SEXY_LIST = nana7mi_recore_data.SEXY_NANA7MI_RECORD_DATA
TRAIN_LIST = nana7mi_recore_data.TRAIN_SONGS_DATA
OTTO_LIST = nana7mi_recore_data.OTTOLANGUAGE_NANA7MI_DATA

_max = 30  #每日上限次数
_nlmt = DailyNumberLimiter(_max)
_cd = 3 # 调用间隔冷却时间(s)
_flmt = FreqLimiter(_cd)

MAX_WARN = f"我真的怀疑有些人闲的程度啊，你每天就搁这儿看着我了是吧，今天都听了{_max}条了，直播员也是楞啊"
CD_WARN = f"┭┮﹏┭┮呜哇~频繁使用的话bot会宕机的...再等{_cd}秒吧"
USE_BILIURL = True  #发送优质二创时是否附带发送原曲链接，True为附带False为不附带
SHOW_FILENAME = True  #发送语音时是否附带发送文件名，True为附带False为不附带

sv_help = '''
♥~是可爱小七海捏~♥

- [来点不能转的/来点优质二创 + 数字编号]   发一首娜娜米的优质二创，如果不加编号则随机发送

- [不能转的列表/娜娜米单曲列表]   查看优质二创列表

- [来点滑了/来点烧0娜娜米]   发一点娜娜米的怪叫合集（滑了~~嘿嘿~~嘿嘿） ##慎用！

- [来点小火车/来点铁轨难题]   发经典小火车，包括小火车的其它版本

- [来点古神语]   发点娜娜米台词回古神语

- [来点可爱小七海]   随机发送语音，选取范围不含小火车/怪叫/二创/古神语

- [来点可爱大七海]   随机发送语音，选取范围包含所有项目

- [更多小七海]   查看bot语音收藏来源

七海Nana7mi 主页：https://space.bilibili.com/434334701
'''.strip()

sv = Service(
    name = '可爱小七海',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.ADMIN, #管理权限
    visible = True, #False隐藏
    enable_on_default = True, #是否默认启用
    bundle = 'nana7mi', #属于哪一类
    help_ = sv_help #帮助文本
    )

@sv.on_fullmatch(["帮助可爱小七海", "帮助小七海", "帮助七海语音"])
async def bangzhu_nnm(bot, ev):
    await bot.send(ev, sv_help)

'''- 如有需要，在下方更改文件路径 -'''

#随机优秀二创(不能转的)/鬼畜歌曲
nana7mi_songs_folder = R.get('record/nana7mi/精品单曲/').path
def nnm_random_songs():
    files = os.listdir(nana7mi_songs_folder)
    filename = random.choice(files)
    rec = R.get('record/nana7mi/精品单曲/', filename)
    return rec, filename
#随机怪叫(本音小七海)合集
sexy_nana7mi_folder = R.get('record/nana7mi/怪叫/').path
def nnm_random_sexys():
    files = os.listdir(sexy_nana7mi_folder)
    filename = random.choice(files)
    rec = R.get('record/nana7mi/怪叫/', filename)
    return rec, filename
#随机各种小火车
train_folder = R.get('record/nana7mi/小火车/').path
def nnm_random_trains():
    files = os.listdir(train_folder)
    filename = random.choice(files)
    rec = R.get('record/nana7mi/小火车/', filename)
    return rec, filename
#随机七海nana7mi特供古神语
ottolanguage_nana7mi_folder = R.get('record/nana7mi/古神语特辑/').path
def nnm_random_ottos():
    files = os.listdir(ottolanguage_nana7mi_folder)
    filename = random.choice(files)
    rec = R.get('record/nana7mi/古神语特辑/', filename)
    return rec, filename
#随机各种七海切片语音
record_nnm_folder = R.get('record/nana7mi/切片语音').path
def nnm_random_recs():
    files = os.listdir(record_nnm_folder)
    filename = random.choice(files)
    rec = R.get('record/nana7mi/切片语音', filename)
    return rec, filename

#汇总所有文件夹路径
allnnm_folder = (nana7mi_songs_folder,sexy_nana7mi_folder,train_folder,ottolanguage_nana7mi_folder,record_nnm_folder)



@sv.on_prefix(("来点不能转的", "来点优质二创", "发点不能转的"))
async def send_nnmsongs(bot, ev) -> MessageSegment:
    uid = ev['user_id']
    if not _flmt.check(uid):
        await bot.send(ev, CD_WARN, at_sender=True)
        return
    _flmt.start_cd(uid)
    input = ev.message.extract_plain_text()
    all_songs_count = int(len(SONG_LIST))
    search_range = range(1, all_songs_count)

    if not _nlmt.check(uid):
        data = {
            "type": "share",
            "data": {
                "url": "https://live.bilibili.com/21452505",
                "title": "七海Nana7mi的直播间 - 哔哩哔哩直播",
                "content": "每天晚上21:00开播 除了周一是24:00开播！"
                }
            }
        await bot.send(ev, MAX_WARN, at_sender=True)
        await bot.send(ev, data)
        return
    _nlmt.increase(uid)

    if not input:  #不接参数时随机发送
        songs_num = random.randint(1, all_songs_count)
        Song_name = SONG_LIST[songs_num][0]  #获取文件名
        Url = SONG_LIST[songs_num][1]  #获取原曲链接
        Title = SONG_LIST[songs_num][2]  #获取原视频标题    
        Content = SONG_LIST[songs_num][3]  #获取评价
        share_data_a = {
            "type": "share",
            "data": {
                "url": f"{Url}",
                "title": f"{Title}",
                "content": f"{Content}"
                }
            }
        songs_output_a = R.get('record/nana7mi/精品单曲/', Song_name)
        final_send = MessageSegment.record(f'file:///{os.path.abspath(songs_output_a.path)}')
        await bot.send(ev, final_send)
        if USE_BILIURL is True:
            await bot.send(ev, share_data_a)
            return
        else:
            await bot.send(ev, f"对于此作品，我的评价是：{Content}")
            return

    if int(input) in search_range:  #当参数在编号范围内时
            nums = int(input)
            Song_name = SONG_LIST[nums][0]  #获取文件名
            Url = SONG_LIST[nums][1]  #获取原曲链接
            Title = SONG_LIST[nums][2]  #获取原视频标题    
            Content = SONG_LIST[nums][3]  #获取评价
            share_data_b = {
                "type": "share",
                "data": {
                    "url": f"{Url}",
                    "title": f"{Title}",
                    "content": f"{Content}"
                    }
                }
            songs_output_b = R.get('record/nana7mi/精品单曲/', Song_name)
            final_send = MessageSegment.record(f'file:///{os.path.abspath(songs_output_b.path)}')
            await bot.send(ev, final_send)
            if USE_BILIURL is True:
                await bot.send(ev, share_data_b)
            else:
                await bot.send(ev, f"对于此作品，我的评价是：{Content}")
    else:
        await bot.send(ev, f"编号不在范围内哦！当前范围1-{all_songs_count}")
        return


@sv.on_fullmatch(["不能转的列表", "不能转的编号", "娜娜米单曲列表", "nana7mi单曲列表"])
async def idlist_song(bot, ev):
    vlist = []
    for k, v in SONG_LIST.items():
        vlist.append(k)
        vlist.append(v[2])
        vlist.append('################')
        final = f"{vlist}"  #粗糙的排版，能用就行OTZ
    await bot.send(ev, final)


@sv.on_fullmatch(["来点滑了", "来点烧0娜娜米", "来点烧0nana7mi", "来点入脑", "来点娜娜米怪叫", "来点nana7mi怪叫", "发点怪叫"])
async def send_nnmsexy(bot, ev) -> MessageSegment:
    uid = ev['user_id']
    voice_list = []
    voice_list = nnm_random_sexys()
    voice_name = voice_list[1]
    sexy_rec = voice_list[0]

    if not _nlmt.check(uid):
        data = {
            "type": "share",
            "data": {
                "url": "https://live.bilibili.com/21452505",
                "title": "七海Nana7mi的直播间 - 哔哩哔哩直播",
                "content": "每天晚上21:00开播 除了周一是24:00开播！"
                }
            }
        await bot.send(ev, MAX_WARN, at_sender=True)
        await bot.send(ev, data)
        return
    _nlmt.increase(uid)

    try:
        final_send = MessageSegment.record(f'file:///{os.path.abspath(sexy_rec.path)}')
        await bot.send(ev, final_send)
        if SHOW_FILENAME is True:
            await bot.send(ev, voice_name)
    except CQHttpError:
        sv.logger.error("娜娜米怪叫语音发送失败。")


@sv.on_fullmatch(["来点小火车", "来点铁轨难题", "发点小火车"])
async def send_nnmtrain(bot, ev) -> MessageSegment:
    uid = ev['user_id']
    voice_list = []
    voice_list = nnm_random_trains()
    voice_name = voice_list[1]
    train_rec = voice_list[0]

    if not _nlmt.check(uid):
        data = {
            "type": "share",
            "data": {
                "url": "https://live.bilibili.com/21452505",
                "title": "七海Nana7mi的直播间 - 哔哩哔哩直播",
                "content": "每天晚上21:00开播 除了周一是24:00开播！"
                }
            }
        await bot.send(ev, MAX_WARN, at_sender=True)
        await bot.send(ev, data)
        return
    _nlmt.increase(uid)

    try:
        final_send = MessageSegment.record(f'file:///{os.path.abspath(train_rec.path)}')
        await bot.send(ev, final_send)
        if SHOW_FILENAME is True:
            await bot.send(ev, voice_name)
    except CQHttpError:
        sv.logger.error("小火车语音发送失败。")



@sv.on_fullmatch(["来点古神语", "来点otto语", "发点古神语"])
async def send_nnmotto(bot, ev) -> MessageSegment:
    uid = ev['user_id']
    if not _flmt.check(uid):
        await bot.send(ev, CD_WARN, at_sender=True)
        return
    _flmt.start_cd(uid)

    voice_list = []
    voice_list = nnm_random_ottos()
    voice_name = voice_list[1]
    otto_rec = voice_list[0]

    if not _nlmt.check(uid):
        data = {
            "type": "share",
            "data": {
                "url": "https://live.bilibili.com/21452505",
                "title": "七海Nana7mi的直播间 - 哔哩哔哩直播",
                "content": "每天晚上21:00开播 除了周一是24:00开播！"
                }
            }
        await bot.send(ev, MAX_WARN, at_sender=True)
        await bot.send(ev, data)
        return
    _nlmt.increase(uid)

    try:
        final_send = MessageSegment.record(f'file:///{os.path.abspath(otto_rec.path)}')
        await bot.send(ev, final_send)
        if SHOW_FILENAME is True:
            await bot.send(ev, voice_name)
    except CQHttpError:
        sv.logger.error("小火车语音发送失败。")



@sv.on_fullmatch(["来点可爱小七海", "来点可爱娜娜米", "发点可爱小七海", "发点可爱娜娜米"])
async def send_nnmlove(bot, ev):
    uid = ev['user_id']
    if not _nlmt.check(uid):
        data = {
            "type": "share",
            "data": {
                "url": "https://live.bilibili.com/21452505",
                "title": "七海Nana7mi的直播间 - 哔哩哔哩直播",
                "content": "每天晚上21:00开播 除了周一是24:00开播！"
                }
            }
        await bot.send(ev, MAX_WARN, at_sender=True)
        await bot.send(ev, data)
        return
    _nlmt.increase(uid)


    voice_list = []
    voice_list = nnm_random_recs()
    voice_name = voice_list[1]
    minrec_rec = voice_list[0]

    try:    
        final_send = MessageSegment.record(f'file:///{os.path.abspath(minrec_rec.path)}')
        await bot.send(ev, final_send)
        if SHOW_FILENAME is True:
            await bot.send(ev, voice_name)
    except CQHttpError:
        sv.logger.error("切片语音发送失败。")



@sv.on_fullmatch(["来点可爱大七海", "发点可爱大七海", "发点七海nana7mi", "来点七海nana7mi"])
async def send_random_allnnm(bot, ev):
    uid = ev['user_id']
    if not _flmt.check(uid):
        await bot.send(ev, CD_WARN, at_sender=True)
        return
    _flmt.start_cd(uid)

    if not _nlmt.check(uid):
        data = {
            "type": "share",
            "data": {
                "url": "https://live.bilibili.com/21452505",
                "title": "七海Nana7mi的直播间 - 哔哩哔哩直播，二次元直播平台",
                "content": "每天晚上21:00开播 除了周一是24:00开播！"
                }
            }
        await bot.send(ev, MAX_WARN, at_sender=True)
        await bot.send(ev, data)
        return

    _nlmt.increase(uid)

    select_fd = random.choice(allnnm_folder)
    files = os.listdir(select_fd)
    filename = random.choice(files)
    await bot.send(ev, f"[CQ:record,file=file:///{select_fd}/{filename}]")
    if SHOW_FILENAME is True:
        await bot.send(ev, filename)


@sv.on_fullmatch(["更多小七海"])
async def collection_nnm(bot, ev):
    data = {
        "type": "share",
        "data": {
            "url": "https://space.bilibili.com/34763008/favlist?fid=1335400608&ftype=create",
            "title": "松尧尧尧尧尧尧的收藏夹【切片】 - 哔哩哔哩",
            "content": "创建者：松尧尧尧尧尧尧 - 公开"
            }
        }
    await bot.send(ev, "更多内容可以前往我的B站收藏夹哦~")
    await bot.send(ev, data)
