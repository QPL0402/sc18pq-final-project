import Topk
import time
import Create
import Lastpath
import order

import random
import time
random.seed(2)

def strTimeProp(start, end, prop, frmt):
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + prop * (etime - stime)
    return int(ptime)

def randomDate(start, end, frmt='%Y-%m-%d %H:%M:%S'):
    return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))
 
def randomDateList(start, end, n, frmt='%Y-%m-%d %H:%M:%S'):
    return [randomDate(start, end, frmt) for _ in range(n)]

if __name__ == '__main__':
    start = '2022-03-31 09:00:00'
    end = '2022-03-31 21:00:00'
    lenth = 100



    # 随机生成时间
    random_date_1 = randomDateList(start, end, lenth)
    random_date_1 = sorted(random_date_1)
    random_date_2 = randomDateList(start, end, lenth)
    random_date_2 = sorted(random_date_2)
    # print(random_date)

    # 随机生成乘客订单tr<起点to,终点td,申请时间tt>
    # 随机生成包裹订单pr<起点po,终点pd,申请时间pt>
    poi_list = ['a','b','c','d','e','f']
    tr = []
    pr = []
    for i in range(lenth):
        one_tr = random.sample(poi_list,2)
        one_tr.append(random_date_2[i])
        tr.append(one_tr)

        one_pr = random.sample(poi_list,2)
        one_pr.append(random_date_1[i])
        pr.append(one_pr)
    
    print('Passenger orders tr<starting point to,end point td,Order submission time tt>\n',tr)
    print('Package orders pr<starting point po,end point pd,Order submission time pt>\n',pr)

    Lastpath.lastpath()
    print('Lastpath.lpath:',Lastpath.lpath)

    print('=====Matching=====')
    begin = time.time()
    c = 1
    t_sum,t3_sum = 0,0

    tmp_pr = pr             # 临时的包裹订单
    for i in range(lenth):
        request2 = tr[i]    # 乘客订单
        
        matched_pr = []     # 已匹配上的包裹订单
        for j in range(len(tmp_pr)):
            request1 = tmp_pr[j]    # 包裹订单
            match_res = order.match1(request1, request2) # 匹配结果
            try:
                if match_res[0] == 1:
                    # print("match successfully!")
                    # print('[match] 乘客订单:',request2,'包裹订单:',request1)
                    matched_pr.append([request1,match_res[1],match_res[2]])
                elif match_res[0] == 2:
                    # print("match successful(transfer station)")
                    # print('[match] 乘客订单:',request2, '包裹订单:',request1)
                    matched_pr.append([request1,match_res[1],match_res[2]])
                else:
                    # print("match fail")
                    pass
            except:
                pass
        
        # FIFO先进先出(取matched_pr中第一个)
        if matched_pr:
            print(f'\n[match order{c}] Passenger orders:{request2},\nMatchable parcel orders:matched_pr:{matched_pr}')
            print('Matchting order of FIFO alogrithm:',matched_pr[0])
            print('==='*10)
            tmp_pr.remove(matched_pr[0][0])
            t_sum += matched_pr[0][1]
            t3_sum += matched_pr[0][2]
            c+=1
    end = time.time()
    print('\n【Evaluation】')
    print(f'The elapsed time of FIFO algorithm:{end-begin:.4f}s')
    print(f'Average (wait + shipping) time for matched package orders:{t_sum / c:.2f} minutes')
    print(f'Total (wait + shipping) time for matched package orders:{t_sum} minutes\nAverage time of parcel transport:{t3_sum/c:.2f} minutes')
    print(f'Order matching rate[{c}/{lenth}]={c/lenth:.2f}')


