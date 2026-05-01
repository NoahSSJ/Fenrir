import dm_pb2

# 创建一个空容器
danmaku_seg = dm_pb2.DmSegMobileReply()

# 读取 .pb 文件并解析
with open('bullet_screen.pb', 'rb') as f:
    danmaku_seg.ParseFromString(f.read())

# 打印弹幕
print(f'一共 {len(danmaku_seg.elems)} 条弹幕\n')

for elem in danmaku_seg.elems:
    print(f'时间: {elem.progress}ms | 内容: {elem.content}')