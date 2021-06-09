# Steam Screenshots Sorter

Automatically sorts all your Steam screenshots into folders based on the name of the game. It runs as a background process and listens for new files, so if you place it in the same folder that Steam saves your screenshots, it will automatically sort it for you. This makes it slightly easier to find that one great screenshot you did a long time ago that you dread looking for because it's burried too deep.

## Support

Please, if you got any use out of my work, donate so I'm able to continue coding like this. I'm in a limbo of not enough work experience and no relevant formal education, so getting work is difficult for me, and I have to pay back my student depts. If you've got disposable income, I ask that you donate a little.

## Install

Fetch Python 3.9.5 or newer from [the official site](https://www.python.org/downloads/release)

Download the zip file in the [releases](#) tab and extract the contents of it in the folder of your unsorted screenshots (still beta, I recommend keeping a backup. It probably won't mess anything up, but it _could_)

### Setup dependencies

Open the directory you unzipped to in a terminal and input `pip install pipenv` (You may need to run an elevated shell. Sudo on Linux, open as admin on Windows). Once that's done, run `pipenv install`

### Run script

Everything should be setup and ready to go now. Just open the folder you placed the script in, in a terminal and run `pipenv run python -m _main`. It doesn't matter if there's already images in the folder or if you drop new ones into it. If you want the script to stop running, click `ctrl + c`.
