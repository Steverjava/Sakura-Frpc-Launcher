import platform
import time
import requests

print("Welcome to tools that automate FRPC deployment on individual systems.\n You ready?")  # 询问用户是否开始
parameter = input("[y/n]")
if parameter == "y":
    pass
else:
    exit()

print("Now we are examining your computer system and its architecture.")  # 告知用户检测信息
System = platform.system()
Machine = platform.machine()
for parameter in range(4):
    time.sleep(0.5)
    print("... ", end="")
print("... ")
time.sleep(2)
print("Your operating system is", System, ".")
print("Your CPU architecture is", Machine, ".")

while True:
    if System == "Windows":  # Windows类
        time.sleep(2)
        path = input("Please select a file storage location.")  # 获取路径
        if path.isspace() is False:  # 判断路径合法性
            pass
        else:
            print("Do you want to quit?\n[y/n]")
            parameter = input("")
            if parameter == "y":
                exit()
            if parameter == "n":
                continue
        print("Downloading...")
        if Machine == "x86":  # 32bit
            file_all_path = path + "/frpc_windows_386.exe"  # 全路径
            url = "https://nya.globalslb.net/natfrp/client/frpc/0.45.0-sakura-7/frpc_windows_386.exe"  # 下载地址
            file = requests.get(url)  # 下载文件
            open(file_all_path, "wb").write(file.content)  # 保存文件
            file_name = "frpc_windows_386.exe"  # 文件名字
        elif Machine == "AMD64":  # 64bit
            file_all_path = path + "/frpc_windows_amd64.exe"
            url = "https://nya.globalslb.net/natfrp/client/frpc/0.45.0-sakura-7/frpc_windows_amd64.exe"
            file = requests.get(url)
            open(file_all_path, "wb").write(file.content)
            file_name = "frpc_windows_amd64.exe"
        elif Machine == "ARM64":  # ARM
            file_all_path = path + "/frpc_windows_arm64.exe"
            url = "https://nya.globalslb.net/natfrp/client/frpc/0.45.0-sakura-7/frpc_windows_arm64.exe"
            file = requests.get(url)
            open(file_all_path, "wb").write(file.content)
            file_name = "frpc_windows_arm64.exe"
        else:  # 没有的类别
            print("Not supported.")
            print("Do you want to quit?\n[y/n]")
            parameter = input("")
            if parameter == "y":
                exit()
            if parameter == "n":
                continue
    time.sleep(1)
    print("The download is complete!")
    break

Token = input("Please enter your access key(Token).")  # 获得秘钥
while True:
    if Token.isalnum() is False:  # 秘钥合法性
        print("Do you want to quit?\n[y/n]")
        parameter = input("")
        if parameter == "y":
            exit()
        if parameter == "n":
            continue
    else:
        break

ID_list = list()  # 创建列表
while True:  # 写入循环
    temp = input("Enter the tunnel ID you want to start.")  # 将ID存入temp
    if not temp:  # 输入空格
        print("Do you want to exit the loop?\n[y/n]")
        parameter = input("")
        if parameter == "y":
            break
        if parameter == "n":
            continue
    else:  # 有内容
        if temp.isnumeric() is True:  # 输入合法
            temp = int(temp)  # 转成整数
            ID_list.append(temp)  # 加入进列表
        else:
            continue

List_variables = ""  # 多开隧道输出变量
Loop_parameters = 1  # 次数函数
long = len(ID_list)  # 列表长度
while True:  # 循环-总
    number = input("How many tunnels do you want to open?")  # 开启数量
    number = str(number)  # 转成字符串
    if number.isnumeric() is True:  # 开启数量是否合法
        number = int(number)  # 转成整数
        if number <= 0:  # 开启数量不正确
            continue
        elif number == 1:  # 合法-单开
            print("Entering single-open mode.")
            print("Please select the tunnel you want to open ( 1 -", long, ").")
            print(ID_list)
            Serial_Number = input("")  # 获得隧道序号
            if Serial_Number.isnumeric() is True:  # 序号合法
                Serial_Number = int(Serial_Number)  # 转成整数
                Serial_Number = Serial_Number - 1  # 匹配列表序号法则
                if Serial_Number > long:  # 序号在列表外
                    continue
                else:  # 序号在列表内
                    List_variables = ID_list[Serial_Number]  # 将列表对应元素写入变量
                    List_variables = str(List_variables)  # 转成字符串
                    print(List_variables)
                    break
            else:  # 序号不合法
                print("Do you want to quit?\n[y/n]")
                parameter = input("")
                if parameter == "y":
                    break
                if parameter == "n":
                    continue
        else:  # 合法-多开
            print("Entering multi-open mode.")
            for parameter in range(number):  # 进入多开循环
                print(ID_list)
                print("Please select the tunnel you want to open ( 1 -", long, ").")
                Serial_Number = input("")  # 获得隧道序号
                if Serial_Number.isnumeric() is True:  # 序号合法
                    Serial_Number = int(Serial_Number)  # 转成整数
                    Serial_Number = Serial_Number - 1  # 匹配列表序号法则
                    if Serial_Number > long:  # 序号在列表外
                        continue
                    else:  # 序号在列表内
                        if Loop_parameters != number:  # 不是第一次写入
                            temp = ID_list[Serial_Number]  # 将列表对应元素写入变量
                            temp = str(temp)  # 转成字符串
                            List_variables = temp + "," + List_variables  # 为变量添加隔断
                            Loop_parameters = Loop_parameters + 1
                        else:  # 第一次写入
                            temp = ID_list[Serial_Number]  # 将列表对应元素写入变量
                            temp = str(temp)  # 转成字符串
                            List_variables = List_variables + temp  # 刷新变量
                            Loop_parameters = Loop_parameters + 1
                else:  # 序号不合法
                    print("Do you want to quit?\n[y/n]")
                    parameter = input("")
                    if parameter == "y":
                        break
                    if parameter == "n":
                        continue
            print(List_variables)
            break
        break
    else:  # 开启数量不合法
        continue
