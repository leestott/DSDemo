test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> all_fruits.num_rows
					3
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> all_fruits.num_columns
					9
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> [i[0] for i in all_fruits.sort("Names").select("Dragonfruits").rows]
					[9, 7, 3]
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> [i[0] for i in all_fruits.sort("Names").select("Apples").rows]
					[3, 2, 5]
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> [i[0] for i in all_fruits.sort("Names").select("Least Favorite Fruit").rows]
					['Kiwi', 'Kiwi', 'Orange']
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