al = {
	"a":"1",
	"b":"2",
	"c":"3",
	"d":"4",
	"e":"5",
	"f":"6",
	"g":"7",
	"h":"8",
	"i":"9",
	"j":"10",
	"k":"11",
	"l":"12",
	"m":"13",
	"n":"14",
	"o":"15",
	"p":"16",
	"q":"17",
	"r":"18",
	"s":"19",
	"t":"20",
	"u":"21",
	"v":"22",
	"w":"23",
	"x":"24",
	"y":"25",
	"z":"26"
}
# 12 = ab, l beacause 12 is format from a,b and l
def num_ways(data):
	arr = list(data)
	obj = {}
	for x in al:
		if arr[0] == al[x]:
			obj['comb'] = x
		if arr[1] == al[x]:
			obj['comb'] += x
		if(data == al[x]):
			obj['single'] = x

	print(obj)

num_ways('14')

