#!/usr/local/bin/python3
#coding=utf-8

import re, sys, os, random, time, base64
import urllib.parse, urllib.request
import socket
import MySQLdb

timeout = 10
socket.setdefaulttimeout(timeout)

proxy_list = [
    {'ip':"222.217.99.129", 'port':"9000", 'type':"http"},
    {'ip':"59.53.92.7", 'port':"8090", 'type':"http"},
    {'ip':"58.83.224.217", 'port':"8080", 'type':"http"},
    {'ip':"218.247.244.155", 'port':"8080", 'type':"http"},
    {'ip':"59.173.247.162", 'port':"8888", 'type':"http"},
    {'ip':"125.39.93.68", 'port':"8888", 'type':"http"},
    {'ip':"221.2.80.126", 'port':"8888", 'type':"http"},
    {'ip':"221.235.205.66", 'port':"8090", 'type':"http"},
    {'ip':"220.181.159.60", 'port':"8080", 'type':"http"},
    {'ip':"218.247.244.23", 'port':"8888", 'type':"http"},
    {'ip':"218.241.153.43", 'port':"8080", 'type':"http"},
    {'ip':"125.39.93.69", 'port':"8888", 'type':"http"},
    {'ip':"211.144.76.7", 'port':"8181", 'type':"http"},
    {'ip':"58.53.192.218", 'port':"8123", 'type':"http"},
    {'ip':"222.92.141.155", 'port':"8090", 'type':"http"},
    {'ip':"59.108.53.1", 'port':"8080", 'type':"http"},
    {'ip':"203.93.28.166", 'port':"8080", 'type':"http"},
    {'ip':"60.190.189.214", 'port':"8123", 'type':"http"},
    {'ip':"59.36.183.178", 'port':"8081", 'type':"http"},
    {'ip':"121.11.149.250", 'port':"8081", 'type':"http"},
    {'ip':"212.50.244.8", 'port':"8081", 'type':"http"},
    {'ip':"216.113.208.185", 'port':"8081", 'type':"http"},
    {'ip':"220.181.159.23", 'port':"8080", 'type':"http"},
    {'ip':"59.44.204.198", 'port':"8088", 'type':"http"},
    {'ip':"221.2.174.164", 'port':"8082", 'type':"http"},
    {'ip':"178.135.59.142", 'port':"8090", 'type':"http"},
    {'ip':"202.57.4.124", 'port':"8089", 'type':"http"},
    {'ip':"211.100.52.196", 'port':"8090", 'type':"http"},
    {'ip':"211.144.76.58", 'port':"9000", 'type':"http"}
    ]
pinyin_list = ["a", "ai", "an",  "ao", "ba", "bai", "ban",  "bao", "bei",
                "ben", "bi",   "bo", "bu", "ca", "cai",
                "ce", "cha", 
                "che", "chi", "chu", 
                "ci", "cu", "cui", "cun",
                "da", "dai", "dan",  "dao", "de", "di",
                "die", "dun",  "dou", "du","dui", 
                "duo", "e", "en", "er", "fa", "fan", "fei", 
                "fo", "fu", "gai", "gan",  "gao", "ge", "gei",  
                "gou", "gu", "gua", "gui", "gun", "guo", "ha",
                "hai", "han", "hao", "he", "hei", "hen", "hou", "hu",
                "hua", "hui", "hun", "huo", "ji", "jia", 
                "jie", "jin", "jiu", "ju", "jue", "jun", "ka",
                "kai", "kan", "kao", "ke", "kou", "ku",
                "kua", "kui", "kun", "kuo", "la", "lai", "lan",
                "lao", "le", "lei", "li", "lie", "lin",
                "liu", "lo", "lou", "lu", "lun", "luo",
                "ma", "mai", "man", "mao", "me", "mei", "men", "mi", 
                "min","mo", "mu", "na", "nai", "nan",
                "nao", "ne", "nei", "ni",
                "niu", "nu", "nuo",
                "o", "ou", "pa", "pai", "pan",  "pao", "pei", "pi",
                "pin", "po",  "pu", "qi",
                "qin", "qiu", "qu", 
                "que", "qun", "ran", "rao", "re", "ren", "ri",  "ru",
                "rui", "run", "ruo", "sa", "sai", "san", "se", "sen",
                "sha",  "she", "tong", 
                "shi", "shu", 
                "si",  "sou", "su","sui", "sun", "suo", "ta", "tai", "tan", 
                "tao", "te", "ti", "tou", "tu",
                "tui", "tuo", "wa", "wai", "wan","wei", "wen",
                "wo", "wu", "xi", "xia",  "xie", "xin", 
                "xiu", "xu","xue", "xun", "ya", "yan", "yao", "ye", "yi", "yin",
                "you", "yu","yue", "yun", "za", "zai", "zan",
                "zao", "ze",  
                "zhe",  "zhi", "zhu",
                "zi",  "zou", "zu",
                "zui", "zun", "zuo"]
def request_domain(domain):
    have_error = True
    while have_error:
        try:
            url = 'http://pandavip.www.net.cn/check/check_ac1.cgi'
            user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)'
            values = {'domain' : domain}
            headers = {'User-Agent' : user_agent}
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data, headers)

            index = random.randint(0, len(proxy_list) - 1)
            proxy = proxy_list[index]

            if True:
                proxy_support = urllib.request.ProxyHandler({proxy['type'] : proxy['ip'] + ':' + proxy['port']})
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)

            response = urllib.request.urlopen(req)
            the_page = response.read().decode("utf-8")

        except Exception as e:
            have_error = True
            #proxy_list.pop(index)
            ##print(">>>>>>>>>>> EXCEPTION:  " + proxy['ip']+ " " + str(e))
        else:
            have_error = False

    else:
        return the_page

def construct_domain():
    domainList = []
    domainList.append({'pre': "doucube", 'ext': "com"})
    domainList.append({'pre': "doucube", 'ext': "net"})
    domainList.append({'pre': "doucube", 'ext': "org"})
    domainList.append({'pre': "doucube", 'ext': "cn"})

    for i in range(0, len(pinyin_list) - 1):
        if (i < 0):
             continue
        for j in range(0, len(pinyin_list) - 1):
            if (skip(pinyin_list[j])):
                continue;
            if (skip(pinyin_list[i])):
                break;
            domain_pre = pinyin_list[i] + pinyin_list[j]
            domainList.append({'pre': domain_pre, 'ext': "com"})

    return domainList

def skip(arg):
    skip_list = []
    if (skip_list.count(arg) != 0):
        return True
    else:
        return False

def main():

    conn = MySQLdb.connect(host='localhost', user='root', passwd='tSBneLS', db='domaindb')
    domains = construct_domain()

    for i in range(0, len(domains)):
        domain_full = domains[i]['pre'] + "." + domains[i]['ext']
        sql = "SELECT * FROM T_DOMAIN WHERE DOMAIN = '%s'" % domain_full
        cursor = conn.cursor()
        cursor.execute(sql)
        count = cursor.rowcount
        if (count > 0):
            continue
        result = request_domain(domain_full)
        cur_time        = str(time.strftime("%H:%M:%S", time.localtime()))
        #cursor = conn.cursor()
        if result.find("is not available") != -1:
            #print(cur_time + "\t" + domain_full + "\tOccupied!")
            sql = "INSERT T_DOMAIN (DOMAIN, STATUS, RESULT, GMT_CREATE, GMT_MODIFIED) VALUES ('%s', 1, '%s', now(), now())" % (domain_full, result)
        elif result.find("is available") != -1:
            #print(cur_time + "\t" + domain_full + "\tFREE! ------->$")
            sql = "INSERT T_DOMAIN (DOMAIN, STATUS, RESULT, GMT_CREATE, GMT_MODIFIED) VALUES ('%s', 2, '%s', now(), now())" % (domain_full, result)
        else:
            if not result.count('Domain exists'):
                #print(cur_time + "\t" + domain_full + "\t" + result)
                sql = "INSERT T_DOMAIN (DOMAIN, STATUS, RESULT, GMT_CREATE, GMT_MODIFIED) VALUES ('%s', 2, '%s', now(), now())" % (domain_full, result)
            else:
                sql = "INSERT T_DOMAIN (DOMAIN, STATUS, RESULT, GMT_CREATE, GMT_MODIFIED) VALUES ('%s', 1, '%s', now(), now())" % (domain_full, result)
        cursor.execute(sql)
        cursor.close()
        conn.commit()

    conn.close()
    
    

if __name__ == '__main__':
    main()
#    print(base64.b64decode(b'Q29weXJpZ2h0IChjKSAyMDEyIERvdWN1YmUgSW5jLiBBbGwgcmlnaHRzIHJlc2VydmVkLg==').decode())


