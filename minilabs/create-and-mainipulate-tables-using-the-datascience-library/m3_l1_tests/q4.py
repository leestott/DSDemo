test = {
	"name": "q4",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> prices.num_rows
					2
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> prices.rows[0][0]
					'Ahmed'
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> prices.rows[1][2]
					3
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> prices.num_columns
					5
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> prices.rows[1][4]
					10.71
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