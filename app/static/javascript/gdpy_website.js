
var questionAnswerElt = document.getElementById("answers");
questionAnswerElt.style.display = "None";

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
        // Creating a list of couples of questions and answers
        var newQuestionAnswer = createQuestionAnswer(question);
        var question = questionElt.value;
        // Creating a function to add to the list the new questions / answers
        var data = JSON.parse(reponse);
        var coordinates = data.coords;
        var url = data.url;
        var summary = data.summary;
        var speech = data.speech;
        
        // This function returns the question previously asked by the visitor.
        function returnQuestion() {
            var questionElt = document.createElement("p");
            var questionTextElt = document.createTextNode(question);
            questionElt.appendChild(questionTextElt);
            return questionElt;
        }

        // This function returns the speech produced by Grandpy to this question.
        function returnSpeech() {
            var speechElt = document.createElement("p");
            var speechTextElt = document.createTextNode(speech);
            speechElt.appendChild(speechTextElt);
            return speechElt;
        }

        // map à mettre dans une fonction createMap et mettre return à la fin.
        /* This function create a map and its marker, according to the GPS coordinates
        of the location found by the program.*/
        function createMap() {
            var mapElt = document.createElement("divmap");
            var myLatLng = {lat: coordinates[0], lng: coordinates[1]};
            var map = new google.maps.Map(mapElt {
                zoom: 4,
                center: myLatLng
            });
            var marker = new google.maps.Marker({
              position: myLatLng,
              map: map
            });
            return map, marker;
        }

        // summary
        function returnSummary() {
            var summaryElt = document.createElement("p");
            var summaryTextElt = document.createTextNode(summary);
            summaryElt.appendChild(summaryTextElt);
            return summaryElt;
        }

        // answer
        // inclure tous les éléments précédents dans 1 élément answer
        // ajouter answer à answers

        // créer lien + balise "a" avec title "en savoir plus" pour aller sur le site de la page wiki
        


        },
    true
    );
}); 

