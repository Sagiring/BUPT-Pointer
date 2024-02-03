import requests
import base64
from lxml import etree
import time


def PingJwgl():
    jwgl_url =  'https://jwgl.bupt.edu.cn/jsxsd/'
    try:
        res = requests.get(jwgl_url)
    except Exception:
        return False
    return True
   
        
    
def loginJwgl(ACCOUNT,PASSWD):
    data = {
    'userAccount':ACCOUNT,
    'userPassword':'',
    'encoded':base64.b64encode(ACCOUNT.encode()) + b"%%%" + base64.b64encode(PASSWD.encode())
    }
    headers = {
    'sec-ch-ua-platform': "Windows",
    'Host': 'jwgl.bupt.edu.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
    jwgl_url =  'https://jwgl.bupt.edu.cn/jsxsd/'
    login_url = 'https://jwgl.bupt.edu.cn/jsxsd/xk/LoginToXk'
    login_session = requests.Session()
    login_session.headers = headers
    res = login_session.get(jwgl_url)
    login_res = login_session.post(login_url,data=data)
    login_tree = etree.HTML(login_res.content.decode())
    title_login = login_tree.xpath('/html/head/title')[0].xpath('./text()')[0]
    
    if title_login == '登录':
        return False,False
    elif title_login == '教学一体化服务平台':
        accountName = login_tree.xpath('/html/body/div/div[1]/div[2]/div[3]/span[2]')[0].xpath('./text()')[0]
        return login_session,accountName
    else:
        return False,False



def getClassPoint(login_session, ACCOUNT, TIME_ID):
    
    class_table_url = f'https://jwgl.bupt.edu.cn/jsxsd/xskb/tzdkbcx_query_10013?&xs0101id={ACCOUNT}&xnxq01id={TIME_ID}'
    # print(class_table_url)
    class_table_res = login_session.get(class_table_url)
    sel = etree.HTML(class_table_res.content.decode())
    class_num = len(sel.xpath('/html/body/div/form/table/tr'))
    class_dict = {}
    for i in range(2,class_num + 1):
        class_id = sel.xpath(f'/html/body/div/form/table/tr[{i}]/td[1]')[0].xpath('./text()')[0].replace(' ','').replace('\r\n','')
        class_name = sel.xpath(f'/html/body/div/form/table/tr[{i}]/td[4]')[0].xpath('./text()')[0].replace(' ','').replace('\r\n','')
        class_Spoint = sel.xpath(f'/html/body/div/form/table/tr[{i}]/td[5]')[0].xpath('./text()')[0].replace(' ','').replace('\r\n','')
        class_pointer_url = f'https://jwgl.bupt.edu.cn/jsxsd/kscj/pscj_list.do?zcj=1&jx0404id={class_id}'

        class_point_res = login_session.get(class_pointer_url)
        pointerTree = etree.HTML(class_point_res.content.decode())

        point = []
        for index in range(2,12):
            try:
                pointData = pointerTree.xpath(f'//*[@id="dataList"]/tr[2]/td[{index}]')[0].xpath('./text()')[0]
                point.append(pointData)
            except IndexError:
                point.append('0')
        time.sleep(0.2)
        class_dict[class_id] = [class_name,class_Spoint,point]
    

    return class_dict

if __name__ == '__main__':
    print(PingJwgl())
 