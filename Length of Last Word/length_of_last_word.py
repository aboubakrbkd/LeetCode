# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    length_of_last_word.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/26 14:16:12 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/26 14:39:27 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):
    def lengthOfLastWord(self, s):
        last_word = s.strip().split()
        if last_word == 0:
            return 0
        return len(last_word[-1])

solution = Solution()
print(solution.lengthOfLastWord("Hello Worldd"))