test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> import hashlib
					>>> hashlib.sha256(bytes(str(round(prob_positive, 4)), "utf-8")).hexdigest()
					'eadbdb321ea15085a665751930eff3bb46ebb08be7da59633661b2f542073071'
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