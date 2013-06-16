import haxe.completion.hx.constants as hxcc

import sublime_plugin
import re 
from haxe.log import log

from haxe.tools import viewtools

from haxe.completion.hx.types import CompletionOptions
from haxe.completion.hx.base import trigger_completion

class HaxeAsyncTriggeredCompletionCommand( sublime_plugin.TextCommand ):
    def run( self , edit) :

        options = CompletionOptions(
            hxcc.COMPLETION_TRIGGER_ASYNC, 
            hxcc.COMPILER_CONTEXT_REGULAR, 
            hxcc.COMPLETION_TYPE_REGULAR)
        trigger_completion(self.view, options)


class HaxeDisplayCompletionCommand( sublime_plugin.TextCommand ):
    def run( self , edit, input_char = None) :
        log("RUN - HaxeDisplayCompletionCommand")
        if input_char != None:
            self.view.run_command("insert" , {
                "characters" : input_char
            })
        log("RUN - HaxeDisplayCompletionCommand")
        if is_valid_completion(self.view, edit, input_char):
            options = CompletionOptions(
                hxcc.COMPLETION_TRIGGER_MANUAL, 
                hxcc.COMPILER_CONTEXT_REGULAR, 
                hxcc.COMPLETION_TYPE_REGULAR)
            trigger_completion(self.view, options)


class HaxeDisplayMacroCompletionCommand( sublime_plugin.TextCommand ):
    def run( self , edit ) :
        log("RUN - HaxeDisplayMacroCompletionCommand")
        
        options = CompletionOptions(
            hxcc.COMPLETION_TRIGGER_MANUAL, 
            hxcc.COMPILER_CONTEXT_REGULAR, 
            hxcc.COMPLETION_TYPE_REGULAR)
        trigger_completion(self.view, options)
        
        

class HaxeHintDisplayCompletionCommand( sublime_plugin.TextCommand ):
    def run( self , edit ) :
        log("RUN - HaxeHintDisplayCompletionCommand")
        
        options = CompletionOptions(
            hxcc.COMPLETION_TRIGGER_MANUAL, 
            hxcc.COMPILER_CONTEXT_REGULAR, 
            hxcc.COMPLETION_TYPE_HINT)
        trigger_completion(self.view, options)

class HaxeMacroHintDisplayCompletionCommand( sublime_plugin.TextCommand ):
    def run( self , edit ) :
        log("RUN - HaxeMacroHintDisplayCompletionCommand")
        
        options = CompletionOptions(
            hxcc.COMPLETION_TRIGGER_MANUAL, 
            hxcc.COMPILER_CONTEXT_MACRO, 
            hxcc.COMPLETION_TYPE_HINT)

        trigger_completion(self.view, options)


def is_valid_completion (view, edit, input_char):
    valid = True
    if input_char == "(":
        src = viewtools.get_content_until_first_cursor(view)
        
        if is_open_parenthesis_after_function(src):
            log("Invalid Completion is open par after function")
            valid = False

    return valid


anon_func = re.compile("^function(\s+[a-zA-Z0-9$_]*\s+)?\s*\($")

def is_open_parenthesis_after_function (src):
    last_function = src.rfind("function")
    src_part = src[last_function:]
    match = re.match(anon_func, src_part)
    log(str(match))
    log(src_part)
    return match is not None

   