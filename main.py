from urllib.request import *
import urllib.parse
import pickle
import requests
data={
	"username":"15411012141",
	"ac_id":"1",
	"save_me":"1",
	"ajax":"1"}
url="http://172.18.1.95:801/srun_portal_pc.php?ac_id=1&"
def login(url,data):
          data=urllib.parse.urlencode(data).encode("utf-8")


          get=urlopen(url,data)
          print(get.read().decode("utf-8"))
def logout(url,data):
          data=urllib.parse.urlencode(data).encode("utf-8")
          
          get=urlopen(url,data)
          print(get.read().decode("utf-8"))

if __name__=="__main__":
          num=int(input("请选择功能(1 校园网登录。2 校园网注销。0 退出程序）:"))
          
          data["password"]=str(input("请输入密码："))
          if num==1:
                    data["action"]="login"
                    login(url,data)
          if num==2:
                    data["action"]="logout"
                    logout(url,data)
          elif num==0:
                    exit()



          
