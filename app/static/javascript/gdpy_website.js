
var questionAnswerElt = document.getElementById("answers");
questionAnswerElt.style.display = "None";
var loadingIconElt = document.getElementById("loading_icon");
loadingIconElt.style.display = "None";


// This function returns the question previously asked by the visitor.
function returnQuestion(question) {
    var questionElt = document.createElement("p");
    var questionTextElt = document.createTextNode(question);
    questionElt.appendChild(questionTextElt);
    questionElt.classList.add("question");
    return questionElt;
}

// This function returns the speech produced by Grandpy to this question.
function returnSpeech(speech) {
    var speechElt = document.createElement("p");
    var speechTextElt = document.createTextNode(speech);
    speechElt.appendChild(speechTextElt);
    speechElt.classList.add("speech");
    return speechElt;
}

/* This function create a map and its marker, according to the GPS coordinates
of the location found by the program.*/
function createMap(coordinates) {
    var mapElt = document.createElement("div");
    mapElt.classList.add("map");
    var myLatLng = {lat: coordinates[1], lng: coordinates[2]};
    var map = new google.maps.Map(mapElt, {
        zoom: 4,
        center: myLatLng
    });
    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map
    });
    return mapElt;
}

// This function returns the summary found by Grandpy on the wikipedia' website.
function returnSummary(summary, url) {
    var summaryElt = document.createElement("p");
    summaryElt.classList.add("summary");
    //var summaryTextElt = document.createTextNode(summary + " ");
    //summaryElt.appendChild(summaryTextElt);
    summaryElt.innerHTML = summary + " "
    var linkElt = document.createElement("a");
    linkElt.href = url;
    var knowMoreElt = document.createTextNode("En savoir plus")
    linkElt.appendChild(knowMoreElt)
    summaryElt.appendChild(linkElt)
    return summaryElt;
}

// This function returns all the previous elements as a global answer.
function addAnswer(question, answer) {
    var questionElt = returnQuestion(question);
    var speechElt = returnSpeech(answer.speech);
    var summaryElt = returnSummary(answer.summary, answer.url);
    var mapElt = createMap(answer.coords);

    var answerElt = document.createElement("div");
    answerElt.classList.add("answer");
    answerElt.appendChild(questionElt);
    answerElt.appendChild(speechElt);
    answerElt.appendChild(summaryElt);
    answerElt.appendChild(mapElt);

    var answersElt = document.getElementById("answers");
    answersElt.appendChild(answerElt);
}

// Grandpy's answer and map appear when form is submitted.
var formElt = document.getElementById("form");
formElt.addEventListener("submit", function(e) {
    e.preventDefault();
    var questionElt = document.querySelector("#gp_question");
    question = {
        question : questionElt.value
    };

    ajaxPost("/answer", question, function(reponse) {
        var question = questionElt.value;
        var data = JSON.parse(reponse);
        addAnswer(question, data);
    },
    true
    );
    //
    // Replacing the form by a loading logo for 3 seconds:
    var divFormElt = document.querySelector("form");
    divFormElt.style.display = "None";
    loadingIconElt.style.display = "block";
    setTimeout(function() {
        divFormElt.style.display = "block";
        loadingIconElt.style.display = "none";    
    }, 3000);
    questionAnswerElt.style.display = "block";
}); 

