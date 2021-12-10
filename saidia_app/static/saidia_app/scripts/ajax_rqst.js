// store dictionary of possible requestResponse handlers
var responseHandlers = {}

// function retrieves the resource using specified requestType
// you can pass data if required
function requestResource(requestType, url, data=null){
  var xhr = new XMLHttpRequest();

  // create a request
  xhr.open(requestType, url);
  // set content type if requestType == POST
  if(requestType == "POST"){
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  }
  // send request add data if not Null
  if(data == null){
    xhr.send()
  }
  else{
    xhr.send(data)
  }

  // get data in response if status is 200
  xhr.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200){
      console.log(JSON.parse(xhr.responseText));
      requestResponse(JSON.parse(xhr.responseText));
    }
  }
}

// set data on retrieval depending on
// the type of data in the data head
function requestResponse(data){
  responseHandlers[data.head](data.body);
}

// response handler for locationCoordinates
responseHandlers["locationCoordinates"] = function(data){
  // latitude and longitude respectively
  var lat = parseFloat(data.x);
  var lng = parseFloat(data.y);
  // create an object with latitude and longitude
  myLatLng = {lat: lat, lng: lng};

  // set input fields with coordinates
  x_coord_element.value = data.x;
  y_coord_element.value = data.y;

  // add a marker indicating currently selected location
  updateMarker(myLatLng);
}

responseHandlers["close_orphanages"] = function(data){
  console.log(data);
}
