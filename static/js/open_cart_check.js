$(".up-down-btn").on("click",function() {
    if ($(this).hasClass("open")) {
        $(this).removeClass("open");
        $(".summary-area").removeClass("open");
    } else {
        $(this).addClass("open");
        $(".summary-area").addClass("open");
    }
});