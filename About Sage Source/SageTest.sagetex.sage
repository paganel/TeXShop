## -*- encoding: utf-8 -*-
## This file (SageTest.sagetex.sage) was *autogenerated* from SageTest.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('SageTest', version='2015/08/26 v3.0-92d9f7a', version_check=True)
try:
 _st_.current_tex_line = 23
 _st_.inline(0, latex(32^31))
except:
 _st_.goboom(23)
try:
 _st_.current_tex_line = 25
 _st_.inline(1, latex(1324^9))
except:
 _st_.goboom(25)
try:
 _st_.current_tex_line = 29
 _st_.plot(0, format='notprovided', _p_=plot(x * sin( 30 * x), -1, 1))
except:
 _st_.goboom(29)
try:
 _st_.current_tex_line = 33
 _st_.inline(2, latex(integrate( (x^2 + x + 1) / ((x - 1)^3 * (x^2 + x + 2)), x )))
except:
 _st_.goboom(33)
try:
 _st_.current_tex_line = 38
 _st_.inline(3, latex(matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])^3))
except:
 _st_.goboom(38)
try:
 _st_.current_tex_line = 40
 _st_.inline(4, latex(Matrix([[1, 2], [3, 4]])))
except:
 _st_.goboom(40)
try:
 _st_.current_tex_line = 40
 _st_.inline(5, latex(Matrix([[5, 6], [6, 8]])))
except:
 _st_.goboom(40)
try:
 _st_.current_tex_line = 40
 _st_.inline(6, latex(Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [6, 8]])))
except:
 _st_.goboom(40)
try:
 _st_.current_tex_line = 44
 _st_.plot(1, format='notprovided', _p_=plot(x * ln(x), 0, 2))
except:
 _st_.goboom(44)
try:
 _st_.current_tex_line = 48
 _st_.inline(7, latex(pi * e))
except:
 _st_.goboom(48)
try:
 _st_.current_tex_line = 48
 _st_.inline(8, latex(N(pi * e)))
except:
 _st_.goboom(48)
_st_.endofdoc()
