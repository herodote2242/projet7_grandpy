
var questionAnswerElt = document.getElementById("answers");
questionAnswerElt.style.display = "None";

//A METTRE DANS ajax.js
// creating a general ajaxPost function:
function ajaxPost(url, data, callback, isJson) {
    var req = new XMLHttpRequest();
    req.open("POST", url);
    req.addEventListener("load", function() {
        if (req.status >= 200 && req.status < 400) {
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function() {
        console.error("erreur réseau avec l'url" + url);
    });
    if (isJson) {
        // If the content of the request is JSON's type :
        req.setRequestHeader("content-Type", "application/json");
        data = JSON.stringify(data);
    }
    req.send(data);
}


// Grandpy's answer and map appear when form is submitted.
var formElt = document.getElementById("form");
formElt.addEventListener("submit", function() {
    e.preventDefault();
    var questionElt = document.querySelector("#question_asked");
    question = {
        question : questionElt.value
    };
    ajaxPost("/answer", question, function(reponse) {
        var answersElt = document.getElementById("answers");
        // creating a list of couples of questions and answers
        var newQuestionAnswer = createQuestionAnswer(question);
        var question = questionElt.value;
        // creating a function to add to the list the new questions / answers
        var data = JSON.parse(reponse);
        var coordinates = data.coords;
        var url = data.url;
        var summary = data.summary;
        var speech = data.speech;
        
        // question
        var questionElt = document.createElement("p");
        var questionTextElt = document.createTextNode(question);
        questionElt.appendChild(questionTextElt);

        // speech
        var speechElt = document.createElement("p");
        var speechTextElt = document.createTextNode(speech);
        speechElt.appendChild(speechTextElt);

        // map à mettre dans une fonction createMap et mettre return à la fin.
        //idem pour summary, speech
        var mapElt = document.createElement("div");
        var myLatLng = {lat: coordinates[0], lng: coordinates[1]};

        var map = new google.maps.Map(mapElt {
          zoom: 4,
          center: myLatLng
        });

        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map
        });        

        // summary
        var questionElt = document.createElement("p");
        var questionTextElt = document.createTextNode(question);
        questionElt.appendChild(questionTextElt);

        // answer
        // inclure tous les éléments précédents dans 1 élément answer
        // ajouter answer à answers

        // créer lien + balise "a" avec title "en savoir plus" pour aller sur le site de la page wiki
        


        },
    true
    );
}); 

