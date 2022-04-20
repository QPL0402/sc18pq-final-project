import datetime
import Create
import Lastpath
def cal_time(startTime,endTime):
    startTime= datetime.datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S")
    endTime= datetime.datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S")
    # 相减得到秒数
    seconds = (endTime- startTime).seconds
    # 换算成时分秒
    m = 0
    m, s = divmod(seconds, 60)
    # h, m = divmod(m, 60)

    # res_time = '0'
    # if h==0:
    #     res_time = f'{m}m:{s}s'
    # else:
    #     res_time = f'{h}h:{m}m:{s}s'
    # print("%d:%02d:%02d" % (h, m, s))
    
    return int(m) if s>30 else m+1

# FIFO算法匹配过程
def match1(request1,request2):
    Create.lista()
    Lastpath.lastpath()
    if request1[0] != request2[0]:
        return 0,0,0
    
    elif request1[2] > request2[2]:# 包裹订单晚于乘客订单
        return 0,0,0

    else:
        t = 0
        t1,t2,t3,t_total = 3,0,0,0
        if request1[1] == request2[1]:  # 同起点同终点
            # for ii in range(len(Create.listpoi)):
            for n in range(len(Lastpath.lpath)):
                # 乘客的最短时间t2
                if request2[0] == Lastpath.lpath[n][0][0] and request2[1] == Lastpath.lpath[n][-1][0]:
                    t2 = Lastpath.lpath[n][-1][1]
                    t3 = 2  # 放下乘客后,放包裹假设2分钟
                    print('Passenger paths：Lastpath.lpath[n]:',Lastpath.lpath[n])
                    print('The path of the parcel (i.e. the passenger path)：Lastpath.lpath[n]:',Lastpath.lpath[n])
                    t_wait = cal_time(request1[2],request2[2])
                    t_total = t_wait+t1+t2+t3
                    print('t_wait:',t_wait,'\tt2:',t2,'\tt3:',t3,'\tt_total:',t_total)
            return 1,t_total,t3
        
        else:
            for i in range(len(Lastpath.lpath)):
                ## Calculate the delivery time of the package
                # 起点在第i个路径第1个地址的第1个位置, 终点在第i个路径最后1个地址的第1个位置
                if request1[0] == Lastpath.lpath[i][0][0] and request1[1] == Lastpath.lpath[i][-1][0]:
                    # print(Lastpath.lpath[i])
                    t = Lastpath.lpath[i][-1][1]-Lastpath.lpath[i][0][1]

            for ii in range(len(Create.listpoi)):
                tag_n = 0

                for n in range(len(Lastpath.lpath)):
                    # 乘客的最短时间t2
                    if request2[0] == Lastpath.lpath[n][0][0] and request2[1] == Lastpath.lpath[n][-1][0]:
                        t2 = Lastpath.lpath[n][-1][1]
                        tag_n = n

                if request2[1] == Create.listpoi[ii][0]:
                    for m in range(len(Lastpath.lpath)):
                        # 判断包裹距离目的地是否近
                        if request2[1] == Lastpath.lpath[m][0][0] and request1[1] == Lastpath.lpath[m][-1][0]:
                            t3 = Lastpath.lpath[m][-1][1]-Lastpath.lpath[m][0][1]
                            if(t3 < t):
                                print('Passenger paths：Lastpath.lpath[n]:',Lastpath.lpath[tag_n])
                                print('The route through which packages are transported when passengers arrive：Lastpath.lpath[m]:',Lastpath.lpath[m])
                                t_wait = cal_time(request1[2],request2[2])
                                t_total = t_wait+t1+t2+t3
                                print('t_wait:',t_wait,'\tt2:',t2,'\tt3:',t3,'\tt_total:',t_total)
                                print()
                                return 2,t_total,t3
                            else:
                                return 0,0,0

# DeCloser算法匹配过程
def match2(request1,request2):
    Create.lista()
    Lastpath.lastpath()
    if request1[0] != request2[0]:
        return 0,0,0
    
    elif request1[2] > request2[2]:# 包裹订单晚于乘客订单
        return 0,0,0

    else:
        t = 0
        t1,t2,t3,t_total = 3,0,0,0
        if request1[1] == request2[1]:  # 同起点同终点
            # for ii in range(len(Create.listpoi)):
            for n in range(len(Lastpath.lpath)):
                # 乘客的最短时间t2
                if request2[0] == Lastpath.lpath[n][0][0] and request2[1] == Lastpath.lpath[n][-1][0]:
                    t2 = Lastpath.lpath[n][-1][1]
                    t3 = 2  # 放下乘客后,放包裹假设2分钟
                    print('Passenger paths：Lastpath.lpath[n]:',Lastpath.lpath[n])
                    print('Package path (i.e. passenger path)：Lastpath.lpath[n]:',Lastpath.lpath[n])
                    t_wait = cal_time(request1[2],request2[2])
                    t_total = t_wait+t1+t2+t3
                    print('t_wait:',t_wait,'\tt2:',t2,'\tt3:',t3,'\tt_total:',t_total)
            return 1,t_total,t3
        
        else:
            for i in range(len(Lastpath.lpath)):
                ## Calculate the delivery time of the package
                # 起点在第i个路径第1个地址的第1个位置, 终点在第i个路径最后1个地址的第1个位置
                if request1[0] == Lastpath.lpath[i][0][0] and request1[1] == Lastpath.lpath[i][-1][0]:
                    # print(Lastpath.lpath[i])
                    t = Lastpath.lpath[i][-1][1]-Lastpath.lpath[i][0][1]

            for ii in range(len(Create.listpoi)):
                tag_n = 0

                for n in range(len(Lastpath.lpath)):
                    # 乘客的最短时间t2
                    if request2[0] == Lastpath.lpath[n][0][0] and request2[1] == Lastpath.lpath[n][-1][0]:
                        t2 = Lastpath.lpath[n][-1][1]
                        tag_n = n

                if request2[1] == Create.listpoi[ii][0]:
                    for m in range(len(Lastpath.lpath)):
                        # 判断包裹距离目的地是否近
                        if request2[1] == Lastpath.lpath[m][0][0] and request1[1] == Lastpath.lpath[m][-1][0]:
                            t3 = Lastpath.lpath[m][-1][1]-Lastpath.lpath[m][0][1]
                            if(t3 < t):
                                print('Passenger paths：Lastpath.lpath[n]:',Lastpath.lpath[tag_n])
                                print('The route through which packages are transported when passengers arrive：Lastpath.lpath[m]:',Lastpath.lpath[m])
                                t_wait = cal_time(request1[2],request2[2])
                                t_total = t_wait+t1+t2+t3
                                print('t_wait:',t_wait,'\tt2:',t2,'\tt3:',t3,'\tt_total:',t_total)
                                print()
                                return 2,t_total,t3
                            else:
                                return 0,0,0

# 因子算法匹配过程
def match3(request1,request2,alph,beta):
    Create.lista()
    Lastpath.lastpath()
    if request1[0] != request2[0]:
        return 0,0,0,0
    
    elif request1[2] > request2[2]:# 包裹订单晚于乘客订单
        return 0,0,0,0

    else:
        t = 0
        t1,t2,t3,t_total,t_yz = 3,0,0,0,0
        if request1[1] == request2[1]:  # 同起点同终点
            # for ii in range(len(Create.listpoi)):
            for n in range(len(Lastpath.lpath)):
                # 乘客的最短时间t2
                if request2[0] == Lastpath.lpath[n][0][0] and request2[1] == Lastpath.lpath[n][-1][0]:
                    t2 = Lastpath.lpath[n][-1][1]
                    t3 = 2  # 放下乘客后,放包裹假设2分钟
                    print('Passenger paths：Lastpath.lpath[n]:',Lastpath.lpath[n])
                    print('Package path (i.e. passenger path)：Lastpath.lpath[n]:',Lastpath.lpath[n])
                    t_wait = cal_time(request1[2],request2[2])
                    t_total = t_wait+t1+t2+t3
                    t_yz =  alph*t_total + beta*t_wait # alph*t_total + beta*t_wait
                    print('t_wait:',t_wait,'\tt2:',t2,'\tt3:',t3,'\tt_total:',t_total,f'\tt_yz:{t_yz:2f}')
            return 1,t_total,t3,t_yz
        
        else:
            for i in range(len(Lastpath.lpath)):
                ## Calculate the delivery time of the package
                # 起点在第i个路径第1个地址的第1个位置, 终点在第i个路径最后1个地址的第1个位置
                if request1[0] == Lastpath.lpath[i][0][0] and request1[1] == Lastpath.lpath[i][-1][0]:
                    # print(Lastpath.lpath[i])
                    t = Lastpath.lpath[i][-1][1]-Lastpath.lpath[i][0][1]

            for ii in range(len(Create.listpoi)):
                tag_n = 0

                for n in range(len(Lastpath.lpath)):
                    # 乘客的最短时间t2
                    if request2[0] == Lastpath.lpath[n][0][0] and request2[1] == Lastpath.lpath[n][-1][0]:
                        t2 = Lastpath.lpath[n][-1][1]
                        tag_n = n

                if request2[1] == Create.listpoi[ii][0]:
                    for m in range(len(Lastpath.lpath)):
                        # 判断包裹距离目的地是否近
                        if request2[1] == Lastpath.lpath[m][0][0] and request1[1] == Lastpath.lpath[m][-1][0]:
                            t3 = Lastpath.lpath[m][-1][1]-Lastpath.lpath[m][0][1]
                            if(t3 < t):
                                print('Passenger paths：Lastpath.lpath[n]:',Lastpath.lpath[tag_n])
                                print('The route through which packages are transported when passengers arrive：Lastpath.lpath[m]:',Lastpath.lpath[m])
                                t_wait = cal_time(request1[2],request2[2])
                                t_total = t_wait+t1+t2+t3
                                t_yz =  alph*t_total + beta*t_wait # alph*t_total + beta*t_wait
                                print('t_wait:',t_wait,'\tt2:',t2,'\tt3:',t3,'\tt_total:',t_total,'\tt_yz:',t_yz)
                                return 2,t_total,t3,t_yz
                            else:
                                return 0,0,0,0

                      




