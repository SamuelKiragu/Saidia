// marker set to the selected location by default
// data structure stores marker
var marker;


// initializing map
// map defaults to the set coordinates
function initMap(lat=1.292100, lng=36.821900){
  const myLatLng = {lat : lat, lng: lng}
  map = new google.maps.Map(map, {
    zoom: 10,
    center: myLatLng,
  });

  map.addListener('click', (e) => {
    updateMarker(e.latLng);
  });
}

// checks if there is an already existent marker
// and replaces it
function updateMarker(myLatLng){
  if(marker != null){
    // remove current marker
    marker.setMap(null);
  }
  // add new marker
  addMarker(myLatLng);
}

// function adds marker to the map
function addMarker(myLatLng){
  // default marker
  marker  = new google.maps.Marker({
    position: myLatLng,
    // icon: "http://127.0.0.1:8000/static/saidia_app/icons/orphanage.png"
  });
  marker.setMap(map);
  // center map using marker
  position = marker.getPosition();
  map.setCenter(position);

  // update x-coordinate and y-coordinate
  x_coord_element.value = position.lat();
  y_coord_element.value = position.lng();
}
