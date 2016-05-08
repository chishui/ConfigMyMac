import os
import shutil

def install():
    os.system('apt-get install git vim tmux zsh autojump')

def install_plugin():
    os.system('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
    os.system('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim')

def download_myconfig():
    os.system('git clone https://github.com/chishui/dotfile.git')
    shutil.copyfile('./dotfile/.vimrc', '~/.vimrc')
    shutil.copyfile('./dotfile/.zshrc', '~/.zshrc')
    shutil.copyfile('./dotfile/.tmux.conf', '~/.tmux.conf')

if __name__== '__main__':
    install()
    install_plugin()
    download_myconfig()

