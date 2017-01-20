Title: Tips using Jupyter to publish on a blog
Date: 2017-01-19 7:53
Category: coding
Tags: jupyter, notebook, python, css
Slug: tips-using-jupyter-to-publish-on-a-blog
Summary: A short list of things I learned while making this blog: improving the display of notebook with some CSS hack, a markdown trick and some bokeh suggestions. 
Status: 
Image: /images/jupyter-main-logo.svg


Jupyter Notebook are very easy to integrate in pelican. I modified it a bit so it's easier to read. I already blogged about the button 'Reveal Code', which creates a button for each code cell, and hides all the code cells. Here is a list of the other small modifications I made.

## Hide the empty input cells

Jupyter Notebooks are made of two columns: one for the input number (In [X]) and the code/text column. When seeing the Notebook on a blog, it's not so relevant. On my configuration, it was still showing, so I added: 

	:::css

	div.input_prompt{
	  display: none;
	}
	div.prompt:empty{
	  display: none;
	}

## Improve the print function

Markdown cannot be used in the print function. I found someone suggesting the following function to put at the start of your Notebook. Neat!

	:::python

	from IPython.display import Markdown, display
	def printmd(string):
	    display(Markdown(string))


## Using Bokeh

### Show the plots in the Notebook

Bokeh is sooo much better than matplotlib, especially if you use pandas. To use it in the notebook, you should use the `output_notebook()` function. So add at the start of your Notebook:

	:::python
	# To plot bars and scatter plot
	from bokeh.charts import Bar, Scatter, output_file, show
	# To plot in the notebook
	from bokeh.io import output_notebook, push_notebook
	# To use the option "sort = False" in the labels: CatAttr(columns=['word'], sort=False)
	from bokeh.charts.attributes import CatAttr
	# To plot simple figures
	from bokeh.plotting import figure, output_file, show, ColumnDataSource
	# To get the hover function
	from bokeh.models import HoverTool
	# To have subplots
	from bokeh.layouts import gridplot
	# To modify the scale used in a plot (interesting for sublots). Use: plot.y_range = Range1d(min,max)
	from bokeh.models.ranges import Range1d
	# To get the plots in the notebook
	output_notebook()

### Hide "Bokeh Notebook handle for In[]"

The Bokeh plots are not shown in the result cell, instead it shows: 

`<Bokeh Notebook handle for In[n]>` 

which is not only ugly/useless, but also doesn't render properly in pelican. To remove it, and since it's the only thing that appears in the result cell, [someone suggested](https://github.com/bokeh/bokeh/issues/4697) to add a semicolon after the `show()` function: 

`show(bar,notebook_handle=True);`.

It's also possible to hide the logo, but although I find it a bit childish with all these colors, I think it's good to show where the graphs come from. Besides, it also indicates when the library has been loaded, which is user friendly for people with slow connections.

## Et voilà!

It's easy to make your Jupyter Notebook easy to navigate, so go on and do some storytelling with data!




