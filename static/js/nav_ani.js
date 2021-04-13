// Nav Class Add & Remove (Generic Way)
var menu_nav = $("#menu-nav");

$("#menu-btn").on("click", function() {
    if (menu_nav.hasClass("active")) {
        menu_nav.removeClass("active");
        $(this).children().removeClass("active");
        $("main").removeClass("active");
        $("footer").removeClass("active");
        $("body").removeClass("active");
        $(".nav-search-form-holder").removeClass("active");
    } else {
        menu_nav.addClass("active");
        $(this).children().addClass("active");
        $("main").addClass("active");
        $("footer").addClass("active");
        $("body").addClass("active");
        $(".nav-search-form-holder").addClass("active");
    }
});

// Nav Class Remove (Appendix | Outside of element)
$("main").on("click", function() {
    menu_nav.removeClass("active");
    $("#menu-btn").children().removeClass("active");
    $("main").removeClass("active");
    $("footer").removeClass("active");
    $("body").removeClass("active");
    $(".nav-search-form-holder").removeClass("active");
});
$("footer").on("click", function() {
    menu_nav.removeClass("active");
    $("#menu-btn").children().removeClass("active");
    $("main").removeClass("active");
    $("footer").removeClass("active");
    $("body").removeClass("active");
    $(".nav-search-form-holder").removeClass("active");
});