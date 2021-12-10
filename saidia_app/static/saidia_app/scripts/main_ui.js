// navigation options
var optnLst = document.querySelectorAll('.optn');
// div that shows change
var chDiv = document.querySelector('.optn:nth-child(1)');

// add eventListener for each optn in the list
optnLst.forEach((item) => {
  item.addEventListener('click', () => changeOptn(item));
});


// function to change Option selected
function changeOptn(item){
  // get initial height
  var i = chDiv.getBoundingClientRect().top;
  // get final height
  var f = item.getBoundingClientRect().top;
  // get value of top styling
  var t = parseInt(chDiv.style.top.slice(0,-2));

  // new t
  console.log(t);
  t =  t + (f - i);
  chDiv.style.top = t+"px"
}
