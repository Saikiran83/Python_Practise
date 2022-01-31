#Health management system
client_list={1:"sai",2:"kiran",3:"sri"}
log_list={1:"exercise",2:"diet"}
def gettime():
    import datetime
    return datetime.datetime.now()

try:
    print("select client name")
    for k,v in client_list.items():
        print("Press",k,"for",v,"\n",end="")
    client_name=int(input())
    print("Press 1 for log")
    print("Press 2 for Retrieve")
    op = int(input())
    if op is 1:
        for k,v in log_list.items():
            print("Press",k,"for",v,"\n",end="")
        log_name = int(input())
        print("Selected Job:",log_list[log_name])
        f = open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")
        k='Y'
        while(k is not "N"):
            print("Enter", log_list[log_name],"\n", end="")
            mytext = input()
            f.write("["+str(gettime())+"]:"+mytext+"\n")
            k = input("Add More ? Y/N:")
            continue
        f.close()
    elif op is 2:
        for key,value in log_list.items():
            print("Press",key,"to retrieve",value,"\n",end="")
        log_Name = int(input())
        print(client_list[client_name],"-",log_list[log_Name],"Report:","\n", end="")
        f = open(client_list[client_name]+"_"+log_list[log_Name]+".txt","rt")
        contents = f.readline()
        for line in contents:
            print(line,end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")