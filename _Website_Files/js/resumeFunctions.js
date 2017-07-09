$(document).ready(function(){
      jQuery('.clickableImg img').on("click", function () {
        var clickedPicSrc = $(this).prop('src');
        var clickedPicAlt = $(this).prop('alt');
        var captionText = document.getElementById("caption");
        clickedPicSrc = clickedPicSrc.slice(-100,-4)+"L"+clickedPicSrc.slice(-4);
        captionText.innerHTML = clickedPicAlt;
        $('#myModal img').prop('src', clickedPicSrc);
        $('#myModal img').prop('alt', clickedPicAlt);
        $('#myModal').css("display", "block");
})});

if(document.getElementsByClassName('flex-item').length === 0) {
      document.getElementById('topContacts').style.display = 'none';
}
if(document.getElementsByTagName('h1').length === 0) {
      document.getElementById('header').style.display = 'none';
}
if(document.getElementsByClassName('work-entry').length === 0) {
      document.getElementById('workExperience').style.display = 'none';
}
if(document.getElementsByClassName('project-entry').length === 0) {
      document.getElementById('projects').style.display = 'none';
}
if(document.getElementsByClassName('education-entry').length === 0) {
      document.getElementById('education').style.display = 'none';
}
if(document.getElementsByClassName('honor-entry').length === 0) {
      document.getElementById('honor').style.display = 'none';
}
if(document.getElementsByClassName('flex-item').length === 0) {
      document.getElementById('lets-connect').style.display = 'none';
}
if(document.getElementById('map') === null) {
      document.getElementById('mapDiv').style.display = 'none';
}