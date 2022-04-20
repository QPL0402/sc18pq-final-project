import Create
import Topk

## Create new the least time routing table
def lastpath():
    Create.lista()
    global lpath
    lpath = []
    num = 0
    for i in range(len(Create.listpath)):
        t = []
        for ii in range(len(Create.listpath)):
            ##add same route time into list and select the one with the shorter time
            if(Create.listpath[i][0][0] == Create.listpath[ii][0][0] and Create.listpath[i][-1][0] == Create.listpath[ii][-1][0]):
                t.append(Create.listpath[ii][-1][1]-Create.listpath[ii][0][1])
                ##print(t)
        h = Topk.select(t, 0)
        ##print(h)
        for iii in range(len(Create.listpath)):
            ## Find the original paths in the shortest time 最短时间
            if(Create.listpath[i][0][0] == Create.listpath[iii][0][0] and Create.listpath[i][-1][0] == Create.listpath[iii][-1][0]):
                if(Create.listpath[iii][-1][1]-Create.listpath[iii][0][1]== h):
                    lpath.append(Create.listpath[iii])
                    lpath.sort()
                    tt = lpath[-1]
                    ## Delete the duplicate paths
                    for m in range(len(lpath) - 2, -1, -1):
                        # print(i)
                        if tt == lpath[m]:
                            # del lists[i]
                            lpath.remove(lpath[m])
                        else:
                            tt = lpath[m]


# if __name__ == '__main__':
#     lastpath()
#     print(lpath)
#     print(len(lpath))











