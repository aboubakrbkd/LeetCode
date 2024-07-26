# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rev_print.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/26 19:09:34 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/26 19:18:05 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):
    def rev_print(self, s):
        l = len(s) - 1
        result = ""
        i = 0
        while l >= 0:
            result = result + s[l]
            l = l -1
        return result
solution = Solution()
print(solution.rev_print("hello"))