(function($) {
    $(() => {
        $('.navbar-toggler').on('click', function() {
            $(this).toggleClass('is-active');
            $('.navbar-collapse.show[id]').each(function() {
                $(`.navbar-toggler.is-active[data-target="#${$(this).attr('id')}"]`).click();
            });
        });
    });
})(jQuery);
