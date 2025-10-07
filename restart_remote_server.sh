#!/bin/bash

# 脚本位于a文件夹中，假设当前目录为a
# 首先尝试结束之前正在运行的server_remote.py进程
pkill -f "server_remote.py" 2>/dev/null || true  # 忽略错误，如果没有进程则无事发生

# 等待一小会儿确保进程结束
sleep 1

# 使用uv在项目环境中后台运行server_remote.py
uv run server_remote.py > server_remote.log 2>&1 &

echo "server_remote.py running in background，PID: $!, log: server_remote.log"
