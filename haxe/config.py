class Config :

	targetPackages = ["flash","flash9","flash8","neko","js","php","cpp","cs","java","nme","jeash","neash"]

	targets = ["js","cpp","swf","swf9","neko","php","java","cs"]
	
	nme_targets = [("Flash","flash","test"),("HTML5","html5","test"),("C++","cpp","test"),("Linux 64","linux -64","test"),("iOS - iPhone Simulator","ios -simulator","test"),("iOS - iPad Simulator","ios -simulator -ipad","test"),("iOS - Update XCode Project","ios","update"),( "Android","android","test"),("WebOS", "webos","test"),("Neko","neko","test"),("BlackBerry","blackberry","test")]
	
	nme_target = ("Flash","flash","test")

	SOURCE_HAXE = 'source.haxe.2'
	SOURCE_HXML = 'source.hxml'
	SOURCE_NMML = 'source.nmml'
	SOURCE_ERAZOR = 'source.erazor'
	HXSL_SUFFIX = '.hxsl'