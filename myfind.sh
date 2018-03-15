#!/bin/bash
# 查找内容脚本
if [ "$#" -eq "3" ];then
    find $1 -name $2|xargs grep -ri $3
    exit
fi
if [ "$#" -eq "2" ];then
    find $1 -name $2
    exit
fi
ls $1
