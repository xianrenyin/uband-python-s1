#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup
  print tup[0:3]
  print tup[1:]
  # 是否存在某值
  print (1 in tup)####!!!!!
  print (8 in tup)
  
  # 赋值
  a,b,c,d = (1,2,3,4)
  print a
  print b
  print c
  print d
  print '---------------'

  # 遍历
  for item in tup:
    print item

  print '-----------enumerate----------'
  try:
    tup[2] =9
  except:
    print 'Do not support item assignment'


  print '-----------'
  print tup
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除

  
if __name__ == '__main__':
  main()

