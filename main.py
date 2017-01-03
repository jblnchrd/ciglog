#main program
 
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    A program to track your smoking
"""

import sys
import os.path
import filehandler
import helpers

def run():
    fname = filehandler.get_config_file()
    print("Current config file is {}".format(fname))
    args = sys.argv
    if(os.path.isfile(fname)):
        if(len(args) < 1):
            helpers.show_usage()
        elif (len(args) >= 2):
            helpers.menu(args[1], fname)
        else:
            helpers.show_usage()
        
if __name__ == "__main__":
    run()