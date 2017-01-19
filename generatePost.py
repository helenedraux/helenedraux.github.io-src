import sys
from datetime import datetime

TEMPLATE = """
Title: {title}
Date: {year}-{month:02d}-{day:02d} {hour}:{minute:02d}
Category: 
Tags: 
Slug: {slug}
Summary: 
Status: draft
Image: /images/

"""
def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}.md".format(slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)

if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print('Need a "Title"')