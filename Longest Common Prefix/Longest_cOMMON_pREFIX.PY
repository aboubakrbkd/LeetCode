# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Longest_cOMMON_pREFIX.PY                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/26 17:19:04 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/26 17:44:08 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs is None:
            return ""
        first = strs[0]
        for i in strs[1:]:
            while not i.startswith(first):
                first = first[:-1]
                if not first:
                    return ""
        return first
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
