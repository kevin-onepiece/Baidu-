### 不要用在线网站去转换mp3格式音频，用ffmpeg去转换
#### 将mp3转换为pcm
```
ffmpeg -y -i beidao.mp3 -acodec pcm_s161e -ac 1 -ar 16000 beidao.pcm
```
#### 将mp3转换为pcm
```
ffmpeg -y -i beidao.mp3 -acodec pcm_s16le -f s16le -ac 1 -ar 16000 beidao.wav
```
