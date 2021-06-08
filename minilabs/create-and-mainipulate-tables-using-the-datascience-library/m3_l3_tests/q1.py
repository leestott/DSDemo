test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> np.random.seed(2020)
					>>> sum([dice() for _ in range(100000)])
					349547
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> np.random.seed(2020)
					>>> [dice() for _ in range(100000)][12945]
					5
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