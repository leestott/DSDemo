test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> fruits.rows[0][0]
					'Tien'
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> dragonfruits.rows[0][0]
					'Ahmed'
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> dragonfruits.rows[2][0]
					'Tien'
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