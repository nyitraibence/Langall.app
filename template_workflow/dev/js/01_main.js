(function ($) {
    $(() => {
        console.log('Hello Django user!');
        $('[data-toggle="tooltip"]').tooltip()
    });
})(jQuery);


$('.jarallax').jarallax({
    speed: 0.5,
    disableParallax: /iPad|iPhone|iPod|Android/
});

$('.jarallax-icon').jarallax({
    speed: .5,
    disableParallax: /iPad|iPhone|iPod|Android/
});

$(document).ready(function () {
    $("a").on('click', function (event) {
        if (this.hash != "") {
            event.preventDefault();

            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top - 65
            }, 600);
        }
    });
});