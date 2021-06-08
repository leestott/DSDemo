test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> 7500 < covid_population.group("COVID-19").sort("COVID-19").rows[0][1] < 8500
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> 1500 < covid_population.group("COVID-19").sort("COVID-19").rows[1][1] < 2500
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> covid_population.num_rows
					10000
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