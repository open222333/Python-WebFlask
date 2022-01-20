#!/bin/sh
BASEDIR=$(dirname $0) # 取得當下檔案資料夾
file="$BASEDIR/local_python_env.sh"

if [ -f $file ]; then
    # 若檔案存在
    sh local_python_env.sh
    python main.py
else
    echo "$file"
    echo "No local_python_env.sh"
fi