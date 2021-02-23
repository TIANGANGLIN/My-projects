from itertools import permutations, product
class Solution():
    def __init__(self,a,t):
        self.a=a 
        self.t=t
        self.data_permutations = []
        self.operation_permutations = []

    def f(self):
        a=self.a 
        t=self.t
        operations = ['+','-','*','/']
        equations_list=[]
        data_list = self.Permutation(a,len(a),repeat_data=None)

        operations_list =self.Permutation(operations,len(a)-1,repeat_data=True)
        for i in data_list:
            for j in operations_list:
                cur_result = i[0]
                equation = str(i[0])
                for n_of_opers,op in enumerate(j):
                    if op =='+':
                        cur_result +=i[n_of_opers+1]
                    if op =='-':
                        cur_result -=i[n_of_opers+1]
                    if op == '*':
                        cur_result *=i[n_of_opers+1]
                    if op =='/':
                        cur_result /=i[n_of_opers+1]
                    if i[n_of_opers+1]<0:
                        equation = equation+op+'('+str(i[n_of_opers+1])+')'*2
                    else:
                        equation = equation+op+str(i[n_of_opers+1])+')'
                equation = '('*len(j)+equation+ '='+str(t)
                if cur_result == t:
                    equations_list.append(equation)
        return equations_list

    def Permutation(self, data,lenth,repeat_data=True):
        # write code here
        data_lis, res = list(data), []
        cur_res=[]
        def dfs(x,cur_res):
            if x == lenth:
                res.append(tuple(cur_res))
                # res.append(''.join(cur_res))
                return
            for i in data_lis:
                if repeat_data:
                    cur_res.append(i)
                    dfs(x+1,cur_res)
                    cur_res.pop()
                else:
                    if i not in cur_res:
                        cur_res.append(i)
                        dfs(x+1,cur_res)
                        cur_res.pop()
        dfs(0,cur_res)
        return res



if __name__ == '__main__':
    a,t =[2,3,5,-9,10],10
    print(Solution(a,t).f()) 
