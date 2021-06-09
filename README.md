# Steam Screenshots Sorter

Automatically sorts all your Steam screenshots into folders based on the name of the game. It runs as a background process and listens for new files, so if you place it in the same folder that Steam saves your screenshots, it will automatically sort it for you. This makes it slightly easier to find that one great screenshot you did a long time ago that you dread looking for because it's burried too deep.

## Install

In the future I want to simplify this, but for now, you'll have to do some additional steps.

Fetch Python 3.9.5 or newer from [the official site](https://www.python.org/downloads/release)

Download the zip file in the [releases](#) tab and extract the contents of it in the folder of your unsorted screenshots (still beta, I recommend keeping a backup. It probably won't mess anything up, but it _could_)

### Setup dependencies

Open the directory you unzipped to in a terminal and input `pip install pipenv` (You may need to run an elevated shell. Sudo on Linux, open as admin on Windows). Once that's done, run `pipenv install`

### Run script

Everything should be setup and ready to go now. Just open the folder you placed the script in, in a terminal and run `pipenv run python -m _main`. It doesn't matter if there's already images in the folder or if you drop new ones into it. If you want the script to stop running, click `ctrl + c`.

## Sponsor Me

Please, if you got any use out of my work, donate so I'm able to continue coding like this. Sponsor me [directly](https://github.com/sponsors/Reinachan) on GitHub or give me some crypto so that I can continue doing what I love :)

**BTC**: 3CYuRVKrwbrpNavSuKFPrnSUsVYkahwAzs<br>
**MATIC**: 0x3965F4F9d3233b0470b82863Fb102Cc5e22347b3<br>
**OMG**: 0xea90e92aFd82177Edbf4F49A86a132A9Fb63E216<br>
**USDC**: 0xfa40F956a28e66B8ee0d88E6ceBD1fba02BB30B5<br>
**DOGE**: DHZtSJjFpmYVZSDQeuMWTFfxdZ61huTtJr<br>

## Credit Me

If you use any of my code, remember to credit me properly according to the license. If you make money off of my code, please kindly refer to the section above and donate some of it my way, thank you :)
