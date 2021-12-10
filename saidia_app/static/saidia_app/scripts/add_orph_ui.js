// this stores all the ui elements that are involved in updating the coordinates of a place.

// constants
const csrfToken = document.querySelector('#main_div input').value;
const locationSelect = document.querySelector('#main_div select');
const x_coord_element = document.querySelector("#main_div input:nth-of-type(4)");
const y_coord_element = document.querySelector("#main_div input:nth-of-type(5)");

// variables
var map = document.querySelector("#map");
