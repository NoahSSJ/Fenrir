class Engine():
    def __init__(self, spider, pipelines):
        self.spider = spider
        self.pipelines = pipelines
    def run(self):
        """运行爬虫并处理 Item"""
        print("开始运行爬虫...")
        # 获取 Spider 生成的 Item 生成器
        items = self.spider
        # 遍历生成的 Item 并通过 Pipeline 处理
        for item in items:
            # 依次通过每个 Pipeline 处理 Item
            for pipeline in self.pipelines:
                item = pipeline.process_item(item)
        print("爬虫运行完成!")