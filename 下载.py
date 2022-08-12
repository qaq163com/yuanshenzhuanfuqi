import time
import requests
print("依赖包正在下载，请千万不要关闭此窗口")
def downloader(url, path, title):
    start = time.time()
    size = 0
    res = requests.get(url, stream=True)

    chunk_size = 1024 # 每次下载数据大小
    content_size = int(res.headers["content-length"]) # 总大小
    if res.status_code == 200:
        print('[%s 文件大小]: %0.2f MB' % (title, content_size/chunk_size/1024))
        with open(path, 'wb') as f:
            for data in res.iter_content(chunk_size=chunk_size):
                f.write(data)
                size += len(data)  # 已下载文件大小
                # \r 指定第一个字符开始，搭配end属性完成覆盖进度条
                print('\r'+ '[下载进度]: %s%.2f%%' % ('>'*int(size*50/content_size), float(size/content_size*100)), end='')
        end = time.time()
        print('\n' + "全部下载完成！用时%s.2f秒" % (end - start))

if __name__ == '__main__':
    url=open("data/下载url",encoding="utf-8").read()
    path=open("data/下载后保存的位置",encoding="utf-8").read()
    downloader(url, path, title="")