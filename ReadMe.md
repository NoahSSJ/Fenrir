# 多站点社媒agent

## 简介

本项目是一个爬虫+agent项目，用于从多个社媒平台采集数据并进行分析。

目前支持的社媒平台:抖音,b站,微博

待支持的社媒平台:小红书,推特,reddit,百度贴吧,知乎

目前本项目只是一个多站点社媒采集器,后续会添加AI Agent功能.

## 依赖

- python3.12
- nodejs v24.11.1

一键下载依赖
```
pip install requirements.txt
```

## 项目文件夹介绍

打开app文件夹

app/config: 配置文件夹
app/config/auth: 在这里填写自己的api key, cookies等信息
app/config/env: 环境变量文件,用于存储数据库等基础配置信息


app/controller: 控制器文件夹
engine: 引擎代码

core: 核心爬虫代码文件夹,在这里编写爬虫代码

database: 数据库文件夹,在这里编写数据库代码

download: 下载文件夹, 下载的文件都存在这里

mods: 插件文件夹,在这里编写插件代码,如拦截器,检查器等等
