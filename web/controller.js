$(document).ready(function(){

eel.expose(DisplayMessage)

function DisplayMessage(message){
    $(".siri-message li:first").text(message);
    $('.siri-message').textillate('start');
}

eel.expose(home)
function home()
{
    $("#ovel").attr("hidden",false)
    $("#siri-Wave").attr("hidden",true);
}

eel.expose(senderText)
function senderText(message)
{
    var chatBox=document.getElementById("chat-canvas-body");
    if(message.trim()!== ""){
        chatBox.innerHTML +=`<div class="row justify-content-end mb-4 tha">
        <div class="width-size">
            <div class="sender_message">${message}</div>
        </div>
        </div>;`
        chatBox.scrollTop=chatBox.scrollHeight;
    }
}

eel.expose(receiverText)
function receiverText(message){
    var chatBox=document.getElementById("chat-canvas-body");
    if(message.trim()!==""){
        chatBox.innerHTML+=`<div class="row justify-content-start mb-4">
        <div class="width-size">
        <div class="receiver_message">${message}</div>
        </div>
        </div>`;
        chatBox.scrollTop=chatBox.scrollHeight;
    }
}

});