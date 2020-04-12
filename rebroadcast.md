# 关于

介绍如何在油管/YouTube上直播视频文件，本技术可以用来重播已经直播过的视频。

## 直播面板操作步骤

- 打开浏览器输入以下地址：https://www.youtube.com/live_dashboard?nv=1
- 修改直播相关的选项，例如图片(thumnail)、标题(title)、说明(description)、分类(category)、隐私(privacy)等
- 记录直播流名称 (stream name/key), 如：8hjb-wmrk-14w0-2pg7

## 命令行操作相关步骤

- 拷贝以下脚本内容到一个文件，如`streaming.sh`

```bash
#! /bin/bash
#
VBR="2500k"
FPS="30"
QUAL="medium"
YOUTUBE_URL="rtmp://x.rtmp.youtube.com/live2"

SOURCE=$1
KEY=$STREAMING_KEY

ffmpeg \
    -i "$SOURCE" -deinterlace \
    -vcodec libx264 -pix_fmt yuv420p -preset $QUAL -r $FPS -g $(($FPS * 2)) -b:v $VBR \
    -acodec libmp3lame -ar 44100 -threads 6 -qscale 3 -b:a 712000 -bufsize 512k \
    -f flv "$YOUTUBE_URL/$KEY"
```

- 设置环境变量 `export STREAMING_KEY=8hjb-wmrk-14w0-2pg7`，这里要替换你自己的key
- 开始直播 `sh streaming.sh test.mp4`, 这里你需要将test.mp4 替换成你自己的视频文件

## 观看直播

- 可以在当前的直播页面观看，你可以看到直播状态从OFFLINE很快会变成LIVE
- 或者也可以以观众的角度观看，只需到你自己的主页就能很容易找到正在直播的视频
