#!/bin/bash
# 取消注释图片引用的脚本
find chapters/ -name "*.tex" -exec sed -i "" "s/%\\includegraphics/\\includegraphics/g" {} \;
echo "图片引用已恢复"

