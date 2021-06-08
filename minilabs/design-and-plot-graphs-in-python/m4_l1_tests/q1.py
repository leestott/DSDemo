test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> average_fires.num_columns
					5
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> average_fires.num_rows
					12
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum([i for i in average_fires.rows[4]]), 3)
					43.34
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum([i for i in average_fires.rows[6]]), 3)
					47.22
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum(average_fires.column("temp average")), 4)
					171.9256
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum(average_fires.column("area average")), 4)
					109.3733
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