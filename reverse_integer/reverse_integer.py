# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reverse_integer.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/27 23:04:02 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/27 23:19:22 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):
    def reverse(self, x):
        reverse = 0
        is_negative = x < 0
        x = abs(x)
        while x != 0:
            modulo = x % 10
            reverse = reverse * 10 + modulo
            x = x //10
        if is_negative:
            reverse = -reverse
        if reverse > 2147483647 or reverse < -2147483648:
            return 0
        return reverse
		
solution = Solution()
print(solution.reverse(1534236469))