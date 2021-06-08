test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> monthly_statistics.num_rows
					12
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> monthly_statistics.num_columns
					5
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum([i[0] for i in monthly_statistics.select("area average").rows]), 4)
					109.3733
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum([i[0] for i in monthly_statistics.select("temp average").rows]), 4)
					171.9256
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(np.prod([i.item() for i in monthly_statistics.sort("month").rows[5][1:]]), 4)
					7.4152
					""",
					"hidden": False,
					"locked": False,
				}, 
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}, 
	]
}