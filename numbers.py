def range( start, end=None, step=1, default=[] ):
	if end == None:
		start, end = 0, start
		
	if start > end:
		if step>0 or end>=start:
			return

	elif start < end:
		if step<0 or start>=end:
			return


	default.append(start)
	start+=step

	range( start, end, step, default )
	return default


print( range( 1,50,2 ) )