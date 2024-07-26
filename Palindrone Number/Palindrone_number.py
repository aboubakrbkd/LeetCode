# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Palindrone_number.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/24 20:41:09 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/24 21:05:07 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):
    def isPalindrome(self, x):
        original_num = x
        reversed_number = 0
        if x < 0:
            return False
        while original_num != 0:
            modulo = original_num % 10
            reversed_number = reversed_number * 10 +  modulo
            original_num = original_num // 10
        if x == reversed_number:
            return True
        return False
            
solution=Solution()
print(solution.isPalindrome(121))
        