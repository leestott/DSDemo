test = {
	"name": "q3",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> str(type(num_below))
					"<class 'float'>"
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> simulation_table.num_rows == iterations
					True
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