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