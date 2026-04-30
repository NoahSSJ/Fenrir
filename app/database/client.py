import sqlite3
import mysql.connector
import redis
from dotenv import load_dotenv
import os
from minio import Minio
from minio.error import S3Error

load_dotenv()


class SQLiteConfig():
    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA journal_mode = WAL")

    def process_item(self, item):
        """处理 Item"""
        print(f"SQLite 处理 Item: {item}")
        
        # 检查并创建 followings 表
        self._create_followings_table()
        
        # 处理 FollowingsItem
        if hasattr(item, 'sec_uid') and hasattr(item, 'nickname'):
            try:
                # 插入数据，使用 INSERT OR IGNORE 避免重复插入
                sql = """
                INSERT OR IGNORE INTO followings 
                (avatar_thumb, nickname, sec_uid, signature, uid, unique_id, short_id, aweme_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
                self.cursor.execute(sql, (
                    item.avatar_thumb,
                    item.nickname,
                    item.sec_uid,
                    item.signature,
                    item.uid,
                    item.unique_id,
                    item.short_id,
                    item.aweme_count
                ))
                self.conn.commit()
                print(f"成功插入数据: {item.nickname}")
            except Exception as e:
                print(f"插入数据失败: {e}")
                self.conn.rollback()
        
        return item
    
    def _create_followings_table(self):
        """创建 followings 表（如果不存在）"""
        try:
            sql = """
            CREATE TABLE IF NOT EXISTS followings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                avatar_thumb TEXT,
                nickname TEXT,
                sec_uid TEXT UNIQUE,
                signature TEXT,
                uid TEXT,
                unique_id TEXT,
                short_id TEXT,
                aweme_count TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(f"创建表失败: {e}")
            self.conn.rollback()


class MysqlConfig():
    def __init__(self, host, password, user, database):
        self.host = host
        self.password =password
        self.user = user
        self.database = database
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password = self.password,
            database = self.database
        )
        self.cursor = self.conn.cursor()

class RedisConfig():
    def __init__(self, host, port, db, password):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.r = redis.StrictRedis(
            host = self.host,
            port = self.port,
            db = self.db,
            password = self.password
        )

class MinIOConfig():
    def __init__(self, host, port, access_key, secret_key):
        self.host = host
        self.port = port
        self.access_key = access_key
        self.secret_key = secret_key
        self.client = Minio(
            endpoint=f"{self.host}:{self.port}",
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=False
        )

    def create_bucket(self, bucket_name):
        try:
            self.client.make_bucket(bucket_name)
        except S3Error as err:
            if err.code == "BucketAlreadyExists":
                print("Bucket already exists")
            else:
                print(err)
    
    def upload_file(self, bucket_name, object_name, file_path):
        """上传文件"""
        try:
            # 确保存储桶存在
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
                print(f"Created bucket {bucket_name}")
            else:
                print(f"Bucket {bucket_name} already exists")
            # 上传文件
            with open(file_path, 'rb') as file_data:
                file_stat = os.stat(file_path)
                self.client.put_object(
                    bucket_name, 
                    object_name, 
                    file_data, 
                    file_stat.st_size
                )
            print(f"Uploaded {file_path} to {bucket_name}/{object_name}")
            return True
        except S3Error as err:
            print(f"S3 operation failed; {err}")
            return False

if __name__ == "__main__":
    minio_client = MinIOConfig(
        host=os.getenv("MINIO_HOST"),
        port=os.getenv("MINIO_PORT"),
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY")
    )
    minio_client.create_bucket("test")
    minio_client.upload_file("test", "test.txt", "test.txt")