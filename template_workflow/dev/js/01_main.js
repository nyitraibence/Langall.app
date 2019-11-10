(function ($) {
    $(() => {
        console.log('Hello Django user!');
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
