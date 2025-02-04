# """
# for node i:
#     children: 2i+1 and  2i+2
#     parent: (i−1)/2
# """
class MinHeap:
    def __init__(self):
        self.size=0
        self.arr=[] # level by level, left to right

    def sift_up(self):
        i = self.size-1
        while (i-1)//2 >= 0 and self.arr[(i-1)//2] > self.arr[i]:
            self.arr[(i-1)//2],self.arr[i] = self.arr[i],self.arr[(i-1)//2]
            i=(i-1)//2
        
    def insert(self,val):
        self.arr.append(val)
        self.size+=1
        self.sift_up()

    def sift_down(self):
        i = 0
        while 2*i+1<self.size:
            # GET MIN CHILD IDX
            if 2*i+2>=self.size: # if right out of bounds, Minchild is leftchild
                mc_idx = 2*i+1
            else:
                if self.arr[2*i+1] < self.arr[2*i+2]:
                    mc_idx = 2*i+1
                else:
                    mc_idx = 2*i+2

            if self.arr[i] > self.arr[mc_idx]:
                self.arr[i],self.arr[mc_idx]=self.arr[mc_idx],self.arr[i]
                i=mc_idx
            else:
                break
                
    def pop_min(self):
        data = self.arr[0]
        self.arr[0]=self.arr[self.size-1] 
        self.arr.pop()
        self.size-=1
        self.sift_down()
        return data


if __name__ == '__main__':
    mh = MinHeap()
    mh.insert(1)
    mh.insert(3)
    mh.insert(5)
    mh.insert(7)
    mh.insert(2)
    mh.insert(4)
    mh.insert(92)
    mh.insert(11)
    mh.insert(223)
    mh.insert(400)


    # a = mh.pop_min()

    res=[]
    # print("start",mh.arr)
    while mh.arr:
        a = mh.pop_min()
        res.append(a)
        # print(mh.arr)
    print(res)

    # print(mh.arr)

    #             #       1
    #             #     3   5
    #             #   7   2

    #             #        1
    #             #     2     5
    #             #    7 3   4

    #             #        1
    #             #     2     4
    #             #    7 3   5
    # POP
    #             #        5
    #             #     2     4
    #             #    7 3   1

    #             #        5
    #             #     2     4
    #             #    7 3   

    #             #        2
    #             #     5     4
    #             #    7 3   

    #             #        2
    #             #     3     4
    #             #    7 5   
    # POP
    #             #        5
    #             #     3     4
    #             #    7    
    #             #        3
    #             #     5     4
    #             #    7 
    # POP   
    #             #        7
    #             #     5     4
    #             #        4
    #             #     5     7
    # POP
    #             #        7
    #             #     5     
    #             #        5
    #             #     7     
    