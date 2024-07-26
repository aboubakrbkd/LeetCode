 # **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Sort_an_array.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/25 16:26:03 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/25 17:04:20 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution(object):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        middle  = len(arr) // 2
        left = arr[middle:]
        right = arr[:middle]
        sleft = merge_sort(left)
        sright = merge_sort(right)
        return merge(sleft, sright)
    
    def sortArray(self, nums):
        
