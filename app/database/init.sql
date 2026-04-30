-- 初始化数据库表结构
-- 如果表不存在则创建

CREATE TABLE IF NOT EXISTS followings (
    uid           STRING PRIMARY KEY,
    sec_uid       STRING UNIQUE,
    unique_id     STRING,
    short_id      STRING,
    nickname      TEXT,
    signature     TEXT,
    avatar_thumb  TEXT,
    aweme_count   TEXT,
    create_time   TEXT,                    
    insert_time   TEXT DEFAULT (datetime('now', 'localtime'))   
);

-- 可以继续添加其他表...
-- CREATE TABLE IF NOT EXISTS ... 

PRAGMA foreign_keys = ON;