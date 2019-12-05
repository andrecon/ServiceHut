// Get the modal
var modal = document.getElementById("myModal");
              
// Get the image and insert it inside the modal - use its "alt" text as a caption
// var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");

var captionText = document.getElementById("caption");

function display(element)
{
    var img = document.getElementById(element.id);

    modal.style.display = "block";
    modalImg.src = img.src;
    var data = img.nextSibling.nextElementSibling.innerHTML;
    
    captionText.innerHTML = data;
}


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}


$(function() {
  $('p.edit').click(function(e) {
    e.preventDefault();
    $(this).text(($(this).text() == 'Volunteer List: [Click to Show Volunteers]') ? 'Volunteer List:' : 'Volunteer List: [Click to Show Volunteers]').fadeIn();
    
    var list = $(this).next("spam").next("ol").attr("id");

    var total = $(this).next("spam").attr("id");

    var theList = document.getElementById(list).getElementsByTagName("li");
    var numberOfItems = theList.length;
    
    document.getElementById(total).innerHTML = "Current Number of Volunteers: " + numberOfItems.toString();
   
    hide(list, total);

  });
});

function hide(element, total)
{
  var list = document.getElementById(element);

  var elementData = document.getElementById(total);

  if (elementData.style.display == "none"){
    elementData.style.display = "block";
  }else{
    elementData.style.display = "none";
  }


  // console.log(list);
  if (list.style.display == "none"){
    list.style.display = "block";
  }else{
    list.style.display = "none";
  }
}

(function(){
  // some code…
 })();