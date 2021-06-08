test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> round(slope(sat.column("Math"), sat.column("Writing")), 4)
					0.9343
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(intercept(sat.column("Math"), sat.column("Writing")), 4)
					15.3979
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