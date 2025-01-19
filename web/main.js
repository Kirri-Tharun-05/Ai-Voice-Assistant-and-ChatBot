
$(document).ready(function () {
    $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        },
    });
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 840,
        height: 200,
        style:"ios9",
        speed:"0.1",
        amplitude:2
      });
      $('.siri-message').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"fadeInUp",
            sync:true
        },
        out:{
            effect:"fadeOutUp",
            sync:true
        },
    });
    $('#MicBtn').click(function(){
        eel.playAssistantSound()
        $('#ovel').attr("hidden",true)
        $('#siri-Wave').attr("hidden",false)
        eel.take_allCommands()()
    });
    function doc_keyUp(e){

        if(e.key==='j' && e.metaKey){
            eel.playAssistantSound()
            $('#ovel').attr("hidden",true)
            $('#siri-Wave').attr("hidden",false)
            eel.take_allCommands()()
        }
    }
    document.addEventListener('keyup',doc_keyUp,false);

    function playAssistant(message){

        if(message!="")
        {
            $("#ovel").attr("hidden",true);
            $("#siri-Wave").attr("hidden",false);
            eel.take_allCommands(message);
            $("#chatBox").val("");
            $("#MicBtn").attr("hidden",false)
            $("#SendBtn").attr("hidden",true)
        }
    }

    function ShowHidenButton(message){
        if(message.length==0)
        {
            $("#MicBtn").attr("hidden",false);
            $("#SendBtn").attr("hidden",true);
        }
        else
        {
            $("#MicBtn").attr("hidden",true);
            $("#SendBtn").attr("hidden",false);
        }
    }

    $("#chatBox").keyup(function () {
        let message=$("#chatBox").val();
        ShowHidenButton(message);
      });

      $("#SendBtn").click(function () {

        let message=$("#chatBox").val();
        playAssistant(message);
        
    });

    $("#chatBox").keypress(function(e){

        key=e.which;
        if(key == 13)
        {
            let message =$("#chatBox").val();
            playAssistant(message);
        }
    });
});