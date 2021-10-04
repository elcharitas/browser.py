# Simple Browser Project

This readme is generated to describe this project only.

Its purpose is also to serve as a manual for using the browser executable only.

## Basic information

As per the client's requirements, this software has the following features

- Built with python 3 using PyQt5 module
- Contains an executable
- can be run via command prompt
- takes two optional argument - the URL and Screen Number
- maintains a minimal UI
- identifies multiple monitors/screens
- displays on full screen

## Browser Setup

In order to properly setup this software and get it working, you'll need some modules installed.

Don't fret, simply run the command below via the terminal to install the modules.

```sh
$ pip install -r requirements.txt
```

## Basic Usage

To use this software, simply copy the executable found in the `dist` directory to where you would want to use it.

After copying, run the following command

```sh
$ ./browser [url]
```

[url] can be any string which contains the URL to go to.

To build a new version of the browser, simply run this command

```sh
$ pyinstaller -w -F -i "./icon.ico" browser.py
```

The above command will create three things:
- browser.spec
- build directory
- dist directory

You need not worry about these files created. Simply get the newly compiled browser from dist and copy to wherever you want.
