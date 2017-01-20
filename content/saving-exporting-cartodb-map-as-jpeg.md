Title: Saving/Exporting CartoDB map as jpeg.
Date: 2016-06-01 20:42:17
Category: coding
Tags: cartodb, leaflet, javascript
Slug: saving-exporting-cartodb-map-as-jpeg
Summary: Add an export button to your Leaflet map 
Status: 
Image: /images/saveexportleaflet.png

I've recently needed to make a **save/export static map** from data stored in Cartodb and shown on a leaflet map. There are a couple of plugins for leaflet, but none was satisfying; either printing only around my map, or only the map. I also did not want to use the 'print' to pdf function of the browser, I wanted to save as an image. I found a few articles online, and [this one](https://groups.google.com/forum/#!topic/cartodb/VxysRLNUs6s) mentioned html2canvas but without sharing any parameters.. and when I tried using it out of the box, I could not print the legend (which is the same as Cartodb embeded 'Save Map' function).
I eventually used this configuration:

	:::JavaScript
	function printmap(){
	  var screenshot = {};
	  //Hide the toolbars (zoom and search bars)
	  $('.leaflet-top.leaflet-left').addClass('hide');
	  $('.leaflet-top.leaflet-right').addClass('hide');
	  //Make sure that the legend panel is opened
	  sidebar.open('home');
	  //Grab the map
	  canvasdiv = document.getElementsByTagName("body")[0];
	  //html2canvas function. These options seemed to work for me.
	  html2canvas(canvasdiv, {
	     letterRendering: true,
	     taintTest: true,
	     useCORS: true,
	     onrendered: function(canvas) {
			//inspired from http://stackoverflow.com/questions/31656689/how-to-save-img-to-users-local-computer-using-html2canvas/31657234#31657234
	        var a = document.createElement('a');
	        // toDataURL defaults to png, so we need to request a jpeg, then convert for file download.
	        a.href = canvas.toDataURL("image/png").replace("image/jpeg", "image/octet-stream");
	        a.download = 'havfriluftsliv_kort.jpg';
	        a.click();
	        }
	  });
	}

 
 I call this function with an [easy button](https://github.com/CliffCloud/Leaflet.EasyButton) from the Leaflet map.
