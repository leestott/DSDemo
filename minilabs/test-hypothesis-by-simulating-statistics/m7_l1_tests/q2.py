test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> sample_population(test_results).num_rows
					3000
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> "Test Result" in sample_population(test_results).labels
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(apply_statistic(test_results, "Village Number", np.average), 4)
					8.1307
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