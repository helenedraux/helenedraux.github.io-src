Title: "Reveal Code" button on Jupyter
Date: 2017-01-17 6:30
Category: Website Hack
Tags: pelican, jupyter, javascript
Slug: reveal-code-on-jupyter-notebook
Summary: I wrote a short script to add a button which hides and show the code cells
Status:
Image: /images/revealcode.png

Jupyter notebook still doesn't have the capability of hiding cells when you publish your notebooks online. I think there is a plugin that can do it, but didn't want to install yet another plugin that I wouldn't be able to maintain easily. Besides I'm comfortable enough with javascript to write my own code.

# Process

To create a script that would hide and show the elements of code, I first published a notebook on my server and looked at how the notebook was rendered. For instance, below are two cells: the first is a markdown, the second is a code cell. In pure Javascript, to hide/show an element, the usual path is to change the display style of the element: taking the value either `none` or `block`.

```
<div class="cell border-box-sizing text_cell rendered">
  <div class="prompt input_prompt">
  </div>
  <div class="inner_cell">
    <div class="text_cell_render border-box-sizing rendered_html">
      <p>This is a text cell</p>
    </div>
  </div>
</div>
<div class="cell border-box-sizing code_cell rendered">
  <div class="input">
    <div class="prompt input_prompt">In [1]:</div>
    <div class="inner_cell">
      <div class="input_area">
        <div class=" highlight hl-ipython2">
        	This is a code cell
        </div>
      </div>
    </div>
  </div>
</div>

```

I noticed that there was only one class different between both div: `text_cell` or `code_cell`. Well named I guess! My idea was then to write a javascript function which adds a `button` before `code_cell` and hides/shows the `code_cell`. Once I've added a button, the HTML code would become like this:

```
<div class="cell border-box-sizing text_cell rendered">
  <div class="prompt input_prompt">
  </div>
  <div class="inner_cell">
    <div class="text_cell_render border-box-sizing rendered_html">
      <p>This is a text cell</p>
    </div>
  </div>
</div>

<button>Hide/Show</button>

<div class="cell border-box-sizing code_cell rendered">
  <div class="input">
    <div class="prompt input_prompt">In [1]:</div>
    <div class="inner_cell">
      <div class="input_area">
        <div class=" highlight hl-ipython2">
        	This is a code cell
        </div>
      </div>
    </div>
  </div>
</div>

```

The code that I want to add is therefore the `nextElementSibling`. However, if the `style: display` of the code_cell is changed, it will not render well when showing again. Therefore I decided to modify the display style of the children of `code_cell` instead. 

# Code

## Custom.js

I started by creating a `custom.js` file in the folder `theme/(nameofmytheme)/static/js` since there wasn't any before. 

In the file, I wrote the code below. Note that I use bootstrap, and therefore I use their button style.

	:::JavaScript
	var code_shown = false;
	document.addEventListener("DOMContentLoaded",function(){
	  var cellstohide_wrapper = document.getElementsByClassName('cell border-box-sizing code_cell rendered');
	  console.log(cellstohide_wrapper);
	  var nbcell_wrapper= cellstohide_wrapper.length;
	  for (var i=0;i<nbcell_wrapper;i++){
	      cellstohide_wrapper[i].insertAdjacentHTML('beforebegin', '<button class="btn btn-danger btn-sm" id="toggleCodeBtn_'+ i +'" value="Show Code" onclick="code_toggle(event)">Reveal code</button>');
	        for (var k = 0; k < cellstohide_wrapper[i].childNodes.length; k++) {
	                elementToReturn = cellstohide_wrapper[i].childNodes[k];
	                if (elementToReturn.className == 'input') {
	                    for (var j=0; j < elementToReturn.childNodes.length; j++) {
	                      childtohide = elementToReturn.childNodes[j];
	                      if (childtohide.className == 'prompt input_prompt' || 
	                                  childtohide.className == 'inner_cell') {
	                            childtohide.style.display = 'none';
	                      }
	                    }
	                }

	            }
	  }
	});
	code_toggle = function(event) {
	  	console.log(event.target.id);
	    var baseElement = event.target.nextElementSibling;
	    console.log(baseElement);
	    if (code_shown){
	        for (var i = 0; i < baseElement.childNodes.length; i++) {
	                elementToReturn = baseElement.childNodes[i];
	                if (elementToReturn.className == 'input') {
	                    for (var j=0; j < elementToReturn.childNodes.length; j++) {
	                      childtohide = elementToReturn.childNodes[j];
	                      if (childtohide.className == 'prompt input_prompt' || 
	                                  childtohide.className == 'inner_cell') {
	                            childtohide.style.display = 'none';
	                      }
	                    }
	                }
	            }
	        document.getElementById(event.target.id).innerHTML = 'Reveal code'
	      } else {
	        for (var i = 0; i < baseElement.childNodes.length; i++) {
	                elementToReturn = baseElement.childNodes[i];
	                if (elementToReturn.className == 'input') {
	                    for (var j=0; j < elementToReturn.childNodes.length; j++) {
	                      childtohide = elementToReturn.childNodes[j];
	                      if (childtohide.className == 'prompt input_prompt' || 
	                                  childtohide.className == 'inner_cell') {
	                            childtohide.style.display = 'block';
	                      }
	                    }
	                }
	            }
	        document.getElementById(event.target.id).innerHTML = 'Hide code';
	      }
	        code_shown = !code_shown;
	 }


## article.html

Then I needed to tell my theme to load `custom.js`. I went to `theme/(nameofmytheme)/templates/articles.html` to add before the content:

```
<script src="{{ SITEURL }}/theme/js/custom.js"></script>
```

## Et voilà! 

