#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# example of xdot with multiline support
# author: F. Manuel Hevia (fructu@gmail.com)
# part of abidos https://github.com/fructu/abidos
#
# original code_
#  http://code.google.com/p/jrfonseca/wiki/XDot
#  Copyright 2008 Jose Fonseca
#
# in this example you can navigate the source file main.cpp
# for that you must uncoment the line of the gedit or the kate
# or put other for your favorite editor.
#

import os
import gtk
import gtk.gdk

import xdot

class MyDotWindow(xdot.DotWindow):

    def __init__(self):
        #activate/desactivate the feature here:
        xdot.options.set_multi_line_activate(1)
        #separator is ';' bye default
        xdot.options.set_multi_line_separator(';')
        xdot.DotWindow.__init__(self)
        self.widget.connect('clicked', self.on_url_clicked)

    def on_url_clicked(self, widget, url, event):
        if url is not None:
          if 1 == xdot.options.get_multi_line_activate():
            call_parts = url.split(":")
            file_parts = call_parts[0].split("[")
            line_parts = call_parts[1].split("]")

            command = "echo url '"+ file_parts[1]+" +"+ line_parts[0]+ "'"
#gedit
#            command = "gedit "+ file_parts[1]+" +"+ line_parts[0]
#kate
#            command = "kate " + file_parts[1]+" -l"+ line_parts[0]
          else:
            command = "echo 'url "+ url + "'"
            
        to_run="%s" % command
        error = os.system(to_run)            

        return True

def main():
    window = MyDotWindow()
    window.set_filter("dot")
    window.open_file("example_02.dot");
    window.connect('destroy', gtk.main_quit)
    gtk.main()

if __name__ == '__main__':
    main()


