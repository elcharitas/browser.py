# Simple Browser Project

This readme is generated to describe this project only.

Its purpose is also to serve as a manual for using the browser.

## Basic information

As per the client's requirements, this software has the following features

- Built with python 3
- Contains an executable
- can be run via command prompt
- takes only one optional argument - the URL
- maintains a minimal UI
- identifies multiple monitors
- displays on full screen

## Usage

To use this app, simply copy the executable found in the `dist` directory to where you would want to use it.

After copying, run the following command

```sh
$ ./browser [url]
```

[url] can be any string which contains the URL to go to.

To build a new version of the browser, simply run this command

```sh
$ pyinstaller -w -F -i "./icon.ico" --name browser main.py
```
