set mouse=a
set number
set modeline
set ls=2
set hlsearch
map <C-n> :set number! <CR>
map <C-r> :set syntax=ttcn <CR>
map <C-e> :set syntax=off <CR>
map <C-d> :%g/\.svn/d <CR> :%g/\.xml/d <CR> :%g/^Binary/d <CR>
map <C-left> :tabp <CR>
map <C-right> :tabn <CR>
