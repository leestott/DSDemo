test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> round(standard_units(sat.column("Math"))[12], 4)
					1.0082
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(standard_units(sat.column("Math"))[30], 4)
					-0.5822
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> correlation(sat.column("Math"), sat.column("Math"))
					1.0
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(correlation(sat.column("Math"), sat.column("Writing")), 4)
					0.9826
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