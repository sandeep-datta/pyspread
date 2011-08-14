#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2008 Martin Manns
# Distributed under the terms of the GNU General Public License
# generated by wxGlade 0.6 on Mon Mar 17 23:22:49 2008

# --------------------------------------------------------------------
# pyspread is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyspread is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyspread.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------

"""
icons
=====

Provides:
---------
  1) ArtProvider: Provides stock and custom icons

"""

import types

import wx

from sysvars import get_program_path

class Icons(object):
    """Custom art provider class for providing additional icons"""
    
    theme = "Tango"
    
    icon_size = (24, 24)
    wide_icon = ""
    
    _action_path = get_program_path() + "share/icons/" + theme + "/" + \
                   str(icon_size[0]) + "x" + str(icon_size[1]) + \
                   "/actions/"
                   
    _action_path_small = get_program_path() + "share/icons/" + theme + "/" + \
                         str(icon_size[0]) + "x" + \
                         str(icon_size[1]) + "/actions/"
                   
    _toggle_path = get_program_path() + "share/icons/" + theme + "/" + \
                   str(icon_size[0]) + "x" + str(icon_size[1]) + \
                   "/toggles/"
    
    icons = {"PyspreadLogo": "pyspread.png", 
             "FileNew": _action_path + "filenew.png", 
             "FileOpen": _action_path + "fileopen.png", 
             "FileSave": _action_path + "filesave.png", 
             "FilePrint": _action_path + "fileprint.png", 
             "EditCut": _action_path + "edit-cut.png", 
             "EditCopy": _action_path + "edit-copy.png", 
             "EditCopyRes": _action_path + "edit-copy-results.png", 
             "EditPaste": _action_path + "edit-paste.png",
             "Undo": _action_path + "edit-undo.png",
             "Redo": _action_path + "edit-redo.png",
             "Find": _action_path + "edit-find.png",
             "FindReplace": _action_path + "edit-find-replace.png",
             "FormatTextBold": _action_path_small + "format-text-bold.png",
             "FormatTextItalic": _action_path_small + "format-text-italic.png",
             "FormatTextUnderline": _action_path_small + \
                                                "format-text-underline.png",
             "FormatTextStrikethrough": _action_path_small + \
                                                "format-text-strikethrough.png",
             "JustifyRight": _action_path_small + "format-justify-right.png",
             "JustifyCenter": _action_path_small + "format-justify-center.png",
             "JustifyLeft": _action_path_small + "format-justify-left.png",
             "AlignTop": _action_path_small + "format-text-aligntop.png",
             "AlignCenter": _action_path_small + "format-text-aligncenter.png", 
             "AlignBottom": _action_path_small + "format-text-alignbottom.png", 
             "Freeze": _action_path_small + "frozen_small.png",
             "AllBorders": _toggle_path + "border_all.xpm",
             "LeftBorders": _toggle_path + "border_left.xpm",
             "RightBorders": _toggle_path + "border_right.xpm",
             "TopBorders": _toggle_path + "border_top.xpm",
             "BottomBorders": _toggle_path + "border_bottom.xpm",
             "InsideBorders": _toggle_path + "border_inside.xpm",
             "OutsideBorders": _toggle_path + "border_outside.xpm",
             "TopBottomBorders": _toggle_path + "border_top_n_bottom.xpm",
             "SearchDirectionUp": _toggle_path + "go-down.png",
             "SearchDirectionDown": _toggle_path + "go-up.png",
             "SearchCaseSensitive": _toggle_path + "aA" + wide_icon + ".png",
             "SearchRegexp": _toggle_path + "regex" + wide_icon + ".png",
             "SearchWholeword": _toggle_path + "wholeword" + wide_icon + ".png",
             }
    

    def __getitem__(self, key):
        """Returns bmps by name"""
        
        icon_path = get_program_path() + 'share/icons/' + self.icons[key]
        
        return wx.Bitmap(icon_path, wx.BITMAP_TYPE_ANY)