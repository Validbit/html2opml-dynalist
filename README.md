# Chrome HTML to OPML \[dynalist\] convertor script
When you want to move your bookmarks into dynalist (if you don't use chrome, just import them into chrome/chromium through settings)

## Prerequisites
### Dependencies
- python
https://www.python.org/downloads/
- script libraries
```pip install beautifulsoup4 lxml```

>Note: lxml was used since it provided better performance (and possibly cross-compatibility)

# Usage
# Preparation
For successful conversion you have to prepare two variables, i.e. **all following** 
> tl;dr: stip chrome HTML headers/footers and take a header from your dynalist backup (any will do))

## Bookmarks data
This script works by using the bookmarks data itself. Thus it doesn't need the xml around it.
- remove header
At the time of writing in my environment it looks like this:
```
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
```
**<DL><p>** is already the bookmarks data so **don't delete it** unless you know/see what you have to do not to break it.

## Dynalist header
>Note: You may as well replace the information (FirstName, you@example (email)) manually but I don't have feedback if it's okay if non-registered user info was used.

-  look how it's here by default and make yours inline as well (one line, prefferably without larger spaces)
In [notepad++](https://notepad-plus-plus.org/downloads/) (which can do it easily) you
```
- CTRL+J (Join lines)
- CTRL+F > Replace > (tick) Regex > ("search for") **\s{2,}** > ("replace with" nothing) >
```
- (if you just copied) ensure tags are there (what you paste from your source dynalist file should end with **<body>**)

## Running
All that's needed is to run the script with **py** or **python3**
```python html2opml_dyna.py```
It will generate `output_dyna.opml` that you choose **when creating a new file in dynalist**

add part gh readme

# Troubleshooting
If an problem arises, **create a new issue**
The script is ready for use (and should be compatible with most previous versions of chrome)

## Empty file (or missing content/bookmarks)
If the file is created but the content (converted bookmarks) are missing, the copied **HTML** (chrome bookmarks backup) was likely **not cleaned enough**/logically (and is causing the problem) use linter (or VS Code with related extensions if you can't figure out where is the problem)
