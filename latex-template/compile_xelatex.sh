#!/bin/bash
echo "开始使用XeLaTeX编译LaTeX文档..."
xelatex main.tex
if [ $? -eq 0 ]; then
    echo "第一次编译完成，开始编译参考文献..."
    bibtex main
    echo "参考文献编译完成，第二次编译..."
    xelatex main.tex
    echo "第二次编译完成，第三次编译..."
    xelatex main.tex
    echo "编译完成！PDF文件已生成：main.pdf"
else
    echo "编译失败，请检查错误信息"
fi
