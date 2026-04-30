import mysql.connector
from dotenv import load_dotenv
import os

# 加载环境变量
env_path = os.path.join(os.path.dirname(__file__), 'config', 'env', '.env.dev')
load_dotenv(env_path)

# 数据库连接配置
MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '1234')
MYSQL_DB = os.getenv('MYSQL_DB', 'bili')

def get_db_connection():
    """获取数据库连接"""
    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        charset='utf8mb4'
    )

def create_comments_table():
    """创建评论表（如果不存在）"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS comments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                comment_id INT NOT NULL,
                name VARCHAR(255) NOT NULL,
                text TEXT NOT NULL,
                time DATETIME NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            """
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

def save_comment(comment):
    """保存评论到数据库"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO comments (comment_id, name, text, time)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (comment['id'], comment['name'], comment['text'], comment['time']))
        conn.commit()
        print(f"评论已保存到数据库: ID={comment['id']}")
    finally:
        conn.close()

def generate_comments():
    """生成评论数据的生成器函数"""
    comments_data = [
        {"id": 1, "name": "用户1", "text": "这是第一条评论", "time": "2026-04-25 10:00:00"},
        {"id": 2, "name": "用户2", "text": "这是第二条评论", "time": "2026-04-25 10:05:00"},
        {"id": 3, "name": "用户3", "text": "这是第三条评论", "time": "2026-04-25 10:10:00"},
        {"id": 4, "name": "用户4", "text": "这是第四条评论", "time": "2026-04-25 10:15:00"},
        {"id": 5, "name": "用户5", "text": "这是第五条评论", "time": "2026-04-25 10:20:00"},
    ]
    
    for comment in comments_data:
        yield comment

def process_comments():
    """处理通过yield传递的评论数据"""
    # 创建评论表
    create_comments_table()
    
    print("开始处理评论数据:")
    for comment in generate_comments():
        print(f"评论ID: {comment['id']}, 用户名: {comment['name']}, 内容: {comment['text']}, 时间: {comment['time']}")
        # 保存到数据库
        save_comment(comment)
    print("评论数据处理完成!")

if __name__ == "__main__":
    process_comments()