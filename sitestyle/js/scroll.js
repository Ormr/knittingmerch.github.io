
$(document).ready(function(){
    $("a.scroll").click(function(){
        var elementClick = $(this).attr("href");
        // var destination = $(elementClick).offset().top;
        $("html, body").animate({scrollTop: $(elementClick).offset().top}, 900);
    });
});
