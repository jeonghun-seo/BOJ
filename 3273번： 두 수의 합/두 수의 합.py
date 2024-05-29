#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3273                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: nne7741 <boj.kr/u/nne7741>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3273                           #+#        #+#      #+#     #
#    Solved: 2024/05/29 13:26:49 by nne7741       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def comp_num(num1, num2,x):
    tmp = num1+num2
    if tmp == x:
        return True
    else:
        return False

def find_hap(num_list, x,a):
    count = 0
    a2 = list(map(int, num_list))
    a2.sort()
    for i in range(a-1):
        now_num = a2[i]
        next_list = a2[i+1:]
        for n in next_list:
            if comp_num(now_num,n,x):
                count += 1
    return count

a = int(input())
b = input()
c = int(input())
b_list  = b.split(" ")

print(find_hap(b_list, c,a))
