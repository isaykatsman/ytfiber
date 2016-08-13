//popup.js by Isay Katsman for YT music

//new function that will perform downloading
function manage_download(e) {
  var t = $("download_btn").val();//document.getElementById("download_btn").value;
  chrome.bookmarks.getTree(function traverseBookmarks(bookmarkTreeNodes) {
    for(var i=0;i<bookmarkTreeNodes[0].children[0].children.length;i++) {
        if(!bookmarkTreeNodes[0].children[0].children[i].url) { //must mean that this is a folder
          //alert(bookmarkTreeNodes[0].children[0].children[i].title); //log out folder name
        } else {
          //console.log(bookmarkTreeNodes[i].title);
        }
        
        //if(bookmarkTreeNodes[0].children) {
            //traverseBookmarks(bookmarkTreeNodes[i].children);
        //} 

    }
  });

  //open a window
  var handle = window.open("http://mp3fiber.com");

  //change it's text
  handle.onload = function () {
    var text = handle.document.getElementsByName("videoURL")[0];
    text.innerHTML = "lololololololol"; //https://www.youtube.com/watch?v=73tGe3JE5IU
    alert('leleboiz');
  };
}

//add even listener once document has been loaded
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById("download_btn").addEventListener('click', manage_download);
  //main();
});