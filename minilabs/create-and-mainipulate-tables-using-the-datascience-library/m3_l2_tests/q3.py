test = {
	"name": "q3",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> rain_to_area.num_rows
					7
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> rain_to_area.num_columns
					13
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum([i[0] for i in rain_to_area.select("apr").rows]), 4)
					8.8911
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum([i[0] for i in rain_to_area.select("aug").rows]), 4)
					25.8271
					""",
					"hidden": False,
					"locked": False,
				}, 
				{
					"code": r"""
					>>> round(sum([i.item() for i in rain_to_area.sort("rain").rows[0]]), 4)
					110.2671
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