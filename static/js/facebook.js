// This is called with the results from from FB.getLoginStatus().
function statusChangeCallback(response) {
  //console.log(response);
  // The response object is returned with a status field that lets the app know the current login status of the person.
  // Full docs on the response object can be found in the documentation for FB.getLoginStatus().
  if (response.status === 'connected') {
    // Logged into your app and Facebook.
    testAPI();
  } else if (response.status === 'not_authorized') {
    // The person is logged into Facebook, but not your app.
  } else {
    // The person is not logged into Facebook, so we're not sure if they are logged into this app or not.
  }
}

// This function is called when someone finishes with the Login
// Button.  See the onlogin handler attached to it in the sample
// code below.
function checkLoginState() {
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}

window.fbAsyncInit = function() {
FB.init({
  appId      : '314371472349211',
  cookie     : true,
  xfbml      : true,
  version    : 'v2.8'
});

// Now that we've initialized the JavaScript SDK, we call 
// FB.getLoginStatus().  This function gets the state of the
// person visiting this page and can return one of three states to
// the callback you provide.  They can be:
//
// 1. Logged into your app ('connected')
// 2. Logged into Facebook, but not your app ('not_authorized')
// 3. Not logged into Facebook and can't tell if they are logged into
//    your app or not.
//
// These three cases are handled in the callback function.

FB.getLoginStatus(function(response) {
  statusChangeCallback(response);
});

};

// Load the SDK asynchronously
(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Here we run a very simple test of the Graph API after login is
// successful.  See statusChangeCallback() for when this call is made.
function testAPI() {
  //console.log('Welcome!  Fetching your information.... ');
  FB.api('/me/?fields=id,first_name,last_name,email', function(response) {

    var data = {
      'user': {
        'first_name': response['first_name'],
        'password': 'FB12345',
        'email': response['email'] == undefined ? response['email'] : ''
      },
      'acc_type': 'facebook'
    };

    console.log(data);

    $.ajax({
        url: '/user/new',
        contentType : 'application/json; charset=utf-8',
        type: 'POST',
        data: JSON.stringify(data),
        dataType: 'json',
        success: function (response) {
           // you will get response from your php page (what you echo or print)                 
        },
        error: function(jqXHR, textStatus, errorThrown) {
           console.log(textStatus, errorThrown);
        }
    });
  });
}