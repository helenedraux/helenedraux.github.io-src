Title: Tkinter in Mac
Date: 2016-09-01 20:42
Category: coding
Tags: python, matplotlib, udacity
Slug: tkinter-in-mac
Summary: Issue with matplotlib library
Status: 
Image: /images/TclError.png

I ran into issues with some python files from Udacity course in Machine Learning. The file uses the Tk library, which gives an error 'TclError'. I followed some [online advice](http://stackoverflow.com/questions/34405087/why-is-pyplot-giving-me-a-tclerror-on-osx):

> I found that I have installed the tk both in anacode and system. But I donot know the reason in callback in Tk. So what I did is change the backend of matplotlib.

> cd ~/.matplotlib

> vi matplotlibrc

> then change
>
> backend : TkAgg
> to
>
> backend : Qt4Agg
> And it worked for me !

Worked for me too!