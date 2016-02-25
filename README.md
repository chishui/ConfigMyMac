# ConfigMyMac

####1. Install HomeBrew  
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"   
[website](http://brew.sh/)
####2. Install zsh  
brew install zsh
####3. Install Oh-my-zsh  
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"  
change path to absolute path: edit oh-my-zsh theme, change %c to %d  
install autojump:
brew install autojump
edit .zshrc, add autojump to plugin
[website](http://ohmyz.sh/)
####4. Config terminal
####5. Install Vim
. Copy .vimrc from my github
. Install Vundle:git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
. vim and run :PluginInstall 
####6. Install Vundle
####7. Plugins
#####1. clang-format: 
install: brew install clang-format  
vim support: https://llvm.org/svn/llvm-project/cfe/trunk/tools/clang-format/clang-format.py
