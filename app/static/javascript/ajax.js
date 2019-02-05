// Creating a general ajaxPost function:
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