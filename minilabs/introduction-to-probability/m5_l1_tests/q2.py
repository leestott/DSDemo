test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> import hashlib
					>>> hashlib.sha256(bytes(str(round(prob_negative, 4)), "utf-8")).hexdigest()
					'22fa3ce4995af8d96fcd771f0e1f5d74d8a98f36c3eec8e95bdf7524926b0141'
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