test = {
	"name": "q3",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> dragonfruit_price(1)
					1.53
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> dragonfruit_price(100)
					153.0
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> dragonfruit_price(12.6)
					19.278
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