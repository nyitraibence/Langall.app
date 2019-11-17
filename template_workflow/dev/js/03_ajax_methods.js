(function ($) {
    $(() => {
        $(".js-pending-lesson-ok").click(function () {
            var accepted_lesson_id = $(this).data("l-id");
            var ajax_url = $(this).data("ajax-url");
            console.log("selected lesson id:" + accepted_lesson_id);
            console.log("called ajax url:" + ajax_url);

            $.ajax({
                url: ajax_url,
                type: "GET",
                data: { lesson_id: accepted_lesson_id },
                dataType: 'json',
                success: function (json) {
                    $("[data-l-id=" + accepted_lesson_id + "]").css('background', '#000000');
                    console.log("successfully retrieved ajax response from server");
                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    console.log("Oops! an ajax error occured.");
                }
            });
        });

        $(".js-pending-lesson-not-ok").click(function () {
            var rejected_lesson_id = $(this).data("l-id");
            var ajax_url = $(this).data("ajax-url");
            console.log("selected lesson id:" + rejected_lesson_id);
            console.log("called ajax url:" + ajax_url);

            $.ajax({
                url: ajax_url,
                type: "GET",
                data: { lesson_id: rejected_lesson_id },
                dataType: 'json',
                success: function (json) {
                    $("[data-l-id=" + rejected_lesson_id + "]").css('background', '#000000');
                    console.log("successfully retrieved ajax response from server");
                },

                // handle a non-successful response
                error: function (xhr, errmsg, err) {
                    console.log("Oops! an ajax error occured.");
                }
            });
        });
    });
})(jQuery);
