
/*******Fonction pour vérifier que le token peut être envoyé dans l'entete*********/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*******recherche/affichage de résultat d'un algo par ajax*********/
function result_algo(arr) {

  console.log(arr);
  /*
  Avertir l'utilisateur du chargemnt
  */
  var liblSlct = $('#libelSlct');
  var saveSelectName = liblSlct.html();
  liblSlct.empty();
  liblSlct.append(jQuery('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>'));
  liblSlct.append('&nbsp;&nbsp;Chargement...');


  /*Entrer le token csrf dans le header si la route est sécurisé*/
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  /*console.log("csrf token : "+csrftoken);*/
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  $.ajax({
    type: 'POST',
    url: $('#algoch').val(),
    /*data: {
        login: $("#login").val(),
    }*/
    data: arr,
    success: function (data) {
      //console.log(data.valid_message);

      /*
      On indique à l'utilisateur que le chargement est fini
      */
      liblSlct.html(saveSelectName);

      $('#resultdiv').html(data);
            
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) { 
        alert("Status: " + textStatus); alert("Error: " + errorThrown); 
    }   

  });
};

function verif_bfr_send_data(){

  const regex = RegExp('^[0-9]+(\.|,)?[0-9]*$'); 

  valid = true;

  var arr= {};
  $('.numfield').each(
    function(index){  
        const input = $(this);
        const val = input.val();

        if (!regex.test(val)) valid = false;  

        arr[input.attr('id')] = val.replace(',','.');
    }
  );

  if($('#algoch').val() != 'none'){
    if(valid) result_algo(arr);
    else alert('There is an error in your data. \nRemember that they must be of numeric type (integer or float)')
  }

}

/****Verfication des champs de données format umérique euro ou US***/
$('.numfield').keyup(function() {

  var val = $(this).val();
  const regex = RegExp('^[0-9]+(\.|,)?[0-9]*$'); 

  if (regex.test(val)) {
    $(this).removeClass('invalid');
    $(this).addClass('valid');
  }
  else{
    $(this).removeClass('valid');
    $(this).addClass('invalid');
  }

});


