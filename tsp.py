cost=[	[0,10,15,20],
		[5,0,9,10],
		[6,13,0,12],
		[8,8,9,0]
	]


def G(node ,subset):
	if len(subset)==0:
		return cost[node][0]
	min=10000
	temp_list=[]
	temp=0
	temp_list=subset.copy()
	print(subset)
	for v in subset:
		temp_list=subset.copy()
		temp_list.remove(v)
		temp=G(v,temp_list.copy())+cost[node][v]
		if(temp<min):
			min=temp
	return min

print(G(1,[0,2,3]))
