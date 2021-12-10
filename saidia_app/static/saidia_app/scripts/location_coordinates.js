// add eventListener for change in location
locationSelect.addEventListener('change', ()=>{getCoord(locationSelect.value)});

// returns the coordinates of the location
// with given id
function getCoord(location_id){

  //Object contains the id of the location
  data = `csrfmiddlewaretoken=${csrfToken}&id=${location_id}`
  // get the resource
  requestResource("POST", "/get_coord", data);
}
