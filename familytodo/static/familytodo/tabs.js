function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

function switchTab(evt, tabName){
  //variables
  var i, tmp, containers, tablinks;

  // Get all containers and hide them
  containers = document.getElementsByClassName("container-fluid");


  for(i = 0; i < containers.length; i++){
    if(containers[i].id === tabName){
      containers[i].style.display="flex";
    }else{
      containers[i].style.display="none";
    }
  }


}

