function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  var data = {
    'user': {
      'first_name': profile.getName(),
      'password': 'GOOGLE12345',
      'email': profile.getEmail()
    },
    'acc_type': 'google'
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
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    console.log('User signed out.');
  });
}