from aip import AipSpeech
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

""" 你的 APPID AK SK """
APP_ID = '10446557'
API_KEY = 'RoTmKOyvGATGYBH2TWu1q9f39OHKDxQt'
SECRET_KEY = 'hwkKxOILCpRyvkjb5tvjr7BxhS60vMZ8'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
result = client.asr(get_file_content('qianzhongshu.pcm'), 'pcm', 16000, {
    'dev_pid': 1536
})

print(result)
