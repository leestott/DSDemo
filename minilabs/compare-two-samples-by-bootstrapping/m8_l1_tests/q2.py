test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> # This test case may fail due to random chance!
					>>> # If you believe this to be the case rerun the cell
					>>> 2.5 < bootstrap(Table().with_columns("", np.arange(2, 5, 0.3)), "", np.average) < 4
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