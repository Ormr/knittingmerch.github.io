
$(document).ready(function(){
    $("a.scroll").click(function(){
        var elementClick = $(this).attr("href");
        $("html, body").animate({scrollTop: $(elementClick).offset().top}, 900);
    });
});
