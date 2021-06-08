test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> sum(dice_rolls)
					35165.0
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> np.prod(dice_rolls[3324:3343])
					1592524800.0
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> dice_rolls[7743]
					3.0
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