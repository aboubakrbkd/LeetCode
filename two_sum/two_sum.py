# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    two_sum.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aboukdid <aboukdid@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/07/24 19:24:57 by aboukdid          #+#    #+#              #
#    Updated: 2024/07/24 20:22:35 by aboukdid         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution:
	def twoSum(self, nums: list[int], target: int)->list[int]:
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i, j]
