function getPosition(){
  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(showPosition, showError);
    return
  }
  console.log("this app needs to access your location to function")
}

// function extracts relevant data
// from the position object
function showPosition(position){
  lat = position.coords.latitude;
  lon = position.coords.longitude;
  data = `csrfmiddlewaretoken=${csrfToken}&lat=${lat}&lon=${lon}`;
  requestResource("POST", "/", data);
}

// if error is raised,
// this function receives the error as an
// argument and handles it appropriately
function showError(error){
  console.log(error);
}
