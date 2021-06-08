test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> 700 < covid_sample.pivot("COVID-19", "Test Results").rows[0][1] < 800
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> 100 < covid_sample.pivot("COVID-19", "Test Results").rows[1][2] < 200
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> covid_sample.num_rows
					1000
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