test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> many_dragonfruits.num_rows
					2
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> many_dragonfruits.rows[0][0]
					'Ahmed'
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> many_dragonfruits.rows[1][2]
					3
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