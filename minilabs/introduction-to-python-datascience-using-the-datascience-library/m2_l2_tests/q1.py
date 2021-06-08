test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> np.all(odd_numbers == np.arange(1, 10, 2))
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
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