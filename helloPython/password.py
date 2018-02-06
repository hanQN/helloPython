# -*- coding:utf-8 -*-
import os

class PASSWORD:
    def __init__(self):
        self.arr = ['_',0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.password0 = '43213_'
        
    
    def getPassword(self):
        output = open('passwords.txt','w')
        #output.write(str)
        for k1 in self.arr:
            for k2 in self.arr:
                for k3 in self.arr:
                    for k4 in self.arr:
                        for k5 in self.arr:
                            for k6 in self.arr:
                                key = str(k1)+str(k2)+str(k3)+str(k4)+str(k5)+str(k6)
                                #output.write(key+'\n')
    
    def test(self):
        for i in range(5):  
            print i  
        else:
            print '循环完整执行一次。'
        for j in range(6):
            for k in range(6): 
                print j, k  
                if j >= 3: 
                    print "内重循环即将被break"
                    break
            else:
                print "内重循环完整执行一次。"
        else:
            print "外重循环完整执行一次。"
                        
PASSWORD().test()