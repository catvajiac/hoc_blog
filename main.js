$(document).ready(function() {
  // FIREBASE STUFF
  /*
  var config = {
    apiKey: "AIzaSyCWZhtN2dqX9rpj5m8vrhK9pjCTBhzFxjE",
    authDomain: "hoc-blog.firebaseapp.com",
    databaseURL: "https://hoc-blog.firebaseio.com",
    projectId: "hoc-blog",
    storageBucket: "",
    messagingSenderId: "325290018245"
  };
  firebase.initializeApp(config);

  var ref = firebase.database().ref();
  ref.child("blogposts").on("child_added", function(snapshot){
    addPost(snapshot.val().title, snapshot.val().post); 
  });

  $("#postbutton").on("click", function(e) {
    console.log("Stuff was posted");
    var title = $("#blogtitle").val();
    $("#blogtitle").val("");
    var textarea = $("#blogpost").val();
    $("#blogpost").val("");
    console.log(title);
    console.log(textarea);
    ref.child("blogposts").push({
      title: title,
      post: textarea
    }).catch(console.log.bind(console));
  }); 

   var uiConfig = {
     signInSuccessUrl: '<url-to-redirect-to-on-success>',
     signInOptions: [
       firebase.auth.GithubAuthProvider.PROVIDER_ID,
     ]
   };

   var ui = new firebaseui.auth.AuthUI(firebase.auth());
   // The start method will wait until the DOM is loaded.
   //ui.start('#firebaseui-auth-container', uiConfig);


  function addPost(title, textarea) {
    $("body").append("<div class='blog_post'>")
    $("body").append("  <h3 class='title'>" + title + "</h3>")
    $("body").append("  <p>" + textarea + "</p>")
    $("body").append("</div>")
  };
  */


  //var fs = require("fs")
  function readFile(file) {
    if (!file) {
      return;
    };
    var reader = new FileReader();
    reader.onload = function(e) {
      var contents = e.target.result;
      // do stuff with content
      console.log(contents);
    };
    reader.readAsText(file);
  };

  readFile("posts/html/hi.html");
});
