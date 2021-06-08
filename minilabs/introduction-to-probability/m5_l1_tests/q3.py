test = {
	"name": "q3",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> import hashlib
					>>> hashlib.sha256(bytes(str(round(prob_actual, 4)), "utf-8")).hexdigest()
					'5afdbea3b3375525050a04f0d1cd8ee34f3c2e80d9cdfb21852c303f39947dff'
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