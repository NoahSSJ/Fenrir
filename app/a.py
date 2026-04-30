# 模拟 Scrapy 架构实现

# 1. Item 类：存储数据的容器
class CommentItem:
    def __init__(self, id, name, text, time):
        self.id = id
        self.name = name
        self.text = text
        self.time = time
    
    def __repr__(self):
        return f"CommentItem(id={self.id}, name={self.name}, text={self.text}, time={self.time})"

# 2. Pipeline 类：处理 Item 的组件
class CommentPipeline:
    def process_item(self, item):
        """处理接收到的 Item"""
        print(f"Pipeline 处理 Item: {item}")
        # 这里可以添加保存到数据库、文件等逻辑
        print(f"保存评论到数据库: ID={item.id}, 用户名={item.name}")
        return item

# 3. Spider 类：生成 Item 的组件
class TestSpider:
    def parse(self):
        """生成数据并 yield Item"""
        comments_data = [
            {"id": 1, "name": "用户1", "text": "这是第一条评论", "time": "2026-04-25 10:00:00"},
            {"id": 2, "name": "用户2", "text": "这是第二条评论", "time": "2026-04-25 10:05:00"},
            {"id": 3, "name": "用户3", "text": "这是第三条评论", "time": "2026-04-25 10:10:00"},
        ]
        
        for data in comments_data:
            # yield Item，模拟 Scrapy 的行为
            yield CommentItem(
                id=data["id"],
                name=data["name"],
                text=data["text"],
                time=data["time"]
            )

# 4. Engine 类：协调 Spider 和 Pipeline
class Engine:
    def __init__(self, spider, pipelines):
        self.spider = spider
        self.pipelines = pipelines
    
    def run(self):
        """运行爬虫并处理 Item"""
        print("开始运行爬虫...")
        # 获取 Spider 生成的 Item 生成器
        items = self.spider.parse()
        # 遍历生成的 Item 并通过 Pipeline 处理
        for item in items:
            # 依次通过每个 Pipeline 处理 Item
            for pipeline in self.pipelines:
                item = pipeline.process_item(item)
        print("爬虫运行完成!")

# 5. 测试运行
if __name__ == "__main__":
    # 实例化组件
    spider = TestSpider()
    pipeline = CommentPipeline()
    engine = Engine(spider, [pipeline])
    
    # 运行引擎
    engine.run()