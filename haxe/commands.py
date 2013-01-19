import haxe.haxe_complete




import sublime, sublime_plugin
import time


from haxe.log import log

import haxe.lib as hxlib


from sublime import Region

import os



import haxe.project as hxproject


import haxe.codegen

from haxe.tools import PathTools

#class HaxelibExecCommand(stexec.ExecCommand):
#
#	def run(self, *args, **kwargs):
#
#		print "hello running"
#		super(HaxelibExecCommand, self).run(*args, **kwargs)
#
#	def finish(self, *args, **kwargs):
#		super(HaxelibExecCommand, self).finish(*args, **kwargs)  
#		print "haxelibExec"
#		hxlib.HaxeLib.scan()

class HaxeGetTypeOfExprCommand (sublime_plugin.TextCommand ):
	def run( self , edit ) :
		

		view = self.view
		
		fileName = view.file_name()

		if fileName == None:
			return

		fileName = os.path.basename(view.file_name())

		window = view.window()
		folders = window.folders()
 
		projectDir = folders[0]
		tmpFolder = folders[0] + "/tmp"
		targetFile = folders[0] + "/tmp/" + fileName

		if os.path.exists(tmpFolder):
			PathTools.removeDir(tmpFolder)			
		

		os.makedirs(tmpFolder)
		

		fd = open(targetFile, "w+")
		sel = view.sel()

		word = view.substr(sel[0])

		replacement = "(hxsublime.Utils.getTypeOfExpr(" + word + "))."

		newSel = Region(sel[0].a, sel[0].a + len(replacement))


		view.replace(edit, sel[0], replacement)

		newSel = view.sel()[0]

		view.replace(edit, newSel, word)

		newContent = view.substr(sublime.Region(0, view.size()))
		fd.write(newContent)

		view.run_command("undo")


class HaxeDisplayCompletion( sublime_plugin.TextCommand ):

	def run( self , edit ) :

		log("run HaxeDisplayCompletion")
		
		view = self.view
		project = hxproject.currentProject(self.view)
		project.completion_context.set_manual_trigger(view, False)
		

		self.view.run_command( "auto_complete" , {
			"api_completions_only" : True,
			"disable_auto_insert" : True,
			"next_completion_if_showing" : False,
			'auto_complete_commit_on_tab': True
		})


class HaxeDisplayMacroCompletion( sublime_plugin.TextCommand ):
	
	def run( self , edit ) :
		
		log("run HaxeDisplayMacroCompletion")
		
		view = self.view
		project = hxproject.currentProject(view)
		project.completion_context.set_manual_trigger(view, True)
		
		
		view.run_command( "auto_complete" , {
			"api_completions_only" : True,
			"disable_auto_insert" : True,
			"next_completion_if_showing" : True
		} )

		

class HaxeInsertCompletionCommand( sublime_plugin.TextCommand ):
	
	def run( self , edit ) :
		log("run HaxeInsertCompletion")
		view = self.view

		view.run_command( "insert_best_completion" , {
			"default" : ".",
			"exact" : True
		} )

class HaxeSaveAllAndBuildCommand( sublime_plugin.TextCommand ):
	def run( self , edit ) :
		log("run HaxeSaveAllAndBuildCommand")
		view = self.view
		view.window().run_command("save_all")
		hxproject.currentProject(self.view).run_build( view )

class HaxeRunBuildCommand( sublime_plugin.TextCommand ):
	def run( self , edit ) :
		view = self.view
		log("run HaxeRunBuildCommand")
		hxproject.currentProject(self.view).run_build( view )


class HaxeSelectBuildCommand( sublime_plugin.TextCommand ):
	def run( self , edit ) :
		log("run HaxeSelectBuildCommand")
		view = self.view
		
		hxproject.currentProject(self.view).select_build( view )

# called 
class HaxeHintCommand( sublime_plugin.TextCommand ):
	def run( self , edit ) :
		log("run HaxeHintCommand")
		
		view = self.view
		
		view.run_command('auto_complete', {'disable_auto_insert': True})
		


class HaxeRestartServerCommand( sublime_plugin.WindowCommand ):

	def run( self ) :
		log("run HaxeRestartServerCommand")
		view = sublime.active_window().active_view()
		
		project = hxproject.currentProject(self.view)

		project.server.stop_server()
		project.server.start_server( view )



class HaxeGenerateUsingCommand( sublime_plugin.TextCommand ):
	def run( self , edit ) :
		log("run HaxeGenerateUsingCommand")
		haxe.codegen.generate_using(self.view, edit)
		

class HaxeGenerateImportCommand( sublime_plugin.TextCommand ):

	def run( self, edit ) :
		log("run HaxeGenerateImportCommand")
		
		haxe.codegen.generate_import(self.view, edit)
		