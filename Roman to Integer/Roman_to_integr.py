# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Roman_to_integr.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/24 21:07:11 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/24 22:18:29 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

Roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
	"C" : 100,
	"D" : 500,
	"M" : 1000
}


class Solution(object):
    def romanToInt(self, s):
        x = 0
        for i in range(len(s)):
            if i + 1 < len(s)  and Roman[s[i]] < Roman[s[i + 1]]:
                x -= Roman[s[i]]
            else:
                x += Roman[s[i]]
        return x 
                
solution = Solution()
print(solution.romanToInt("II"))

