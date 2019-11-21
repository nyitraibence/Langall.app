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