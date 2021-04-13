// * Search & Search Layer *
//?? Search Layer
$("#nav-search-inp").on("click",function() {
    $(".search").addClass("visible");
    $(".cats").removeClass("visible");
    $("#nav-reset-btn").css("display", "unset");
    $(".back-to-prev").css("display", "inherit");
});

//?? Close Search Layer
$("#nav-reset-btn").on("click",function() {
    if ($("#nav-search-inp").val() == "") {
        $(".cats").addClass("visible");
        $(".search").removeClass("visible");
        $("#nav-reset-btn").css("display", "none");
        $(".back-to-prev").css("display", "none");
    }
});

//?? Back To Previous
$(".back-to-prev").on("click", function() {
    $(".main").addClass("visible");
    $(".search").removeClass("visible");
    $(".cats").addClass("visible");
    $(this).css("display", "none");
    $("#nav-reset-btn").css("display", "none");
});

// nav-search-form (prevent empy search)
$(".nav-search-form").on("submit", function(event) {
    if ($(this).find('input').val() == "") {
        event.preventDefault();
        // On back-end also you shold prevent from empty search and search with whitespace
    }
});