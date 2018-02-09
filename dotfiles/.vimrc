syntax on
set number
set relativenumber
set tabstop=2
set shiftwidth=2
set noexpandtab
execute pathogen#infect()
call pathogen#helptags()

" Start NERDTree, but focus on file
autocmd VimEnter * NERDTree
autocmd VimEnter * wincmd p

" Close vim when there's only a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Autoindent
 filetype plugin indent on 

au VimEnter,BufWinEnter * syn match ErrorMsg " "

" Uh... dafuck backspace?
set backspace=indent,eol,start

" I use a mouse; fight me
set mouse=a
