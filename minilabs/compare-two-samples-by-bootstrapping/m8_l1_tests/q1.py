test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> sample_population(new_tests).num_rows
					348
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> sample_population(Table().with_columns("", np.arange(523))).num_rows
					523
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