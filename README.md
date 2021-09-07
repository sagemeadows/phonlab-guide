# A Guide to Phonetic Analysis Software
*Last updated: 7 Sept 2021*

This guide explains how to use a number of softwares for phonetic analysis and provides step-by-step instructions on how to get vowel data out of audio files.

This document may look long and complicated, but don’t worry! A lot of it is installation stuff that you’ll only have to do once, and there are also a lot of images adding to the length.

## Table of Contents

1. [**The Command Line**](#the-command-line)
    - Start here if you don't know what a command line is or how it works.
2. [**Praat**](#praat)
    - How to download Praat and annotate sound files. Skim this part if you’ve already downloaded Praat. Skip it entirely if you’re already confident with using Praat’s annotation functions.
3. [**Montreal Forced Aligner**](#montreal-forced-aligner)
    - What a forced aligner does and how to install and use MFA. You need to know how to use a command line to do this!
4. [**FastTrack**](#fasttrack)
    - What FastTrack does, how to install it, and how to use it to extract vowel data.
5. [**Organizing the Data**](#organizing-the-data)
    - How to convert the FastTrack output into something more usable.
6. [**Plotting the Data**](#plotting-the-data)
    - Using R to plot voices and vowels.

## The Command Line
### What is a command line, and why is it useful?
A command line or command line interface (CLI) is a text-based system for accessing the files on your computer more directly than through a click-and-drag file manager application.

To use the command line, you type in commands (hence the name “command line”) that tell the computer what to do.

**Here’s a good beginner’s guide to command lines: [Getting to Know the Command Line by David Baumgold](https://www.davidbaumgold.com/tutorials/command-line/).**

### What does this have to do with software?
All the software that you use comes from files that are stored somewhere on your computer.

Some softwares, e.g. browsers like Chrome, Firefox, etc., have their own interface that you can open and interact with, and are usually easily accessible from the desktop.

But other softwares may not have their own interface, so you have to use the command line to actually use the software.

When this is the case, the software will come with its own set of commands that you can use in the command line to run the software.

The [Montreal Forced Aligner](#montreal-forced-aligner) (MFA) discussed later on in this guide is an example of a software without an interface of its own.

### Where do I find my command line?
Where your command line is [depends on what kind of computer or operating system you have](https://www.davidbaumgold.com/tutorials/command-line/#finding-the-command-line).

#### Mac
If you’re on a Mac, you already have a command line. To find it, go to your Applications folder, then click on Utilities. There, click on the application called Terminal.

#### Linux
If you’re using a Linux operating system, you also already have a command line, but where you can find it depends on what kind of window manager you’re using.

If you’re using KDE, your command line is called Konsole and you find it by clicking on the K button, selecting System, and clicking on Konsole.

If you’re using Gnome or Xcfe, your command line is called Terminal and you find it by clicking on the Applications button on the top left, selecting System Tools, and clicking on Terminal.

#### Windows
If you’re using Windows, you have to install a command line emulator. This is because the command line that comes with Windows is non-standard and hard to use. The command line emulator is a software that lets you use the command line with an easier user interface.

**Here’s a list of free command line emulators you can use on Windows: [15+ Best Free Terminal Emulators for Windows In 2021](https://www.puttygen.com/windows-terminal-emulators)**

### Using the command line
When you open the command line, you should get a window that looks something like the pictures below.

![command-line-linux](https://linuxcommand.org/images/Screenshot-Terminal.png)
![command-line-mac](https://www.dummies.com/wp-content/uploads/111515.image0.jpg)

The command line should tell you who is using the computer, which computer you are using, and where in your files you are.

In the first picture, a Linux command line, `me` is the username, `linuxbox` is the computer name, and `~$` means that it is in the home directory, i.e. your default location in your files.

In the second picture, a Mac OS X command line, `arnold-reynolds-mackbook21` is the computer name, `~` is the home directory, and `agr` is the user. The same information, but in a different order.

Here's a couple examples of a command you can use in the command line: `pwd`, which is short for "print working directory".

![command-line-pwd-linux](https://www.linuxjournal.com/sites/default/files/styles/max_1300x1300/public/u%5Buid%5D/pwd.png)
![command-line-pwd-mac](https://www.imore.com/sites/imore.com/files/styles/large/public/field/image/2016/02/pwd-terminal-command-screenshot.jpg)

Notice that in response to the command `pwd`, the command line prints words separated by forward slashes. This is called a "path", and it's basically a hierarchy of parent folders. It tells you where things are located in your files.

In the upper picture, the user used `pwd` on their default directory and got back `/home/john`. In other words, `/home/john` is the longer, proper path name for the shortcut `~`.

In the lower picture, the user used `pwd` on the home directory `~` and got back `/Users/settern`. This means that `/Users/settern` is the longer name for the home directory.

Here's another command you can use in the command line: `ls`, which is short for "list". This command tells you everything that's inside your working directory, i.e. your current location in your files.

![command-line-ls-linux](https://www.linuxjournal.com/sites/default/files/styles/max_1300x1300/public/u%5Buid%5D/command-line-syntax-example.png)
![command-line-ls-mac](https://www.macworld.com/wp-content/uploads/2021/06/terminal-macos-big-sur-1-2.jpg?quality=50&strip=all&w=1024)

As you can see, Mac and Linux generally share the same commands.

The last command I'll show you for now is `cd`, short for "change directory", which you can use to move around inside your files.

![command-line-cd-linux](https://www.linuxjournal.com/sites/default/files/styles/max_1300x1300/public/u%5Buid%5D/cd-command.png)
![command-line-cd-mac](https://cdn.macpaw.com/uploads/images/Screen%20Shot%202018-10-17%20at%2018.14.23.png)

In the Linux command line, you can see that the user has moved because the working directory path has expanded, both in the shorthand that the terminal gives you before you write commands (the text between `:` and `$`) and as shown by the output of `pwd`.

In the Mac command line, the path the terminal shows you by default only shows you the folder you're currently in (`Documents` as opposed to `~/Documents`), and the user name comes after the current directory. Although things look a bit different, the user has likewise moved into a new folder.

There are lots of different commands, but for using the software in this guide, you only really need to know a few specific commands that come with softwares when you download them.

**If you want more details about command lines:**
Here's [a guide to the Mac OS X Terminal](https://www.imore.com/how-use-terminal-mac-when-you-have-no-idea-where-start).

Here's [a guide to the Linux command line](https://www.linuxjournal.com/content/linux-command-line-interface-introduction-guide).

### Installing software through the command line
You can also install software from the command line with a package manager. A package manager is a collection of tools that makes it easier to access software libraries and download software.

#### Mac
If you’re on a Mac, you need to install a package manager before you can easily download things from the command line.

One option is [Homebrew](https://brew.sh/), which you can install by pasting this into your command line:
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

You can also find the script above at on their [homepage](https://brew.sh/). Other installation options are [here](https://docs.brew.sh/Installation).

Homebrew commands start with brew, followed by another command. The essential commands are:
- `search [insert text here]` - This searches libraries for software
- `install [insert software name here]` - This installs software
- `uninstall [insert software name here]` - This uninstalls software
- `list` - This lists everything you’ve installed with Homebrew

For more details, visit [this page on Homebrew commands and terminology](https://docs.brew.sh/Manpage).

If you want to check out other package manger options for macOS, try [this list of 9 free package mangers](https://www.slant.co/topics/511/~best-mac-package-managers).

#### Linux
If you’re on Linux, you already have a package manager with commands that you can use to access software libraries and download software. The package manager is called Advanced Package Tool (APT) and it has various [`apt`](https://linuxize.com/post/how-to-use-apt-command/) commands you can use in the command line.

For example, say that you wanted to install a game about penguins. You can search the libraries APT has access to with the command `apt-cache search [insert word here]`.

```
user@computer:~$ apt-cache search penguin
ace-of-penguins - penguin-themed solitaire games
cairo-dock-cairo-penguin-plug-in - Cairo-Penguin plug-in for Cairo-dock
extremetuxracer - 3D racing game featuring Tux, the Linux penguin
ez-ipupdate - client for most dynamic DNS services
frozen-bubble - cool game where you pop out the bubbles!
icebreaker - Break the iceberg
linuxlogo - Color ANSI System Logo
muttprint - Pretty printing of mails
penguin-command - missile command clone
pingus - Free Lemmings(TM) clone
pingus-data - Data files for pingus, a free Lemmings(TM) clone
supertux - Classic 2D jump 'n run sidescroller with Tux
supertux-data - Classic 2D jump 'n run sidescroller with Tux (data files)
tuxtype - Educational Typing Tutor Game Starring Tux
tuxtype-data - Data files for the Educational Typing Tutor Game Starring Tux
xpenguins - little penguins walk on your windows
```

This gets you a list of softwares. The software name is on the left side of the dash, and the software description is on the right side of the dash.

But you might notice that not all of them contain the word 'penguin'. So if we only want to see softwares that explicitly mention penguins, we can narrow the search by adding a vertical pipe `|` (**Shift** + **`\`**), the general search command `grep`, and the word you want to search for.

```
user@computer:~$ apt-cache search penguin | grep penguin
ace-of-penguins - penguin-themed solitaire games
cairo-dock-cairo-penguin-plug-in - Cairo-Penguin plug-in for Cairo-dock
extremetuxracer - 3D racing game featuring Tux, the Linux penguin
penguin-command - missile command clone
xpenguins - little penguins walk on your windows
```

Now suppose that you wanted to download one of these softwares. You would use the command `sudo apt-get install [insert name here]`.

The `sudo` part of the command above isn’t part of APT. Instead, it’s a general security measure that you have to use when doing certain things, like installing software or changing your password. Using `sudo` means that you have to type in your password in order for the command that comes after it to work.

```
user@computer:~$ sudo apt-get install extremetuxracer
[sudo] password for user:
```
Note that when you type in your password, the command line won’t show the characters as you type them, but it is still keeping track of what you write.

If you type in your password wrong, you'll get this message:
`Sorry, try again.`

If you type in your password correctly, the installation will continue to the next step.

```
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  extremetuxracer-data libsfml-audio2.5 libsfml-graphics2.5 libsfml-system2.5
  libsfml-window2.5
The following NEW packages will be installed:
  extremetuxracer extremetuxracer-data libsfml-audio2.5 libsfml-graphics2.5
  libsfml-system2.5 libsfml-window2.5
0 upgraded, 6 newly installed, 0 to remove and 227 not upgraded.
Need to get 44.4 MB of archives.
After this operation, 49.0 MB of additional disk space will be used.
Do you want to continue? [Y/n]
```

At this point you will get a summary of the packages needed to install the software and how much space it will take up on your computer, and it gives you a chance to go ahead with the installation or cancel it.

If you want to go ahead and install, type `y` and press **Enter**, or just press **Enter** and the capitalized option, which is `Y` here, will be selected. After that, a lot of lines of text will stream past on your command line telling you about the progress of the installation. When it’s done, you should be able to find the new software with the rest of your applications.

If you want to cancel the installation, type `n` and press **Enter**.

#### Windows
Windows has an official free package manager [released on GitHub](https://github.com/microsoft/winget-cli). However, it appears to use the Windows-specific command line, which you can find a guide to [here](https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/).

There’s also an option called [Chocolatey](https://www.pcworld.com/article/2459950/how-to-use-chocolatey-a-delicious-windows-package-manager.html), but this one also appears to use the Windows-specific command line.

## Praat
### What is Praat?
[Praat](https://www.fon.hum.uva.nl/praat/) is a free phonetic analysis software. You can use Praat to:
- See waveforms and spectrograms
- Track pitch
- Track vowel formants
- Annotate sound files
- Extract information into spreadsheets
- And many more things!

However, for the purpose of this guide, we'll only really need to know how to use the annotation functions in Praat.

If you already know how to create, edit, and save annotation files in Praat, skip to the [Montreal Forced Aligner](#montreal-forced-aligner).

### Installing Praat
#### Official installation instructions
[Instructions for installing Praat on Mac](https://www.fon.hum.uva.nl/praat/download_mac.html)

[Instructions for installing Praat on Windows](https://www.fon.hum.uva.nl/praat/download_win.html)

[Instructions for installing Praat on Linux](https://www.fon.hum.uva.nl/praat/download_linux.html)

#### Command line installation instructions
Alternatively, if you have a package manager, you can install Praat from the command line, as discussed previously (click here to go back to that section).

##### Homebrew (Mac)
If you have Homebrew ([here are all `brew` commands](https://docs.brew.sh/Manpage)), try `brew search praat` and `brew install praat`.

##### APT (Linux)
If you have APT ([here are all `apt` commands](https://linuxize.com/post/how-to-use-apt-command/)), search for Praat with `apt-cache search praat`:

```
user@computer:~$ apt-cache search praat
praat - program for speech analysis and synthesis
```

Install Praat with `sudo apt-get install praat`.

### Using Praat
When you open Praat, a window should appear called **[Praat Objects]**.

![praat-1](https://lh3.googleusercontent.com/pw/AM-JKLUDbpGlNBOdy7m_3TGHIGryUc71IqM_LNqNBVJpE0cm3p83ee2kIa9IspNPB0HAQ8ILPYJQv7OCwqeWYBG0h2VGFA11z-HFztgOUS8fWiyNKjsw44kMK3LemUnj5199KOJFK8RPV0udPYgiBISb48tH=w532-h749-no?authuser=0)

(There will probably also be a window called **[Praat Picture]**, but you can go ahead and close that.)

To open files with Praat, click on "Open", then "Read from file…", then navigate the file browser that pops up until you find the files you want.

![praat-2](https://lh3.googleusercontent.com/pw/AM-JKLV1-Lr7ZuTJJ7HhDVfZmF3eD3Jmula2bedyQyfnwCpCiFHrSuV86q6goK-VZLwl9bV2VwPL74hJ_gJBvfk5EVTjzoREdR8pzgKOOfPQw4a6UH1Pyl-gMa9hZzsIkndbOf-FhYSUYEYazOOnqH4NpXmi=w532-h749-no?authuser=0)
![praat-3](https://lh3.googleusercontent.com/pw/AM-JKLXG4mJdCzkQRnlPxSv3apr2GRphwINBBftIO9bkZIfP9ZK5ri2395m9APY56xi7EEk-gPVzuVb1jRZHk11xK1agURq4RrnLHM84SC13srM7G_HDlUrynWXoi8zUW6Kwp3GBabo06pSvvQ8UCs2T0gIv=w532-h749-no?authuser=0)

Once you have a sound file, select it and click "View & Edit". A window will pop up with you sound file, like this:

![praat-4](https://lh3.googleusercontent.com/pw/AM-JKLXWP-CfXBuRxLPJqKEGU0o4zOUBU4QK2KK0S4iWJXycCXrOSt0U7JHMY2aCC6ONwKF_7ZuHG48A3agldpoCFHm95aYMs1K1scYzdRB7koZdvVNCtn7POj-sFZ0TDO4Phw1pKa1iIobSYtGVneQlhlOb=w1606-h902-no?authuser=0)

The top half of the window shows the wave form of the sound, and the bottom half shows the spectral analysis (aka spectrogram), which is all the difference frequencies present in a sound and how loud each frequency is. The darker the color, the louder the frequency there. The blue lines on the spectrogram are pitch tracking. The red dots and lines are formant tracking.

There are lots of things you can do with just this, for our purposes, the next step is to annotate the file so that we can tell from a glance what words are in it and where they begin. If you don’t already have an annotation file for the sound, you can create one by going back to Praat Objects and clicking "Annotate", then "To TextGrid…"

![praat-5](https://lh3.googleusercontent.com/pw/AM-JKLVSUNGyXvtKcejHZaZ2839X_IvGDY58NJbogaYLH34IuY2WQVEHWe7N_9DrQ8HxzXyqdJAn9dEXw50QpqnnZvf7UvjgUeKGKK_4yJJ2mSHD74Rvp2z5lcG_uzYWCY2Wg-CJNPGvVq5FChIN7e5pNRqj=w532-h749-no?authuser=0)

That will give you a pop-up that looks like this:

![praat-6](https://lh3.googleusercontent.com/pw/AM-JKLUXO4owfFIF-QW4Lm-422f2oMFoEeBNZtomk_yYw_PDS0MeWCPBOBiVbxrkoVEd9lwlqWy5aawZFJpXtxi8IlTymJc7n87tzapuHxE2fnyhGrnEpZSQm_9IZr91x2B2TahcFjPqifVGQDYOQ13oXnbJ=w536-h209-no?authuser=0)

Each word in "All tier names" will become an annotation tier. For example, you could have one tier for marking word boundaries and another for marking speech errors. For this example we only need one tier, and we don’t need any point tiers, so we change the words to this:

![praat-7](https://lh3.googleusercontent.com/pw/AM-JKLUQseIsoQLs0-_B1vApYf19V2Gj2sd_n8LSrWruLs-h9HiYLRTidZrSgrdSq7tHH7kBY6S3ZMUFyAGy_v01JpER0ForDIF0KtMNk_C4aMn_0g9HTd51d8-pA6iC3enq3i0bhiK3GRWtejcQS_mVXeQA=w536-h209-no?authuser=0)

When you click "OK", a new file will appear in Praat Objects.

![praat-8](https://lh3.googleusercontent.com/pw/AM-JKLW38BLUJKqdkCsO_g2GMdHwNlJ79TjaIvnY-aG2DzmAi1CXQh7NPo3oBG6ne_yFxcn0CaK71_ZKYmVltHHoeixTksv4B6XfvbvKQxNTPdcsaub5IGRSMeA0y0aQ20XHgqZ2elWNikv_YfjLoR7bkg3l=w532-h749-no?authuser=0)

Now, select both the sound file and the TextGrid and click "View & Edit".

![praat-9](https://lh3.googleusercontent.com/pw/AM-JKLVjrJchZyOzqXE8oY5uJzOdkSvuXhR9G2vq4oOLsJ3IuciG8kZo8dd5XvnmEpgZ6rMd4KJK9LT2OoNtQueiD-xpEp6m3RkGCSrhC8h1p1fPNngJFr7mRWvU51872kzQxTOjo54LvAkqHB6UXLU2TmBG=w532-h749-no?authuser=0)

That will pop-up a window that looks like this:

![praat-10](https://lh3.googleusercontent.com/pw/AM-JKLUzBLGU1yAZ1WvYp4QzlCf22TJBmw6A2qON5l5vukh9KFJYVgjHxlzVRQyL_tfwfQjD7C_0JcD1M2S5e5BcKPk6laRBAuayEx1k1q_8uW8NnHDlPxZTMP0p4xXsCS0AcocwMKXoMDzLlhFhPcNZBgst=w1606-h902-no?authuser=0)

The space below the spectrogram is the annotation tier. To annotate, simply click on it and start typing.

![praat-11](https://lh3.googleusercontent.com/pw/AM-JKLUjOJ0X6yYeQHQS2kFabp3d7gN9jQxAyhTe0Out7SY7xk3C3plsOMg_VNMQ0jS3ZwVlIumvcXpYhk7uenb4GTPt9YcXVg_W9JFZREZGhDzUIwaqdNvKeeyZg8lXzYTBE-Ro7JNmfB5wnRzwJ5SlSB4T=w1606-h902-no?authuser=0)

To annotate a specific part of the sound file, set up boundaries by clicking somewhere on the waveform or spectrogram and pressing **Enter**, or clicking on the circle at the top of the gray bar.

![praat-12](https://lh3.googleusercontent.com/pw/AM-JKLVwLg2YwkLa38RHWoNPK8JLP8HF4VhA25mh7320qGclQUnGt92ZMV4qOg0uPcpEZ2bhcA17OGDiqSMol-_t68IXuY4_lFYEalFQj3Qu7IDRzKoDP0Zq8Vp3-DRI2xtatptfbqaujoirSuPw9TiUvhxZ=w1606-h902-no?authuser=0)
![praat-13](https://lh3.googleusercontent.com/pw/AM-JKLXOEj4NQbaKQJtHGntymBD8Gdcw3-0gAlYt2dpeugJKBMnQeYsBC-v9r8QpcaLGVEiFnuh4-PNjlwEhzp3u-3Hn5-DnBw_7xTFOUm_IJjfvv5bNwf1tFsA3VLEopbAEDjregijSdDfsQH_8tXpZ3S16=w1606-h902-no?authuser=0)

To delete a boundary, select the boundary and the press Alt+Backspace.

If you create two boundaries, you can put an annotation between them.

![praat-14](https://lh3.googleusercontent.com/pw/AM-JKLVq5gYVC3Bb-REbfvD8GQM1PmKG24T4_ZBlASRVzDCmx8TGJQr6xZBzGTyQ4Y_Y2bBWPWP-c_EeTCiEbq5El8xbkthvjdiqTHLiG1jotqpAX9w4lXgpMb61T5MqpFIu6CYgD7AyUO2OyEKneKnYKU8U=w1606-h902-no?authuser=0)

If you want to listen to the selection, press Tab.

To save the TextGrid, go back to Praat Objects and select the TextGrid, then click “Save”, then "Save as text file…".

![praat-15](https://lh3.googleusercontent.com/pw/AM-JKLVpGNf8XqMiA9__sJmCraNTi34lsXj5GLe_5s6UDdlwPygkY_Y6MrBrjNhf0CL-qMOlXuD6ysvDHMLhRS7uhIkmV-y5nLI0yaok2oDwW7XirOmDLm7_MCCxnsJTk2ufaKL_6xor7yz9024xhdwLVFuz=w532-h749-no?authuser=0)

Then it will give you a pop-up file manager so you can choose where to put the TextGrid in your files. Put it in the same folder that the sound is in.

Once you have a sound file and a TextGrid with a transcription of what is said in the sound file, you’re ready to move on to the next software.

## Montreal Forced Aligner
### What is a forced aligner?
A forced aligner is a tool that takes an orthographic transcription and uses it to identify and mark sound segments in the sound file. Basically, it makes a more phonetically detailed, time-aligned TextGrid so you don’t have to go through marking everything by hand.

The [Montreal Forced Aligner](https://montreal-forced-aligner.readthedocs.io/en/latest/) (MFA) is one of multiple such tools. This software doesn’t have a user interface, however, which is why it has to be run through the command line.

### Installing MFA
Installing MFA is a little tricky, because it’s actually a Python package, so you need to have Python installed in order to get it. If you already have Python, skip to [Installing MFA (for real this time)](#installing-mfa-for-real-this-time).

#### Installing Python
##### Method 1: Conda
If you don’t already have Python, you can install Anaconda/Miniconda first ([instructions here](https://docs.conda.io/en/latest/miniconda.html)), which is an installer for Conda. [Conda](https://docs.conda.io/en/latest/) is a package manager (like APT and Homebrew, discussed earlier) that runs on Mac, Linux, *and* Windows. It was primarily designed for Python packages, so it automatically installs Python for you.

##### Method 2: Command Line
Alternatively, if you just want to install Python and not Conda, you can do so from your command line (or, if you’re on Windows, from multiple options) with the instructions below.

[Install Python on Mac OS](https://realpython.com/installing-python/#how-to-install-python-on-macos)

[Install Python on Linux](https://realpython.com/installing-python/#how-to-install-python-on-linux)

[Install Python on Windows](https://realpython.com/installing-python/#how-to-install-python-on-windows)

No matter what operating system you’re on, installing Python follows the same two-step process:
1. Checking to see if you already have Python, and if so, what version you have
2. Installing or updating Python

#### Installing MFA (for real this time)
pip is a Python package-management system that connects to an online repository of public packages. Once you have Python, you can use the command pip to install Python packages.

**If you have Conda**, you can install MFA with the instructions [here](https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html):

>1. Install Anaconda/Miniconda (https://docs.conda.io/en/latest/miniconda.html)
>2. Create new environment via `conda create -n aligner -c conda-forge openblas python=3.8 openfst pynini ngram baumwelch`
>    1. On Windows to use the aligner natively without G2P functionality, use the command `conda create -n aligner -c conda-forge openblas python=3.8`
> 3. Ensure you’re in the new environment created (`conda activate aligner`)
>4. Run `pip install montreal-forced-aligner`
>5. Install third-party binaries via `mfa thirdparty download` (see also [Building platform-specific binaries from scratch](https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html#collect-binaries) to collect locally built binaries)
>6. If you’d like to use `sox` to align non-WAV files, install a system version (The conda package from `conda install -c conda-forge sox` is missing a lot of codecs).
>
>To upgrade to the latest version of MFA:
>
>1. Activate your conda environment (i.e., `conda activate aligner`)
>2. Run `pip install montreal-forced-aligner -U`

**If don’t have Conda but do have Python and a command line**, just go to your command line and skip to the `pip install montreal-forced-aligner` command in step 4 and the `mfa thirdparty download` command in step 6 in the instructions above.

#### Installing a Pretrained Model
In addition to installing MFA, you also have to download a **pretrained acoustic model** and a **pronunciation dictionary** in the language of your speaker(s) in order for the alignment to work.

To download the English pretrained acoustic model, run this command:
`mfa download acoustic english`

To download the English pronunciation dictionary, run this command:
`mfa download dictionary english`

You can find the acoustic models and dictionaries for all the languages MFA currently has available [here](https://montreal-forced-aligner.readthedocs.io/en/latest/pretrained_models.html#pretrained-models).

### Using MFA
#### Instructions
The command to run the MFA is `mfa align`, and in order for it to work, you have to specify four things, in this order:
1. Where the sound file and TextGrid are (aka the input directory)
2. Which dictionary you’re using, including its location in your files
3. Which acoustic model you’re using, including its location in your files
5. Where you want the new, aligned TextGrid to go (aka the output directory)

In other words, `mfa align` has the following format:

`mfa align input_directory_path/ dictionary_location_directory_path/language.dict acoustic_location_directory_path/language.zip output_directory_path/`

This looks a bit complicated, but in reality, it’s actually quite a bit simpler, because when you install MFA, it creates a folder called `MFA` in your `Documents` folder, and the pretrained models you download automatically go into certain folders inside there. So the locations of the dictionary and acoustic model never change.

So if you’re using the English pretrained model, you can use this template, and the only things you need to change are the input directory path and the output directory path.

`mfa align input_directory_path/ Documents/MFA/pretrained_models/dictionary/english.dict Documents/MFA/pretrained_models/acoustic/english.zip output_directory_path/`

Just copy that command, change `input_directory_path/` and `output_directory_path/` to your input and output folders (including all the folders between your home directory and those folders in your path), press **Enter**, and the computer does the rest for you!

[**Here’s another guide to MFA**](https://eleanorchodroff.com/tutorial/montreal-forced-aligner.html)

#### Example
Say I want to align the `brown-fox.wav` file from the Praat section.

1. First, I create a folder called `brown-fox_input` that contains `brown-fox.wav` and `brown-fox.TextGrid`
2. Next, I create an empty folder called `brown-fox_output`
3. Then I go to the command line and use the following mfa align command:
    `mfa align College/phonlab/Tests/brown-fox_input/ Documents/MFA/pretrained_models/dictionary/english.dict Documents/MFA/pretrained_models/acoustic/english.zip College/phonlab/Tests/brown-fox_output/`
    which spits out this:
    ```
    All required kaldi binaries were found!
    /home/user/Documents/MFA/brown-fox_input/align.log
    INFO - Setting up corpus information...
    INFO - Number of speakers in corpus: 1, average number of utterances per speaker: 2.0
    INFO - Number of speakers in corpus: 1, average number of utterances per speaker: 2.0
    INFO - Parsing dictionary without pronunciation probabilities without silence probabilities
    INFO - Creating dictionary information...
    INFO - Setting up training data...
    WARNING - There were some utterances ignored due to short duration, see the log for full details or run `mfa validate` on the corpus.
    INFO - Calculating CMVN...
    INFO - Done with setup!
    INFO - Performing first-pass alignment...
    INFO - Calculating fMLLR for speaker adaptation...
    INFO - Performing second-pass alignment...
    brown-fox
    {'brown-fox': ''}
    WARNING - There were 1 segments/files not aligned.  Please see College/phonlab/Tests/brown-fox_output/unaligned.txt for more details on why alignment failed for these files.
    INFO - All done!
    ```

And that’s it! Now in my folder `brown-fox_output` there is a file called `brown-fox.TextGrid`. If I open `brown-fox.wav` together with the aligned TextGrid in Praat, it looks like this:

![mfa-done](https://lh3.googleusercontent.com/pw/AM-JKLVHE7wsMnV-hXvK6mfJKT7A1CLV36fV7tzyrPjrxGOMmoNEbT11Z9-lPJF5N6x5Yd6GXXuW12N6FQxlh6grR9306oK0NQruVF1EQQqA7xEwkXQ9inz1xBvY2ge6gDsXsuqKL7abLtp9A-0zRV0q3Nlt=w1606-h902-no?authuser=0)

#### Some things to note
Running MFA creates another tier in the TextGrid for the segments, and that it also aligns the words on the first tier.

For every tier that you have in the original TextGrid, MFA will add a corresponding phones tier. If you have a tier that doesn’t contain transcription, but instead has comments, MFA will attempt to align those comments (and have trouble), but it will be separate from the transcription tier, so you can ignore it.

Also, be careful of having empty tiers! If you have a tier in your original TextGrid with nothing on it at all, MFA will fail. Either get rid of the tier, or put some text on it, anything at all.

Also, the phones it uses in the segment tier are [Arpabet](https://nlp.stanford.edu/courses/lsa352/arpabet.html) instead of IPA because that’s what the English pronunciation dictionary uses. The numbers on the ends of the vowel mark stress, which will be important when we get to FastTrack.

## FastTrack
### What is FastTrack?
[FastTrack](https://github.com/santiagobarreda/FastTrack) is a plug-in for Praat that tracks vowel formants. Even though Praat has its own formant tracking automatically, it can make mistakes and it’s not very flexible, so FastTrack is a better option.

[Watch this short video (2min) about FastTrack](https://www.youtube.com/watch?v=NaAKJJaPD8Y)

### Installing FastTrack
Compared to all the software we’ve encountered so far, FastTrack is by far the easiest to install.

1. Go to the GitHub repository [here](https://github.com/santiagobarreda/FastTrack), click on the green "Code" button, and select "Download Zip". This will give you a file called `FastTrack-master.zip`.
    ![fasttrack-download](https://raw.githubusercontent.com/santiagobarreda/vowelhost/main/FT-wiki/download.png)

2. Extract the `Fast Track` folder from the zip file and put it somewhere in your files. I recommend putting it in `Documents`, since `MFA` is already there.

3. Inside the `Fast Track/functions/utils` folder, you’ll find two “setup” files called `setup_compact.praat` and `setup_lazy.praat`.
    1. `setup_lazy.praat` adds buttons to Praat in the format in the picture on the left below
    2. `setup_compact.praat` adds buttons to Praat in the format in the picture on the right below
    ![fasttrack-setup](https://raw.githubusercontent.com/santiagobarreda/vowelhost/main/FT-wiki/buttonlayout.png)

4. Pick one of the setups and run the script. To run the script:
    1. Open Praat
    2. Click **Praat**, then **Open Praat script...**
    ![fasttrack-script](https://lh3.googleusercontent.com/pw/AM-JKLWGqb3CZZ0rIuhjIbMvNoE_Kh3Kba899EifvCYna4JtzH20f0-RWN5AODpzRJyzj7DsMNY5Po3UDxbMeZaRSgCE69hNiUJseg0i3rpP_qv99G-jYvzL47rQr4wSSEbknTrsAMAqlBmyqixPgsqLh8s_=w532-h749-no?authuser=0)
    3. In the file manager pop-up, navigate to the `Fast Track/functions/utils` folder and pick one of the setup `.praat` files

And that’s it!

Note that running a “setup” script will add buttons that call Fast Track functions to the bottom of your Praat object window. You may not see them appear until you select an appropriate Praat object (e.g. a Sound object).

To change layouts, or if you move the script files, simply run the setup script again.

[**Official instructions here**](https://github.com/santiagobarreda/FastTrack/wiki/Installation)

### Using FastTrack
There are two parts to using FastTrack: extracting vowels from a sound file, and then analyzing all the vowels inside a folder.

This two-step process is because FastTrack can only track one vowel at a time. So first all the vowels you want analyzed have to be extracted into their own short sound files.

Once you have a folder of these individual sound files, FastTrack can go through the folder and track the individual vowels one at a time.

#### Extracting vowels
1. Open a sound file and its MFA-aligned TextGrid in Praat. Select both, click **Fast Track**, and then click **Extract vowels with TextGrid...**
    ![fasttrack-2](https://lh3.googleusercontent.com/pw/AM-JKLU21RpaQtAzJ2zfxXMZ-ZIlAlH1LjKlzgZ-41aTbbRs-QBnc0CFmz-OBAJduPiou3SVUEzQibaTk3kuf4yTQ_Uhe6GMaWg2Xbt_f8CbibCMpEWzEDd0riBUTneoL_NV57ke1zA7sk7P3gXVaKRik0HK=w532-h749-no?authuser=0)

2. A pop-up called **[Pause: Set Parameters]** will appear.
    1. In the space next to "Folder", provide the path from wherever your `Fast Track` folder is stored to the output folder for your sound file
    2. Set "Segment tier" to 2 (because the segment tier created by MFA is the second one down)
    3. Set "Word tier" to 1 (because the tier with words is the first tier)
    4. **Make sure that the box next to "Stress is marked on vowels" is checked!**
    ![fasttrack-3](https://lh3.googleusercontent.com/pw/AM-JKLXYz7IIu8g81uQVWkQiN0PU--JpOjFQMlT7xsrneFPb8GDppSubWQSdXKDEBnzVRAoKOI0mgItMKFD51GQvVbKbgyYmmJyErxIsE2HAUV3bDyEZWP0QKb0bpBD4rY31A1BkN1lEMxA2vF4_V9uvqJs7=w536-h751-no?authuser=0)

3. Press **Ok**

4. Now when you check your output file, you should find that these three things have been added:
    1. a folder called `sounds`, inside of which is multiple `.wav` files called `[sound file name]_0001.wav`, `[sound file name]_0002.wav`, etc.
    2. a file called `[sound file name]_segmentation_info.csv`
    3. a file called `file_information.csv`

#### Tracking folder
Now go back to **[Praat Objects]** and select either the sound file or the TextGrid.

1. Click **Fast Track**, then **Track folder…**
    ![fasttrack-4](https://lh3.googleusercontent.com/pw/AM-JKLVpApMVfL50eOeuJNPZlg83O8ODpaqz3PVOGiMQSdRMuVmGe-0L7i1kTwsBdhEvgNg67TDdxEmBD9K2-k6TZtKDxDk_xhUD39jg9_Syl99vS4hUEG5r5KpqvP6LpwomacSn7QpJDSoiDmSN6iUBdSaB=w532-h749-no?authuser=0)

2. A pop-up called **[Pause: Set Parameters]** will appear.
    1. In the space next to "Folder", provide the path from wherever your `Fast Track` folder is stored to the output folder you used for extracting the vowels
        1. Do not select `sounds` as part of the file path! FastTrack needs those two `.csv` files, so you need to provide the folder that contains the `sounds` folder and the two `.csv` files
    2. When the pop-up appears, "Make images comparing analyses" will be automatically unchecked and "Make images showing winners" will be automatically checked. But if the sound file you extracted the vowels from is long and has hundreds of vowels, uncheck both boxes! Creating the images adds a lot to the time it takes the computer to finish.
    3. Set the number of formants to 4
    4. Make sure the four boxes "Track formants", "Autoselect winners", "Get winners", and "Aggregate" are all checked
    ![fasttrack-5](https://lh3.googleusercontent.com/pw/AM-JKLV7EW6t6MepUaH_91IuMk7fOVhZtVDhBF-Ceef_xBzcmjhwpxEGD0_GsK0vrlXm_e7fo5mK-1graU40pW7cjXxc4zxt7l7aACgquRZ2Ptde7J_CtYHuMqmfPz1BK11Q1_LSCylhPEA3q0Gm00DvGhYZ=w536-h736-no?authuser=0)

3. Press "Ok".
    As FastTrack runs and creates pictures, **[Praat Picture]** will pop-up. Even if you uncheck both images boxes, at the end FastTrack plots the vowels for you, so there will be at least three images.
    ![fasttrack-6](https://lh3.googleusercontent.com/pw/AM-JKLUAC_CfQzDFNJzrqaYcQyBe4aJfoVxSfLBpw2Z-MzUsDl1NLl7qgcvbhy1nFmBe0kj7Ek36Y7_kEFqG1ifwfy-TnFTIGS5ld9BPUowCRwZc8kWOGRAUa91cXs_z72hT-DrTatGcNuBXg5MfkEqYs3Uw=w553-h902-no?authuser=0)

4. Now when you check your output folder, you should see the following added things:
    1. a folder called `csvs`
    2. a folder called `formants`
    3. a folder called `formants_edited`
    4. a folder called `formants_winners`
    5. a folder called `images_comparison`
        (this folder appears whether or not you check the comparison images; if you uncheck that option, the folder will be empty)
    6. a folder called `images_winners`
        (this folder also appears whether or not you check the winning images option; if you uncheck it, the folder will be empty)
    7. a folder called `infos`
    8. a folder called `infos_aggregated`
    9. a folder called `processed_data`
    10. a folder called `regression_infos`
    11. an image called `contours.png`
    ![fastrack-countours](https://lh3.googleusercontent.com/pw/AM-JKLXETl3LeQvaqF9rbcaJ2oruupf-mOxsFH7lYBre2M7-DskQIkF8aYvt-NUTDxGslojr1YR9wgiwLmBIh77fyGseAZxH5Oz27tv85QXpMCBfllLOx_w0lbfH_ZW5aCQghkImhuNCsWjpnu9Yf1gSQo4R=w1504-h902-no?authuser=0)
    12. an image called `label.png`
    ![fasttrack-label](https://lh3.googleusercontent.com/pw/AM-JKLWB3pDN-IaCtMwS381ReYlPpWK2QDyz2Q_DVtZNCXlM4hEm_nGGc62jOpfcdnB8Bi8tw3JjAumoB8tvAmk2Po1nHaRVEEtFoJgLx-MZ4YG0sD1en5isfESo_1j7PdZEV5Xi52R1ciq7pCNJtcl_0P1I=w1504-h902-no?authuser=0)
    13. an image called `number.png`
    ![fasttrack-number](https://lh3.googleusercontent.com/pw/AM-JKLXYpT5n6v2-dMgTg7k_Ef-kLgq3rJLSwnS2ovCKxcYiVPUPAORDYGS0EziOdC_CmiBMKtoc6s2Ci5rujqBlx4uq4W0LYJxhWQN6JN6NEw1NHhGRipPRJDdyGXvv990fXIQKc28ZgQJXmWDcLkHIAMH-=w1504-h902-no?authuser=0)
    14. a file called `winners.csv`
    15. a file called `winners_backup.csv`

And that’s it! You end up with a lot of stuff at the end, but all you really need is the file `aggregated_data.csv` in the `processed_data` folder.

##### Some notes
In my example, FastTrack took about half a minute to finish, and that was with both image options checked (although I unchecked the boxes for the screenshot).

But when I’ve used FastTrack on almost 900 vowels at once, it took about 12 minutes with just the winning images selected, and between 6 and 9 minutes with both image boxes unchecked.

##### Example Output
If you want to take a closer look at the output that FastTrack spits out, you can go to [this shared google drive folder](https://drive.google.com/drive/folders/1BIVARVwvwOFkhwpEGkxdSxW4u66DRjfH?usp=sharing). I’ve also included the original .wav file and the MFA-aligned TextGrid if you want to try running the FastTrack example from the beginning on your own computer.

## Organizing the Data
The `aggregated_data.csv` file that FastTrack gives us is comprehensive but it’s not the most convenient. For example, it collects formant measurements at five points across the duration of the vowel, but it doesn’t calculate an average for those measurements. So there’s some clean up and calculations we have to do on the file to make it more usable.

There are three different ways you can do this:

[**Method 1: Via spreadsheet**](#spreadsheet-method)
- Nothing new to install
- Manual data entry and manipulation
- No coding but more effort

[**Method 2: Via Python in Jupyter Notebook**](#jupyter-notebook-method)
- Requires installing some new things
- Comes with a template, only needs minimal changes to work
- Involves some general knowledge about Python but less work

[**Method 3: Via Python script `organize.py`**](#python-script-method)
- Requires installing one new thing
- Runs from the command line; no knowledge of Python needed
- All the work is done for you, but you have very little freedom regarding the output you get

### Spreadsheet Method
#### Importing the data
Start by opening a new spreadsheet in the software of your choice.

(For this guide I’ll use Google Sheets, but the instructions refer to general spreadsheet tools that you should be able to use with any spreadsheet software.)

Next, import the `aggregated_data.csv` file into the spreadsheet by clicking on "File" and then "Import".

![spreadsheet-1](https://lh3.googleusercontent.com/pw/AM-JKLVQ3mFtT9ssp2ZbLOWO-zACrsH7UrXVcvoPc9Rp4XYz9V-DNcJH3b7iTlyIiiAaOZVGRzU8kXLwtLcrILMY4cQ_JiAntecVsgWkBqPTkBurpezk5GzNf-XyBkvYVeBE-0qXgdXcZQNueAvgxTMdCZY-=w1852-h898-no?authuser=0)

Once you open the file, it should look something like this:

![spreadsheet-2](https://lh3.googleusercontent.com/pw/AM-JKLXKEwal05hCAWENS3OD4mr419cvHLKeatMHg285jRhEyaBxXatsu1-k0g-vz3ipRLc-nDPoT0WrHzYdZrv00auk2vdNd9p12u3dgQruuUm6QuvXXccIuKVPdMCC176bbqmr09Kqum2kcVXvkc2rxohc=w1857-h516-no?authuser=0)

`aggregated_data.csv` has the following columns:
- `file`, which refers to the vowel sound file extracted by FastTrack
- `f0`, which is the pitch
- `duration`, which is is the length of the vowel
- `label`, which is which vowel, using whatever label was in the TextGrid used to extract the vowels
- `group`, which is which vowel again, with a different number corresponding to each vowel type
- `color`, which is the color FastTrack used in plotting the vowels
- `number`, which is the number of the vowel, with a different number for each vowel extracted
- `cutoff`, which is the point above which FastTrack stopped looking for formants

The rest of the columns are the formant measurements. FastTrack by default measures the formants of a vowel at five evently spaced points along the duration (called "temporal bins"), so there are five measurements of each formant.

The first number after 'f' is the formant number, i.e. whether it's F1, F2, F3, or F4. The second number is which temporal bin the measurement belongs to, i.e. whether it's the first, second, third, fourth, or fifth measurement along the vowel duration.

So 'f12' is the second measurement of the first formant, and 'f21' is the first measurement of the second formant.

##### Combining multiple `aggregated_data.csv`s
If you have multiple related sound files that you've fed through FastTrack and you want one big data file with all of them, you can import another `aggregated_data.csv` and append it to the current sheet.

![spreadsheet-3](https://lh3.googleusercontent.com/pw/AM-JKLX7gldiA1vyjjPDo2GpcuAEAdkU7mrnortLOOHBkJrYkttz3CVWGqOxy8TjeMbN3NmaxG0MNJOAU5lUjwd5DD5aWkG-FuEamT96Dhyd5eXiBqKVwRbMVmv2Tt-eGUsR6PXxAWdVf2QWuN64veVPK0BO=w1851-h893-no?authuser=0)

After which, your spreadsheet should look something like this:

![spreadsheet-4](https://lh3.googleusercontent.com/pw/AM-JKLVh1AdS866bU0cvZHM1GWobEBgImIGJXDViJFApO2YGsQef5LIfe_rKnULJ3FbZ4PXWQj9O8B0HUEykxb9vwfZqtLIxpO67N_HJCBqse7fnrJVy0K-p0GmxzxjknBx8KwLD3WFzuBN65fCudfA3xi3M=w1855-h897-no?authuser=0)

Delete that second header row from the appended file.

![spreadsheet-5](https://lh3.googleusercontent.com/pw/AM-JKLWaovjXGriKYKWag-X_WgrieNl22Q-woWXK_ZrukUS_U_Iw3_ciFMsKB25poXqU-kQHMR_30c6Omsq7zWxbq_wxtGPx3LcxFj7AbUD0amq_c4g-vgznWm3hIBQkgoOaW0s0AKcJ0fAgZxYzOnUNACJU=w1855-h895-no?authuser=0)

#### Cleaning up the data
Now, when working with your data, there may be times when you want to refer to all the rows belonging to a sound file that FastTrack extracted from.

Right now the extracted-from sound file is entangled with the extracted sound files in the column 'file', but we can split that into two columns to make it easier on us.

Insert a column to the right of 'file'. You can name it 'file' as well, or 'speaker', or 'subject', or anything really.

![spreadsheet-6](https://lh3.googleusercontent.com/pw/AM-JKLVrHYslDtqWtUMokIIl73p1a1A4-h-c3B0p_xnQ0pmIFoyo5IN9iH_um679aSXRcMi3Jm6cPa3OHYivh4BHvw11PK78Exk-vExkI1MwJQGuzdBnYEE2d4zFaD9-Op1jF7LeGD2Rwt9iKytKqOrySrM4=w1856-h898-no?authuser=0)

Write the file name (the part that comes before the underscore in 'file') in the first row of that file series.

![spreadsheet-7](https://lh3.googleusercontent.com/pw/AM-JKLVBmQ089HFiSrbKVXM4VydmGBWr9tHsHYnoEz4f_kv4djs-6jIpK3vI3mYBpvmb7IPsWQxnTi4OFQ1eldGvBhdXvVLnGdOIJU-B1jo2VWB1nfxPfzla0926m8kTElWA4m4cyqHkgvzN9Xdr23Or2y88=w1855-h897-no?authuser=0)

Select one of the names, then click and hold on the square at the bottom right corner of the cell and drag it down through the empty cells.

![spreadsheet-8](https://lh3.googleusercontent.com/pw/AM-JKLW1fKXvWiLfhymE5lfzp3LSkA98NnXlo7FyzEQtgoC8beTQay1-gR6CejnCTfCGKj-k2JMy1oK_s02AwaByIzuN6JD2HeuUUmvZa4DB94k99pA3LJ1OFNi9ctOqmc4XZfxdHsortHNhA3VpPa98EIVd=w1855-h894-no?authuser=0)
![spreadsheet-9](https://lh3.googleusercontent.com/pw/AM-JKLUDXC3T7TbtTEdZNaYrmntLDCcvmPF7mJN-0EBRq2Znlx-_fn6I29nv95cuAFPvEcsgi5ytQsY4US7XmrpWnkvhuE7i4DzySTMjp9XTY_ML6XcukcHIYgQNxfvWWTpYuckaInnmYrnSUyFSLJ9HiS7a=w1855-h897-no?authuser=0)
![spreadsheet-10](https://lh3.googleusercontent.com/pw/AM-JKLVaC5HfwxLThBZZ04xiIFSeBYZx8dvfWBohxpz8rIwbbRQJJihURFdacf__cYXmkrnHTetFPNv9UbqZ2DzGN_jKpX3PGVwgTMpT7JFsL99ODhrAXTpZYGHYld_Z1UIWWKhnKZMCrT3QPQUZqkKKcH9d=w1855-h898-no?authuser=0)

Delete the first 'file' column.

![spreadsheet-11](https://lh3.googleusercontent.com/pw/AM-JKLXLtRCOBvXFXKY7vgeZMnleSQ-fVzFpf9Igc6BZgbR3WBGr3y9ofEKv3qyJjp2MltSff87GRnTGKJAymo8DL53wQRVWlN5Accrf2XKCWGzJs8m8GY46r11TH2UzE-0PU9z5ufvMqOPBVAPIaHf22bTZ=w1854-h897-no?authuser=0)

If you want a number counter for the sound files, you can move the 'number' column over by clicking and dragging it into place and use that.

![spreadsheet-12](https://lh3.googleusercontent.com/pw/AM-JKLWJebclrcfkS8T6TGg64wqzf0--a2AKcxqRNDafYfeOJp7f5vCeI0vlJIcMCa56Gq_E-S_Otzvv6uZ7jSoC7EJviOQehs0V2ewJvehF9hGFmy2pKiCt91b5o61MTQ6PMq0x2Qd79uR4HJd4BUhTNWSI=w1857-h894-no?authuser=0)

At this point, since 'group' and 'color' really only have to do with FastTrack's automatic vowel plotting and 'cutoff' isn't important to the vowels themselves (only to FastTrack's processing of the vowels), you can hide those columns or delete them. Select the columns and right-click on them to see your options.

![spreadsheet-13](https://lh3.googleusercontent.com/pw/AM-JKLWQS9KT3GKR_AE2AFsa2WDjBEuZ8_jeXz7rw4oKcMIUUdcxUVjKW0qo8CbqK4d9746lhQYFYXDgHKIQiDR53vBTBd-F5Lgo9n-MNYA1aYO_QRRfTwq9EiaQ16TMhj_2J27RdyEDd_2Erle5C1wPw7Bn=w1857-h895-no?authuser=0)

#### Average vowel formants
To find a vowel's average formants, take the mean of the middle three temporal bins. In other words,
- the average of F1 is the average of 'f12', 'f13', and 'f14'
- the average of F2 is the average of 'f22', 'f23', and 'f24'
- the average of F3 is the average of 'f32', 'f33', and 'f34'
- the average of F4 is the average of 'f42', 'f43', and 'f44'

First, make four new columns at the end of the spreadsheet for the mean formants.

![spreadsheet-14](https://lh3.googleusercontent.com/pw/AM-JKLX5KKLkhu5vJgZ5_6V6_Ug4BLqOypx9tQ6UnNQf_yT-NgqTqYgM30wgAXzcgDuMVDnSU8UfcwMkNEFuMUqaS3t-lh3GqkbCgg3LEzD90vI3Sni5gmQcpOGxVGUbLCMDpw1lUsgVhkakrfCX4-B71Y0Z=w1857-h895-no?authuser=0)

In the first empty cell of the 'f1_mean' column (or whatever you named it), insert the following formula:
`=AVERAGE(M2,Q2,U2)`

Note that if you chose to delete 'color', 'group', and 'cutoff', or if you added any additional columns, you may have to change the formula to whatever columns 'f12', ‘f13', and 'f14' are in.

![spreadsheet-15](https://lh3.googleusercontent.com/pw/AM-JKLWLekjhUHaC_ZK8xtgYUIBpituP-pp66G3pICP-pEevlEFJm5xOcNzn0cChsTvg93XHDKJdvtPC1KPpOoXUBx3JGfqy6wKYJ3w0KORUDLqsBfvI7bZQC7-zfaSFID_i7UVsw5LyVOzk0BL6KMCU4ooq=w1920-h897-no?authuser=0)

Now either drag the formula down the column or, if Google Sheets gives you an autofill prompt, accept it.

![spreadsheet-16](https://lh3.googleusercontent.com/pw/AM-JKLVIHGuuauZEcBudrAFZCIzFplXcixj2Rxo_ewcSJqb0BmNHxmE7tmZ04qj-AgcrvjxazUA5Ts7hyiLXu5S9tnAj29z_6NQ68nvgKubvfykVTMKePtacsz2jL4b-B6XoKS06_-6bbbjpNfjLB_GZDLWs=w1855-h895-no?authuser=0)

Repeat process for the other three mean columns, changing the formula to get the right columns.

For 'f2_mean':
`=AVERAGE(N2,R2,V2)`

![spreadsheet-17](https://lh3.googleusercontent.com/pw/AM-JKLXlgNqGq82bNWuARcA3ubLLXOEW0bCdaMy8QMMINnVOCQmEaVzPHdaBY88Ph4vPyd1VqjpNl-Cl38oEeVLlJCzyxoTkTCP4t0UzKMkR4Dt62cDy_-1Pu0WKOAQuzn9OGp3FG-j97KGtnSEjs7RL0Osf=w1855-h894-no?authuser=0)

For 'f3_mean':
`=AVERAGE(O2,S2,W2)`

![spreadsheet-18](https://lh3.googleusercontent.com/pw/AM-JKLUJxzULmQp6jo9JGCkdo-zyp3xiHYJPPG2kbNjLMPL6fbpudk9KA6OCSn0SkNso72RABMuGDIQ5WRKbUuniYr-P5s9pGplgzGVTy1M88po-fe-6XMjEhMv9tkvVGnALZNu_EL6AAeJPenhxhNCLzvve=w1855-h895-no?authuser=0)

For 'f4_mean':
`=AVERAGE(P2,T2,X2)`

![spreadsheet-19](https://lh3.googleusercontent.com/pw/AM-JKLVFsqj0XG_SJn1KYZhjSnkRvTYDEJWaD258ZET_p7JZfUwnEKcr8fNE-pjhohbdxi9PF_Trt_UXEgRd5bvjKlMB5AROxec2Trzvq-51LLQViljZ2nHOcIGKPB0ob3KAyFClVHyY47HZxz-8a6BK_iXf=w1855-h894-no?authuser=0)

To clean up, get rid of the decimals in those four columns by selecting them and then clicking on the "Decrease decimal places" option.

![spreadsheet-20](https://lh3.googleusercontent.com/pw/AM-JKLVurY-JfX99IXa4tPksa-lxyGDEi--1aJdOeuUVs2bTsD9L5JtSQoBBQ3G05R1DY_bFsqasxFxRvrNElUBYFoDw34TkZmgX-9r2s9racihx3U6xFFdmk1cPIB_aW9lDXnD8pHF5u7jf26-d2ToxJ8Db=w1855-h897-no?authuser=0)
![spreadsheet-21](https://lh3.googleusercontent.com/pw/AM-JKLWYkIddygu1WHkhu-dPVrAZYS_woWPbuRb8P30gts1oO_znkd7NI8188iKFeNDwCpr4ktFPil2PjaESMiIpNgd7QKeu8Nb0q96aweRjPO1UNPs29vTVzlvK9Biruy4DKRFJQexnANE-s7IxkZioYZdj=w1855-h897-no?authuser=0)

#### Vocal tract length
Another value that FastTrack doesn’t provide but which is important to vowels is vocal tract length.

Basically, how long or short the vocal tract is changes which harmonics will resonate and become formants, in the same way that tubes of different sizes produce different sounds, or glasses with different amounts of liquid make different sounds.

Since men tend to have longer vocal tracts and women tend to have shorter vocal tracts, vocal tract length is especially important to figure out so you can guess how participants will react to voices.

##### Equations
The vocal tract is essentially a tube that is closed at one end—the glottis—when voiced sounds such as vowels are being produced. Because of this, we can use the resonance equation for a tube closed at one end:

$f_{n} = \frac{(2n-1)c}{4L}$

In this formula,
- 𝑓   = frequency (Hz)
- 𝑛  = resonance number (e.g. 1=first formant, 2=second formant, etc.)
- 𝑐  = speed of sound (35,000<sup>cm/s</sup> in warm moist air)
- 𝐿  = vocal tract length (cm)

Solving for length, we get:

$L = \frac{(2n-1)c}{4 \times f_{n}}$

This is the equation we use to calculate vocal tract length.

However, by changing the shape of our vocal tracts with our tongues and throat, we can change the resonances of our vocal tract in ways that do not have to do with vocal tract length. In fact, this is how we produce different vowels.

In vowel production, F1 correlates inversely with vowel height and F2 correlates directly with vowel frontness. Because of this, those formants are not reliable indicators of vocal tract length.

So for finding vocal tract length in our data, in the end we want two measures: (1) the average length of all the formants of a vowel, and (2) the length of F4, because F4 is the least affected by vowel quality.

##### Finding vocal tract length
First, create four new columns.

![spreadsheet-22](https://lh3.googleusercontent.com/pw/AM-JKLVKKwiJvZqvlx_aHEhpz_a1w3FOV-Ps3T6qctmF19mpRGw75BRjo7vIxoz49JDO-VWF3OA_y68mubyaurf-DItKEz7lNsQKhouyL4hMuv6MVFF4Cd6wxcq20vRdUIYKZ8_Ga9g1ZBuq0EaAiWBru3aG=w1857-h895-no?authuser=0)

To find the length of F1 (which will be part of the average length), use this formula and drag it down the 'length_f1' column or select the autofill option.

`=(35000)/(4*AC2)` (you may have to change the column name depending on where your 'f1_mean' is)

This formula comes from simplifying the vocal tract equation for n=1.
$L = \frac{((2 \times 1)-1)35000}{4 \times f_{1}} = \frac{(2-1)35000}{4 \times f_{1}} = \frac{1 \times 35000}{4 \times f_{1}} = \frac{35000}{4 \times f_{1}}$

![spreadsheet-23](https://lh3.googleusercontent.com/pw/AM-JKLUe49ovju70my7oaVL5_Oz-KHGGZy4Yi6Ie0zXyA0tnJ3TH9dIhSe_kny1E1GQ4qgiRc7acAWSEnqR-F0fdLSKf3fOVmJtAmV7oIWUCi1hfvo0lNWTjM4pxO8QFH5jmAhsnPDOR1jqp-dA1c2V0TRPl=w1855-h894-no?authuser=0)

To find the length of F2:
`=(3*35000)/(4*AD2)` (you may have to change the column name depending on where your 'f2_mean' is)
$L = \frac{((2 \times 2)-1)35000}{4 \times f_{2}} = \frac{(4-1)35000}{4 \times f_{2}} = \frac{3 \times 35000}{4 \times f_{2}}$

![spreadsheet-24](https://lh3.googleusercontent.com/pw/AM-JKLV1ijctkoUhWQQ3_iG1SNFTFEId5FwPR9YvGTaszFbjtpkc9D0jFlC7Tp0qvYn8ib6y2id7703ntgd2AuUOagurri41aJc7Z3DsJhlacRTJyiHuc8z-ALgLguU6Jn-08UMcmkcojeuSxCTbxMr34M-A=w1855-h895-no?authuser=0)

To find the length of F3:
`=(5*35000)/(4*AE2)` (you may have to change the column name depending on where your 'f3_mean' is)
$L = \frac{((2 \times 3)-1)35000}{4 \times f_{3}} = \frac{(6-1)35000}{4 \times f_{3}} = \frac{5 \times 35000}{4 \times f_{3}}$

![spreadsheet-25](https://lh3.googleusercontent.com/pw/AM-JKLWP_rC-Wm35MC9x5rxlEvxqZvEaToLDxUwoavr-Z6QnHpIsHzpq9ihmMLwKNwXQA26G_HI9DPDXkOyS_UQuDyZ6qjJKiNmaBOr0N096mPmgEFRKriIvOD21fOrb0S1i29FL-jekuaxo2b9vxfKQYhbe=w1855-h897-no?authuser=0)

To find the length of F4:
`=(7*35000)/(4*AF2)` (you may have to change the column name depending on where your 'f4_mean' is)
$L = \frac{((2 \times 4)-1)35000}{4 \times f_{4}} = \frac{(8-1)35000}{4 \times f_{4}} = \frac{7 \times 35000}{4 \times f_{4}}$

![spreadsheet-26](https://lh3.googleusercontent.com/pw/AM-JKLU0aVxcCTz_wdiEjtrM7To4odgWZ4MYNXTrYHFfLTpUBsmey6RAKdPgDZYx5owFNSFqQaNXn3O40WQkPhdoYsNbBU9OoZl8I_hL-gx9v2mA5h5MR2efCkWwynCxiVFocpGrY71HGOpsY9aRvcJ6Acu7=w1855-h894-no?authuser=0)

To get the average:
`=AVERAGE(AG2,AH2,AI2,AJ2)` (you may have to change the column names depending on where your 'length_f1', 'length_f2', 'length_f3', and 'length_f4' columns are)

![spreadsheet-27](https://lh3.googleusercontent.com/pw/AM-JKLXlC5iMfjjvg6vXj_6l16iOS3fsRij0r6lTtJc-6roZ044zrcU_CDnUhoNbvcAexI7fTZR0jNgiXV5JTRKDFvi-kEepjshnlmrYu1dC3klm7BFqzTYlH3uyeoipAbXCU9VPIbu8CZWC2zFYCKWGpvbg=w1855-h895-no?authuser=0)

Lastly, make sure that the length measurements have two decimal places.

![spreadsheet-28](https://lh3.googleusercontent.com/pw/AM-JKLU5rSlxQaBYfVo6JoNQCwCqAZJ-OscSsWjgCgMqL9sHtqmwDPEazxzE-xh37xv4-if9EUTyaWooNkMpbabm94IUFZ8lQOcIlhkI66bDl8vZ2ktTC8b4IdTElVy6NwyhbbBhW5GiCoyxUACA9E9iid3e=w1854-h897-no?authuser=0)
![spreadsheet-29](https://lh3.googleusercontent.com/pw/AM-JKLWLafW-gTaG16Ls5-AgGfzVSB7ZG7sWyDBtsosPOxYnHVn_f9WCZn-EqQegKZEXsc5b2RlFt8HJms9ULbASfGvGC0TyKG9QaGwMeTBE9BrbJWJly4ovlyc_lQOGQkAhuAoEUcBrQJG_CSTmxqssq4j-=w1855-h895-no?authuser=0)

At this point we have three length measurements that we don’t really need: the lengths for F1, F2, and F3. But since we’re using a spreadsheet formula to find the average length, we need those columns.

If you want to get rid of the no-longer-necessary lengths for F1-F3, you can download the file onto your computer or export it to another format. When this happens, the formulas disappear and are replaced with the answer they calculated. Once you have a file without formulas, you can safely delet the length columns for F1-F3.

#### Exporting the data
If you want to download a version of the newly organized data from Google Sheets onto your computer, click on "File", then "Download", then "Comma-separated values (csv, current sheet)".

![spreadsheet-30](https://lh3.googleusercontent.com/pw/AM-JKLWTIVnVBZ42nBc0mGI7ZYNLw9znYzEYQpN6IR6qNZTJRtSIQR_wSCxm1sqnCrPcTSzlsHYCuKp4-qqGhB2LY8IcTZKt2WbDfysiqvHtiA7GQJAYfWzMyIdtwiVRqDe_GgIY_2bgI88qeWVNS_Ar1Jxp=w1855-h901-no?authuser=0)

If you’re using a different spreadsheet software and want to export the file, you can usually find exporting options somewhere on the dropdown menu under "File".

#### Example/Template
[Here is the link to the spreadsheet I used in this example](https://docs.google.com/spreadsheets/d/1TfOCyHjGXg4PfkEMcdQqmSilxv_bw738C79DZKNpYSE/edit?usp=sharing)

### Jupyter Notebook Method
#### What is Jupyter Notebook?
Jupyter is a project for developing free, open-source interfaces for working with various different programming languages. A Jupyter notebook is a document interface that allows you to easily combine code and non-code writing.

Jupyter notebook is useful because it can be easier to use Python in a notebook than in a command line, since you can see what you’re doing and edit at the same time.

#### Installing Jupyter Notebook
You can [download the software for Jupyter notebook](https://jupyter.org/install) with two pip install commands:

`pip install jupyterlab`
followed by
`pip install notebook`

#### Using Jupyter Notebook
A great deal of this section draws from [this introduction to Jupyter Notebook](https://colab.research.google.com/github/abrsvn/pyactr-book/blob/master/notebooks/0a_intro_to_jupyter.ipynb).

##### Introduction
You can open Jupyter notebook by going to your command line and typing `jupyter notebook`. That will open the Jupyter notebook interface in your browser.

You can close Jupyter notebook by going to your command line and pressing Ctrl+C. The command line will give you this message: `Shutdown this notebook server (y/[n])?` Type `y` and press **Enter**.

[**Here’s a guide to Jupyter notebook basics**](https://notebooks.gesis.org/binder/jupyter/user/ipython-ipython-in-depth-nra7j86n/notebooks/examples/Notebook/Notebook%20Basics.ipynb)

[**Here's a guide to using the Jupyter notebook interface**](https://problemsolvingwithpython.com/02-Jupyter-Notebooks/02.05-The-Jupyter-Notebook-Interface/)

A Jupyter **computational notebook** is a document-based approach to structuring programming, modeling, data analysis etc. It is a form of [literate programming](https://en.wikipedia.org/wiki/Literate_programming).

A computational notebook is made up of a set of elements called cells that group little bits of information together. There are two main kinds of cells:
- text cells, specifically, Markdown cells; we'll come back to Markdown
- code cells, in our case, Python code cells

The file extension of a notebook document has the .ipynb file extension.
- `.ipynb` for "IPython Notebook", the original version of Jupyter notebooks developed as a particular kind of interface for [IPython](https://en.wikipedia.org/wiki/IPython)

A notebook is a list of cells arranged from the top of the document to the bottom.
- cells can contain several types of information, including code, text, images and so forth.

You develop your project by creating new cells, entering information, reordering cells, and saving the results.

The key element which makes a notebook "computational" is that it can be linked to a computing engine known as a "kernel", which can run on the same computer or another computer using the Internet.
- The kernel is separate from the notebook and can be stopped and started independently from the program displaying the notebook itself
- The magic happens when a code cell is "executed"
    - you can also "execute" a text cell, which just renders the text from Markdown annotation to something easily readable by a human
- When the code from the cell is executed, it is sent to the computational kernel, which runs the sequence of commands contained within the cell
- The results of running the code, e.g., figures, printed messages, etc., are captured and sent back to the notebook from the kernel, where there will be inserted beneath the cell which was just executed

##### The Notebook State and Kernel State are not the same
The notebook is simply a way to organize information and the order of information in a notebook might be different from the order in which code has been executed on the kernel.

For example, you can execute a code cell at the end of the document first, and then go back to the beginning of the document and run a cell there. This happens often when you develop your project.

Thus, the order of the cells in the notebook document is really just for presentation, and it is up to you to "run/execute" the cells in whatever order you want.
- for example, if you delete a cell after running it, it doesn't appear in the notebook anymore but its code has not been "undone" on the kernel
- the kernel doesn't know anything about any edits you make to the notebook interface; all it does is receive code when you send it via the "execute cell" command, runs the code, sends back the outputs, and then it waits

This can mean that the current state of the kernel can be different from what your cells or notebook look like, and the outputs captured in the notebook might be obsolete.

If things get out of control, you can simply restart the kernel, which will erase its current state and set it back to a fresh start. You then need to re-execute all of the cells in your notebook to get back to where you were.

This is like telling your friend how to cook a meal over the phone. You have the instructions in front of you (your notebook) and you tell your friend (the kernel) what to do. If you read the instructions out of order, your friend can't tell the difference. They just know—and follow—the steps in the order in which you communicated them.

If you want to restart the kernal and run the cells in order, you can select **Restart & Run All** from the **Kernel** menu.

![jupyter-restart-and-run-all](https://i.stack.imgur.com/neKoy.png)

##### Writing and running cells
###### Markdown cells
Markdown cells contain prose or comments.

When you first open a notebook, markdown cells are in **command mode**, which basically means they look all pretty and any formatting syntax has been compiled. You can also tell when something is in command mode because the colored bar on the left side is blue.
![jupyter-markdown-command](https://d2l.ai/_images/jupyter01.png)

If you double-click on the markdown cell or press **Enter**, it’ll go into **editing mode** and the colored bar on the left will turn green.
![jupyter-markdown-editing](https://d2l.ai/_images/jupyter02.png)

Markdown cells use markdown syntax for formatting. So for italics, you can use `_single underscores_` or `*single asterisks*`, and for bold you can use `__double underscores__` or `**double asterisks**`.

(Incidentally, this guide is also written in markdown.)

[**Here’s a guide to markdown in Jupyter notebooks**](https://notebooks.gesis.org/binder/jupyter/user/ipython-ipython-in-depth-nra7j86n/notebooks/examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)

[**Here’s a cheatsheet for markdown syntax**](https://www.markdownguide.org/basic-syntax/)

###### Code cells
Code cells can contain any valid Python code in them. When you run the cell, the code is executed and the outputs (if any) are displayed.
- You can execute cells with **Ctrl+Enter**, which will keep the cell selected
- You can also execute cells with **Shift+Enter**, which will select the next cell

Code cells also have **command mode** and **editing mode**, but it’s a lot easier to enter editing mode. Just click the body of the cell once and you’re in.

When you first open a Jupyter notebook from someone else, the code cells may have outputs that were saved as part of the document. But just because you can see those old outputs doesn’t mean that your computer has already run the code cells.

Code cells that haven’t been run yet will have an empty blue bracket next to `In` on the left.

![jupyter-code-1](https://d2l.ai/_images/jupyter05.png)

Once you run a cell, it gets a number in the blue "In" bracket.

![jupyter-code-run](https://problemsolvingwithpython.com/02-Jupyter-Notebooks/images/output_cell.png)

If you want to run all the cells in order automatically, click on "Cell" and then "Run all". You can also choose to run all cells above or below the selected cell.

![jupyter-code-cell](https://i.stack.imgur.com/Lt63H.png)

You can also run all the cells by clicking "Kernel" and then "Restart & Run All"

![jupyter-restart-and-run-all](https://i.stack.imgur.com/neKoy.png)

[**Here’s a guide to running code cells**](https://notebooks.gesis.org/binder/jupyter/user/ipython-ipython-in-depth-nra7j86n/notebooks/examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)

If you have questions about Python itself, there are plenty of tutorials on the internet. [Here’s an official tutorial](https://docs.python.org/3/tutorial/), but in most cases, just googling a bit of code that’s confusing you will turn up answers from lots of people.

#### Data organization template
1. Make sure you have Jupyter notebook
    - If you don’t have it, install it
        1. `pip install jupyterlab`
        2. `pip install notebook`
2. Make sure you have the Python software `pandas`
    - If you don’t have it, install it
        1. `pip install pandas`
3. [Download the data organization template here](https://drive.google.com/file/d/1-MKcAjN-Lg-KKEF_1s1qZgxpln3LM17O/view?usp=sharing)
4. Open Jupyter notebook
    1. Go to command line and enter `jupyter notebook`
    2. In the browser interface, navigate to wherever the downloaded file is and click on it
5. Follow template instructions

### Python Script Method
If you’re not picky about how your organized data looks and you don’t really care how it gets done, you can run a pre-written Python script from the command line and let it do the organizing for you.

1. [Download `organize.py`](https://drive.google.com/file/d/1ha5LIiXVxfymmb3wudKQSf7hqYWmL4-h/view?usp=sharing) and put it somewhere in your files
2. Open your command line
3. Run the script

The structure of the command to run the script looks like this, with optional parts in parentheses (remove the parentheses if you use them):

`python3 path_to_script/organize.py path_to_output_directory_1/processed_data/aggregated_data.csv (path_to_output_directory_2/processed_data/aggregated_data.csv...) (export (path_to_destination_for_organized_data/))`

This command contains, in order:
- the command to use Python, `python3`
- the path from your current location to the Python script `organize.py`
- the path from your current location to the `aggregated_data.csv` file you want to organize
- OPTOINAL: the path from your current location to another `aggregated_data.csv` file you want to append
    - You can add as many `aggregated_data.csv` files as you want
- OPTIONAL: `export`, which will make the script save a .csv file on your computer with the organized data
    - OPTIONAL: the path from your current location to wherever you want the organized data file to go

If you don't want to save a file for the organized data and just want a preview, you can leave out the `export` part of the command. For example, if I do this from my home directory (the default when you open the command line), it looks like this:

```
user@computer:~$ python3 College/phonlab/scripts/organize.py College/phonlab/Tests/brown-fox_output/processed_data/aggregated_data.csv College/phonlab/Tests/test1_output/processed_data/aggregated_data.csv

Organizing 2 data files...

         file sound     f0  duration  ... f3_mean  f4_mean  length_f4  length_mean
0   brown-fox  0001  239.4     0.100  ...  2727.0   4042.0      15.15        16.64
1   brown-fox  0002  312.0     0.070  ...  2907.0   4316.0      14.19        13.76
2   brown-fox  0003  244.9     0.140  ...  2653.0   3614.0      16.95        15.04
3   brown-fox  0004  217.6     0.168  ...  2913.0   4224.0      14.50        15.57
4   brown-fox  0005  223.6     0.060  ...  2648.0   3645.0      16.80        15.80
5   brown-fox  0006  231.0     0.090  ...  2650.0   3920.0      15.62        17.17
6   brown-fox  0007  233.4     0.048  ...  2917.0   4378.0      13.99        15.31
7   brown-fox  0008  222.6     0.060  ...  3279.0   4330.0      14.15        16.62
8   brown-fox  0009  220.0     0.138  ...  3048.0   4392.0      13.95        14.35
9   brown-fox  0010  227.5     0.140  ...  3033.0   4444.0      13.78        14.63
10  brown-fox  0011  292.8     0.230  ...  3045.0   4260.0      14.38        15.84
11    red-fox  0001  290.9     0.080  ...  2958.0   4402.0      13.91        13.79
12    red-fox  0002  246.3     0.120  ...  3006.0   4398.0      13.93        13.09
13    red-fox  0003  179.0     0.180  ...  3034.0   4206.0      14.56        15.49
14    red-fox  0004  232.0     0.038  ...  2730.0   3678.0      16.65        16.40
15    red-fox  0005  246.8     0.190  ...  2711.0   3843.0      15.94        17.54
16    red-fox  0006  240.9     0.160  ...  2366.0   4121.0      14.86        16.34
17    red-fox  0007  234.5     0.038  ...  3195.0   4237.0      14.46        17.20
18    red-fox  0008  236.2     0.120  ...  3065.0   4403.0      13.91        14.32
19    red-fox  0009  247.0     0.068  ...  3090.0   4446.0      13.78        15.04
20    red-fox  0010  217.8     0.120  ...  2603.0   3613.0      16.95        15.22
21    red-fox  0011  100.6     0.198  ...  2867.0   3926.0      15.60        16.41

[22 rows x 31 columns]

Finished!
Organized data was not saved. To save and export data, repeat command (up-arrow key) and add 'export'.
```

If I actually do want to save a copy of the organized data, I add `export`.

```
user@computer:~$ python3 College/phonlab/scripts/organize.py College/phonlab/Tests/brown-fox_output/processed_data/aggregated_data.csv College/phonlab/Tests/test1_output/processed_data/aggregated_data.csv export

Organizing 2 data files...

         file sound     f0  duration  ... f3_mean  f4_mean  length_f4  length_mean
0   brown-fox  0001  239.4     0.100  ...  2727.0   4042.0      15.15        16.64
1   brown-fox  0002  312.0     0.070  ...  2907.0   4316.0      14.19        13.76
2   brown-fox  0003  244.9     0.140  ...  2653.0   3614.0      16.95        15.04
3   brown-fox  0004  217.6     0.168  ...  2913.0   4224.0      14.50        15.57
4   brown-fox  0005  223.6     0.060  ...  2648.0   3645.0      16.80        15.80
5   brown-fox  0006  231.0     0.090  ...  2650.0   3920.0      15.62        17.17
6   brown-fox  0007  233.4     0.048  ...  2917.0   4378.0      13.99        15.31
7   brown-fox  0008  222.6     0.060  ...  3279.0   4330.0      14.15        16.62
8   brown-fox  0009  220.0     0.138  ...  3048.0   4392.0      13.95        14.35
9   brown-fox  0010  227.5     0.140  ...  3033.0   4444.0      13.78        14.63
10  brown-fox  0011  292.8     0.230  ...  3045.0   4260.0      14.38        15.84
11    red-fox  0001  290.9     0.080  ...  2958.0   4402.0      13.91        13.79
12    red-fox  0002  246.3     0.120  ...  3006.0   4398.0      13.93        13.09
13    red-fox  0003  179.0     0.180  ...  3034.0   4206.0      14.56        15.49
14    red-fox  0004  232.0     0.038  ...  2730.0   3678.0      16.65        16.40
15    red-fox  0005  246.8     0.190  ...  2711.0   3843.0      15.94        17.54
16    red-fox  0006  240.9     0.160  ...  2366.0   4121.0      14.86        16.34
17    red-fox  0007  234.5     0.038  ...  3195.0   4237.0      14.46        17.20
18    red-fox  0008  236.2     0.120  ...  3065.0   4403.0      13.91        14.32
19    red-fox  0009  247.0     0.068  ...  3090.0   4446.0      13.78        15.04
20    red-fox  0010  217.8     0.120  ...  2603.0   3613.0      16.95        15.22
21    red-fox  0011  100.6     0.198  ...  2867.0   3926.0      15.60        16.41

[22 rows x 31 columns]

Finished!
File 'organized_data.csv' has been created in current directory.
```

Now I have a file called `organized_data.csv` in my home directory. But I'd rather have that file closer to the aggregated data files that it came from. So I can add a destination for that new file.

```user@computer:~/$ python3 College/phonlab/scripts/organize.py College/phonlab/Tests/brown-fox_output/processed_data/aggregated_data.csv College/phonlab/Tests/test1_output/processed_data/aggregated_data.csv export College/phonlab/Tests/

Organizing 2 data files...

         file sound     f0  duration  ... f3_mean  f4_mean  length_f4  length_mean
0   brown-fox  0001  239.4     0.100  ...  2727.0   4042.0      15.15        16.64
1   brown-fox  0002  312.0     0.070  ...  2907.0   4316.0      14.19        13.76
2   brown-fox  0003  244.9     0.140  ...  2653.0   3614.0      16.95        15.04
3   brown-fox  0004  217.6     0.168  ...  2913.0   4224.0      14.50        15.57
4   brown-fox  0005  223.6     0.060  ...  2648.0   3645.0      16.80        15.80
5   brown-fox  0006  231.0     0.090  ...  2650.0   3920.0      15.62        17.17
6   brown-fox  0007  233.4     0.048  ...  2917.0   4378.0      13.99        15.31
7   brown-fox  0008  222.6     0.060  ...  3279.0   4330.0      14.15        16.62
8   brown-fox  0009  220.0     0.138  ...  3048.0   4392.0      13.95        14.35
9   brown-fox  0010  227.5     0.140  ...  3033.0   4444.0      13.78        14.63
10  brown-fox  0011  292.8     0.230  ...  3045.0   4260.0      14.38        15.84
11    red-fox  0001  290.9     0.080  ...  2958.0   4402.0      13.91        13.79
12    red-fox  0002  246.3     0.120  ...  3006.0   4398.0      13.93        13.09
13    red-fox  0003  179.0     0.180  ...  3034.0   4206.0      14.56        15.49
14    red-fox  0004  232.0     0.038  ...  2730.0   3678.0      16.65        16.40
15    red-fox  0005  246.8     0.190  ...  2711.0   3843.0      15.94        17.54
16    red-fox  0006  240.9     0.160  ...  2366.0   4121.0      14.86        16.34
17    red-fox  0007  234.5     0.038  ...  3195.0   4237.0      14.46        17.20
18    red-fox  0008  236.2     0.120  ...  3065.0   4403.0      13.91        14.32
19    red-fox  0009  247.0     0.068  ...  3090.0   4446.0      13.78        15.04
20    red-fox  0010  217.8     0.120  ...  2603.0   3613.0      16.95        15.22
21    red-fox  0011  100.6     0.198  ...  2867.0   3926.0      15.60        16.41

[22 rows x 31 columns]

Finished!
File 'organized_data.csv' has been created in Tests/
```

If I wanted the paths I have to write to be shorter, I could change directories in the command line to the folder called `phonlab` that contains both `scripts` and `Tests`. Then the previous command could look like this:

`python3 scripts/organize.py Tests/brown-fox_output/processed_data/aggregated_data.csv Tests/test1_output/processed_data/aggregated_data.csv export Tests/`

As you can see, using this Python script doesn't really need any knowledge of Python. A basic understanding of the command line is all you need.

**WARNING**
\
This script won't work well if the 'file' column of your `aggregated_data.csv`, which has the format `[file name]_[sound number]`, has more than one underscore. In other words, it won't work if there's an underscore in the `.wav` and `.TextGrid` files passed through FastTrack.

## Plotting the Data
Now that we have the data we need, we can plot the results so that it’s easier to see what kinds of voices and vowel spaces we have in the data. To do this, we'll be using R and ggplot2.

If you already know how to use R and ggplot2, skip to [Plotting Voices](#plotting-voices) or [Plotting Vowels](#plotting-vowels).

If you already know how to use R but don't know how to use ggplot2, skip to [Installing ggplot2](#installing-ggplot2).

### R (programming language)
The most commonly used method for plotting in linguistics is R, a free software for statistical computing and graphics. Specifically, we want an R package called **ggplot2**.

#### Installing R
[Comprehensive R Archive Network (CRAN)](https://cran.r-project.org/mirrors.html)

[(Tutorial) How to Install R on Windows, Mac OS, and Ubuntu](https://www.datacamp.com/community/tutorials/installing-R-windows-mac-ubuntu)

##### Mac
If you’re on a Mac, you can download R with the links and instructions [here](https://cran.r-project.org/bin/macosx/), or you can check out the tutorial link in the section above.

Alternatively, you could download R from Homebrew, if you have it.

##### Windows
If you’re on Windows, you can download R with the links and instructions [here](https://cran.r-project.org/bin/windows/base/), or you can check out the tutorial link two sections above.

##### Linux
If you’re on Linux, you can download R from the command line with the following command:
`sudo apt-get install r-base`

#### Installing ggplot2
To plot with R, we’ll need a package called [ggplot2](https://ggplot2.tidyverse.org/).

Similar to Python, R comes with its own package manager. So once you have R, you can install R packages like ggplot2 directly from the R console.

You can either use the `command install.packages("ggplot2")` or `install.packages("tidyverse")` ([instructions and details here](https://ggplot2.tidyverse.org/))

#### Using R and ggplot2
R is a programming language, somewhat similar to Python. ggplot2 provides some plotting-specific tools and formulas that you can put together to create an image.

##### The Syntax of R
[**R Tutorial For Beginners**](https://www.statmethods.net/r-tutorial/index.html)

##### Opening R
There are two main ways to open and use R.

###### Command Line
You can open R in your command line with the command `R` (make sure it’s uppercase!).

```
user@computer:~$ R

R version 3.6.3 (2020-02-29) -- "Holding the Windsock"
Copyright (C) 2020 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

>
```

This doesn’t require any new installations, but some people may find the command line format hard to work with. If you’re using the command line, it’s helpful to write up your R code in a text file before and and then just copy and paste it into the command line.

###### RStudio
The other way is using [RStudio](https://www.rstudio.com/), which provides an easier interface to work with that gives you a text editor and puts the code side-by-side with the image it produces.

![rstudio](http://www.sthda.com/sthda/RDoc/images/rstudio.png)

[**Instructions for installing and setting up RStudio**](https://www.earthdatascience.org/courses/earth-analytics/document-your-science/setup-r-rstudio/)

##### The Syntax of ggplot2
[**An introduction to ggplot**](http://kweatherholtz.github.io/blog/intro-to-ggplot/) (slideshow [here](http://kweatherholtz.github.io/tutorials/ggplot/ggplot_ling_tutorial.html))

To make a plot, ggplot needs at least three things:
1. A **dataframe** (you can use a .csv file for this)
2. A set of **aesthetic mappings**
    - These describe how variables in a data frame are mapped to graphical attributes.
    - E.g. x- and y-axis variables, colo(u)rs, subset groupings, linetypes
3. One or more **geometric objects**, called **geoms**
These determine how values are rendered graphically.
E.g. points, lines, boxplots, bars, etc.

Here’s an example of what ggplot code looks like:
ggplot(dataframe, aes(x = xvar, y = yvar)) + geom_boxplot()

There’s more tools you can use in ggplot2, but for now, just get a feel for the structure of ggplot code.

#### Alternative plotting methods
You can also make plots in Python with [matplotlib](https://matplotlib.org/stable/index.html) ([installation instructions here](https://matplotlib.org/stable/users/installing.html)).

Many spreadsheet softwares allow plotting too, but in my experience the plots are limited, for example there’s no option to reverse the axes (or else it's just really hard to find that option).

We won’t talk about these plotting methods here, but they’re options to explore if you’re interested.

### Plotting Voices
Here’s where you’ll need that vocal tract length information that you found.

As discussed earlier, vocal tract length tends to be correlated with gender. But pitch also tends to be correlated with gender.
- Men tend to have longer and thicker vocal folds, which leads to slower vocal fold vibration, i.e. a lower fundamental frequency or pitch
- Women tend to have shorter vocal tracts and shorter and thinner vocal folds, which leads to faster vocal fold vibration, i.e. a higher fundamental frequency or pitch

So by plotting both average vocal tract length and average fundamental frequency, we can get a fairly good picture of gender distribution in a set of voices.

For example, the plots below shows the voices of five California English speakers of varying ages and genders.

![voices-1](https://lh3.googleusercontent.com/pw/AM-JKLXHy2iNkJQ6Ndc5mxkTg80rLR5-AIS7CT0UTszci50212XnzI6EGYC5Avia62qSLkFK2gIAM6hvoOMxZ6Az81LfgDEXzMsRSdJiQKIFfbSZ1JBjSk7grFCd-fxpMr14zDNQWCrpZBvQlniJaPyrCRPb=w469-h406-no?authuser=0)
![voices-2](https://lh3.googleusercontent.com/pw/AM-JKLXvgzsP62R0iah2NKzJlsBzNuQshEa0ecsyTRr1W7BZUHiwqmVIc2ULInjsunYYOpJaJq4Tqw8VezeI4YaWEpZ_ryvXgWFEwVEFNiKdd5ge66Ob07pSTkdOGkXKisAHo6zYkbTZbnUgeunzgzYWDTo8=w471-h404-no?authuser=0)

In both plots, F0 is on the y-axis. In the left image, the x-axis is the average length of F4; in the right image, the x-axis is the average length of F1-F4.

Although there are some differences between the graphs, notice that in both cases, the three female voices are in the upper lefthand corner, while the two male voices are in the lower righthand corner.

#### R Code
First, open R and copy and paste the following two commands.

library(ggplot2)
library(dplyr)

The first library lets you use ggplot commands. The second library lets you use the [pipe function `%>%`](https://www.datacamp.com/community/tutorials/pipe-r-tutorial) and the [`summarise`](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8/topics/summarise) function.

Next, import your data into R.

`data <- read.delim('/path_from_home_to_file_location/organized_data.csv', header = TRUE, sep = ",", dec = ".")`

Now you need to get the averages of F0, length_f4, and length_mean for each speaker.

```
means <- data %>%
    group_by({file/subject/speaker}) %>%
    summarise(mean_f0 = mean(f0),
              mean_length_f4 = mean(length_f4),
              mean_length_mean = mean(length_mean))
```

Make sure to replace the text in the curly brackets with the name of the column that has your different speakers, whatever that column is called in your data.

Now you can plot the values in means. Depending on what kind of plot you want, you can use different geoms and aesthetics.

To get plots like the examples earlier, use `geom_text()` and `theme_bw()`.

`ggplot(means, aes(x = mean_length_f4, y = mean_f0)) + geom_text(label = means$subject) + ggtitle("Voice Plot") + xlab("Mean Vocal Tract Length of F4 (cm)") + ylab("Mean F0 (Hz)") + theme_bw()`

`ggplot(means, aes(x = mean_length_mean, y = mean_f0)) + geom_text(label = means$subject) + ggtitle("Voice Plot") + xlab("Mean Vocal Tract Length (cm)") + ylab("Mean F0 (Hz)") + theme_bw()`

Alternatively, if you use `geom_label()` and `theme_classic()`, you get plots like below.

![voices-3](https://lh3.googleusercontent.com/pw/AM-JKLVxbJmO7DY3xOLc6BWbK30Pe7RyLuUfh06L-y9fyS3qoamJ_tbPSaGrf2oHrTr4IqPGZKTKu9aSkkRw41AnlFAd0j2YEHZFRUcXW_aUq2P_G-Pg_m73Oi4i7lideIXsIRFNiIkpPXvydHm2JQ0AnyNd=w483-h406-no?authuser=0)
![voices-4](https://lh3.googleusercontent.com/pw/AM-JKLXeY-2cXjfvyAMb2D_0aFNVD6E-o17X9-8PxnLgVF_YFnmaKqQVBdZ-I0WIJLV3ReLgvN24vWzehEHfg_IKCpEsiB8AUaYCQFPa-kre_MovE-acoRS7GdO7UVX0bTX8LNSBZ5-UnsYLHOSBHKQLSUFg=w483-h404-no?authuser=0)

The code for these plots is here:

`ggplot(means, aes(x = mean_length_f4, y = mean_f0, label = subject)) + geom_label() + ggtitle("Voice Plot") + xlab("Mean Vocal Tract Length of F4 (cm)") + ylab("Mean F0 (Hz)") + theme_classic()`

`ggplot(means, aes(x = mean_length_mean, y = mean_f0, label = subject)) + geom_label() + ggtitle("Voice Plot") + xlab("Mean Vocal Tract Length (cm)") + ylab("Mean F0 (Hz)") + theme_classic()`

As you get more comfortable with R and ggplot2, you can experiment with other styles of plotting voices.

### Plotting Vowels
F1 is inversely related to vowel height (i.e. the lower the F1, the higher the vowel) and F2 is directly related to vowel frontness (i.e. the higher the F2, the fronter the vowel). When plotting vowels, we want to emulate the physical vowel space the same way that the IPA vowel chat and similar vowel charts mirror the space within the oral cavity.

![vowel-space-1](http://english.mimicmethod.com/uploads/6/6/2/8/6628443/8354785_orig.png)
![vowel-space-2](https://upload.wikimedia.org/wikipedia/commons/5/50/Ipa-chart-vowels.png)

To make this kind of vowel space, we plot F1 on a reverse y-axis and F2 on a reverse x-axis.

![vowel-space-3](https://www.researchgate.net/profile/Fabienne-Westerberg/publication/312165145/figure/fig30/AS:668529531568143@1536401269413/How-F1-and-F2-values-correspond-to-height-and-advancement-on-the-vowel-quadrilateral.png)

But that’s just the basic structure of the plot space. When it comes to actually putting the values on the plot, there are lots of different ways to do it.

#### Before plotting
Make sure you import the following two libraries:

```
library(ggplot2)
library(dplyr)
```

Now import your data.

`data <- read.delim('/path_from_home_to_file_location/organized_data.csv', header = TRUE, sep = ",", dec = ".")`

Another important piece to set up is arranging so that the colors of adjacent vowels aren’t too similar.

```
data$label <- factor(data$label,
                     levels = c("IY", "EH", "AW", "AO", "UH", "IH", "AE", "AH",
                                "OY", "UW", "EY", "AY", "AA", "OW", "ER"))
```

If you don’t have all of these vowel, you might have to make some changes to the code above.

#### Cloud Plot
A pretty typical vowel plot is just to plot every vowel. This will give you "clouds" of different vowels in different areas.

![vowel-plot-1](https://joeystanley.com/images/plots/vowel_plots_1/plot10.png)


```
ggplot(data, aes(x = f2_mean, y = f1_mean, color = label)) +
    geom_point() +
    scale_x_reverse() + scale_y_reverse() +
    scale_color_discrete(breaks = c("IY", "IH", "EY", "EH", "AE", "AY", "AW", "AH",
                                    "AA", "AO", "OY", "OW", "UH", "UW", "ER")) +
    ggtitle("Vowel Plot") + xlab("F2 (Hz)") + ylab("F1 (Hz)") + labs(color = "Vowel") +
    theme_classic()
```

A downside to this kind of plot is that it can be hard to read, because vowels are messy. This kind of plot gets especially hard to read when you have multiple speakers in the data.

#### Average Vowel Plot
To reduce the amount of visual information we have to try to understand, we can instead calculate and plot vowel averages.

First we have to find the means.

```
means <- data %>%
    group_by(label) %>%
    summarise(F1 = mean(f1_mean),
              F2 = mean(f2_mean))
```

Then we make the plot.

![vowel-plot-2](https://joeystanley.com/images/plots/vowel_plots_1/plot13.png)

```
ggplot(means, aes(x = F2, y = F1, label = label)) +
    geom_label() +
    scale_x_reverse() + scale_y_reverse() +
    ggtitle("Vowel Plot") + xlab("F2 (Hz)") + ylab("F1 (Hz)") +
    theme_classic()
```

This is easier to read, but it’s missing the overlappedness of the vowels that we saw in the cloud plot. So we might want to combine the two.

![vowel-plot-3](https://joeystanley.com/images/plots/vowel_plots_1/plot15.png)

```
ggplot(data, aes(x = f2_mean, y = f1_mean, color = label, label = label)) +
    geom_point() +
    geom_label(data = means, aes(x = F2, y = F1)) +
    scale_x_reverse() + scale_y_reverse() +
    scale_color_discrete(breaks = c("IY", "IH", "EY", "EH", "AE", "AY", "AW", "AH",
                                    "AA", "AO", "OY", "OW", "UH", "UW", "ER")) +
    guides(color = "none") +
    ggtitle("Vowel Plot") + xlab("F2 (Hz)") + ylab("F1 (Hz)") +
    theme_classic()
```

Having both the averages and the vowel clouds is a bit better, but back to being kinda hard to read.

#### Ellipses Plots
A different way of capturing the range of vowels along with their averages is with an ellipses plot. You can set up ellipses to show standard deviations from the means.

Here’s a plot with ellipses showing 1 standard deviation from the mean.

![vowel-plot-4](https://joeystanley.com/images/plots/vowel_plots_1/plot29.png)

```
ggplot(data, aes(x = f2_mean, y = f1_mean, color = label, label = label)) +
    stat_ellipse(level = 0.67, geom = "polygon", alpha = 0.1, aes(fill = label)) +
    geom_label(data = means, aes(x = F2, y = F1)) +
    scale_x_reverse() + scale_y_reverse() +
    scale_color_discrete(breaks = c("IY", "IH", "EY", "EH", "AE", "AY", "AW", "AH",
                                    "AA", "AO", "OY", "OW", "UH", "UW", "ER")) +
    ggtitle("Vowel Plot") + xlab("F2 (Hz)") + ylab("F1 (Hz)") +
    theme_classic() +
    theme(legend.position="none")
```

But if you want a 95% confidence interval, which corresponsd to about 2 standard deviations from the mean, use this code:

```
ggplot(data, aes(x = f2_mean, y = f1_mean, color = label, label = label)) +
    stat_ellipse(geom = "polygon", alpha = 0.1, aes(fill = label)) +
    geom_label(data = means, aes(x = F2, y = F1)) +
    scale_x_reverse() + scale_y_reverse() +
    scale_color_discrete(breaks = c("IY", "IH", "EY", "EH", "AE", "AY", "AW", "AH",
                                    "AA", "AO", "OY", "OW", "UH", "UW", "ER")) +
    ggtitle("Vowel Plot") + xlab("F2 (Hz)") + ylab("F1 (Hz)") +
    theme_classic() +
    theme(legend.position="none")
```

##### Plots Source
The vowel plots so far come from [**Making vowels in R (Part 1)**](https://joeystanley.com/blog/making-vowel-plots-in-r-part-1), and the code so far was adapted from this tutorial to work for our organized data. This tutorial gives a deeper explanation of the bits and pieces that make up the plots.

#### Contour Plot
Ellipses plots are a step in the right direction, especially with the transparent color fill. But [this linguist](http://christiandicanio.blogspot.com/2013/10/visualizing-vowel-spaces-in-r-from.html) argues that a better way of capturing vowel range is with **contour plots**, or 2D density plots.

![vowel-plot-contour](http://4.bp.blogspot.com/-0js143QvDCg/UmWh8QPXzZI/AAAAAAAAAKM/xq0xp_iObR0/s1600/plot_ggplot2_contour.jpg)

Contour plots offer a bit more nuance by showing where vowels are concentrated, and if there are more than one areas of concentration.

Unfortunately, a downside I’ve found to contour plots is that when you have a lot of vowels like in English, things get very hard to read very quickly.

![vowels-t104](https://lh3.googleusercontent.com/pw/AM-JKLU-50xQ1wHgKay1nFp-4kSjKTgkuUht7fqKZu32QT4CgWohv5Zks3yGA-azZThNSF_UVvJKpQ2Dbj4m0iZ2psqyHlxCAdzFhF-MdzPMcvSA_ctvrqaS-67eDN-Wq3t68ygkMv03NPpuWTO1o6kHklAy=w1771-h902-no?authuser=0)

So far I haven't been able to figure out how to clean up contour plots so they're more readable like the ellipses plots.

In addition, contour plots sometimes seem to just ignore some of your vowels, for no reason that I've been able to find.

![vowels-t102](https://lh3.googleusercontent.com/pw/AM-JKLWGX5WLgq6gQZSFP-Ve4JfTvAeGS-10gpfs3-_iNy5qcdW_weJiEnqdGLPgeJ-r0UJc8_al2eKxmwZSVQmGuNJlZGhig2YamWxyBMgrFf6jzvf4My3ZtAm_xCC2XkEYfZPGquhUdIO1VTJDPehOtVEZ=w1766-h902-no?authuser=0)
![vowels-t101](https://lh3.googleusercontent.com/pw/AM-JKLX3NoiXc_QJ9174Sy2Fbm1xNXev1QVur0WN2IsAzlxcOFQRg-bCnNp1SItZoikErT_cdL53oUfyazQfTiwAzMnG4SIwXigFq6mu7oDZRAPOVvuw31aeC-MO31AgyWRj0lcBcKv9dxKNknFUTorzn7fD=w1773-h902-no?authuser=0)

The current code for plots like these is here:

`ggplot(data, aes(x = f2_mean, y = f1_mean)) + geom_density_2d(aes(color = label)) + scale_y_reverse() + scale_x_reverse()`

## ???
