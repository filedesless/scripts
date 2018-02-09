# get git branch on prompt
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# colors :)
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$(parse_git_branch)\[\033[00m\] \$(date +%H:%M) \$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'

# brew thing
export PATH=/usr/local/bin:/usr/local/sbin:$PATH

# personal scripts
export PATH=~/bin:$PATH

# aspnet things
export ASPNETCORE_ENVIRONMENT=Development

# opam stuff
eval `opam config env`

alias markright="open -a /Applications/MarkRight.app"
alias python='python3'

export PATH="$HOME/.cargo/bin:$PATH"
