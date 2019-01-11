# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:09:05 2019

"""
from xml.dom import minidom

#打开xml
dom = minidom.parse('info.xml')

#得到文档元素对象
root = dom.documentElement

'''print(root.nodeName) #节点名称
print(root.nodeValue) #节点的值，只对文本节点有效
print(root.nodeType) #节点的类型
print(root.ELEMENT_NODE)'''

#获取任意标签名    
'''tagname = root.getElementsByTagName("browser")
print(tagname[0].tagName)

tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)

tagname = root.getElementsByTagName('province')
print(tagname[2].tagName)'''

#得到文档元素对象
'''logins = root.getElementsByTagName('login')     

#获取login标签的username属性值
username = logins[0].getAttribute("username")
print(username)

#获取login标签的password属性值
password = logins[0].getAttribute("password")
print(password)

username = logins[1].getAttribute("username")
print(username)
password = logins[1].getAttribute("password")
print(password)'''

#获得标签对之间的数据
provinces = dom.getElementsByTagName("province")
citys = dom.getElementsByTagName('city')

#获得第二个province标签对的值
p2 = provinces[1].firstChild.data
print(p2)

#获得第一个city标签对的值
c1 = citys[0].firstChild.data
print(c1)    

#获得第二个city标签对的值
c2 = citys[1].firstChild.data
print(c2)    
