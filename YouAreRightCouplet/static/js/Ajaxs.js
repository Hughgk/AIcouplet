$(function () {
    $("#submit").click(function () {
        var context = $("#mycouplet").val();


        $.post('/test', {"mycouplet": context}, function (json, textStatus) {
            var output = json["output"];


            $("#downtext").empty();

            for (var i = 0; i < output.length; i++) {
                $("#downtext").append("<tr><td>" + output[i] + "</td></tr>")

            }
            console.log("真的不执行吗");
            $("#result").append("<p>" + context + " : " + output + "</p>");
            console.log("真的执行");

        });
    });


    $("#mycouplet").change(function () {
        console.log($("#mycouplet").val());
        var context = $("#mycouplet").val();

        $("#uptext").empty();
        for (var i = 0; i < context.length; i++) {
            $("#uptext").append("<tr><td>" + context[i] + "</td></tr>")

        }

    });




});