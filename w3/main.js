var btn = document.querySelector('#add');
var input = document.querySelector('input');
let list = document.querySelector('.list');

var close = document.getElementsByClassName("close");

btn.onclick = function() {
if(input.value!=''){

    let el = document.createElement('li');
    el.innerHTML = input.value;
    //el.style = 'border: 1px solid black';
    el.style.paddingLeft='10px';
    list.appendChild(el);
    input.value='';
    
    
    var checkbox = document.createElement("input");
    checkbox.type='checkbox';
    checkbox.style.float='left';
    checkbox.onclick = function() {
            var div = this.parentElement;

            if(div.className=='checked'){
                div.className='non';
            }
            else {
            div.className = 'checked';
            }
    }
   
 
    el.appendChild(checkbox);

  var span = document.createElement("SPAN");
 // var txt = document.createTextNode("\u00D7");

 var img = document.createElement("IMG");
 img.src = "trash.png"; 
 img.style.width='20px';
 img.style.height='20px';
 img.style.marginLeft='100px';

  span.className = "close";
  span.appendChild(img);
  el.appendChild(span);


}
else {
    alert('input can\'t be null');
}
 
for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
        }
  }

}
