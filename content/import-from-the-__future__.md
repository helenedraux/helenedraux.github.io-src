Title: import from the __future__
Date: 2016-09-01 20:42
Category: coding
Tags: python
Slug: import-from-the-__future__
Summary: In python 2.7, 1/2 = 0. Here is how to avoid it.
Status: 
Image: /images/fromfutureimportdivision.png

Python 2.7 still struggles with divisions of integers, which means that 1/2 returns 0 instead of 0.5. To avoid that, just use:

```
from __future__ import division
```
