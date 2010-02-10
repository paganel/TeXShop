"""
%%
%% This is file `sagetex.py',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% sagetexpackage.dtx  (with options: `python')
%% 
%% This is a generated file.
%% 
%% Copyright (C) 2008 by Dan Drake <ddrake@member.ams.org>
%% 
%% This program is free software: you can redistribute it and/or modify it
%% under the terms of the GNU General Public License as published by the
%% Free Software Foundation, either version 2 of the License, or (at your
%% option) any later version.
%% 
%% This program is distributed in the hope that it will be useful, but
%% WITHOUT ANY WARRANTY; without even the implied warranty of
%% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
%% General Public License for more details.
%% 
%% You should have received a copy of the GNU General Public License along
%% with this program.  If not, see <http://www.gnu.org/licenses/>
%% 
"""
import sys
if __name__ == "__main__":
  print("""This file is part of the SageTeX package.
It is not meant to be called directly.

This file will be used by Sage scripts generated from a LaTeX document
using the sagetex package. Keep it somewhere where Sage and Python can
find it and it will automatically be imported.""")
  sys.exit()
from sage.misc.latex import latex
import os
import os.path
import hashlib
import traceback
import subprocess
import shutil
initplot_done = False
dirname       = None
filename      = ""
def progress(t,linebreak=True):
  if linebreak:
    print(t)
  else:
    sys.stdout.write(t)
def openout(f):
  global filename
  filename = f
  global _file_
  _file_ = open(f + '.sout.tmp', 'w')
  s = '% This file was *autogenerated* from the file ' + \
        os.path.splitext(filename)[0] + '.sage.\n'
  _file_.write(s)
  progress('Processing Sage code for %s.tex...' % filename)
def initplot(f):
  global initplot_done
  if not initplot_done:
    progress('Initializing plots directory')
    global dirname
    dirname = 'sage-plots-for-' + f + '.tex'
    if os.path.isdir(dirname):
      shutil.rmtree(dirname)
    os.mkdir(dirname)
    initplot_done = True
def inline(counter, s):
  progress('Inline formula %s' % counter)
  _file_.write('\\newlabel{@sagelabel' + str(counter) + '}{{' + \
               latex(s) + '}{}{}{}{}}\n')
def blockbegin():
  progress('Code block begin...', False)
def blockend():
  progress('end')
def plot(counter, p, format='notprovided', epsmagick=False, **kwargs):
  global dirname
  progress('Plot %s' % counter)
  if format == 'notprovided':
    formats = ['eps', 'pdf']
  else:
    formats = [format]
  for fmt in formats:
    plotfilename = os.path.join(dirname, 'plot-%s.%s' % (counter, fmt))
    #print('  plotting %s with args %s' % (plotfilename, kwargs))
    p.save(filename=plotfilename, **kwargs)
    if format != 'notprovided' and epsmagick is True:
      print('Calling Imagemagick to convert plot-%s.%s to EPS' % \
        (counter, format))
      toeps(counter, format)
def toeps(counter, ext):
  global dirname
  subprocess.check_call(['convert',\
    '%s/plot-%s.%s' % (dirname, counter, ext), \
    '%s/plot-%s.eps' % (dirname, counter)])
def goboom(line):
  global filename
  print('\n**** Error in Sage code on line %s of %s.tex! Traceback\
 follows.' % (line, filename))
  traceback.print_exc()
  print('\n**** Running Sage on %s.sage failed! Fix %s.tex and try\
 again.' % (filename, filename))
  os.remove(filename + '.sout.tmp')
  sys.exit(1)
def endofdoc():
  global filename
  sagef = open(filename + '.sage', 'r')
  m = hashlib.md5()
  for line in sagef:
    if line[0:15] != ' sagetex.goboom':
      m.update(line)
  s = '%' + m.hexdigest() + '% md5sum of .sage file (minus "goboom" \
lines) that produced this\n'
  _file_.write(s)
  _file_.close()
  os.rename(filename + '.sout.tmp', filename + '.sout')
  progress('Sage processing complete. Run LaTeX on %s.tex again.' %\
           filename)
"""
\endinput
%%
%% End of file `sagetex.py'.
"""