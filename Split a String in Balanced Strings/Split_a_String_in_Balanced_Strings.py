# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Split_a_String_in_Balanced_Strings.py              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/26 14:53:07 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/26 15:08:23 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):
    def balancedStringSplit(self, s):
        R_count = 0
        L_count = 0
        s_return = 0
        for i in range(len(s)):
            if s[i] == 'R':
                R_count += 1
            elif s[i] == 'L':
                L_count += 1
            if (R_count == L_count):
                s_return += 1
        return s_return
        
        
solution = Solution()
print(solution.balancedStringSplit("RLRRRLLRLL"))