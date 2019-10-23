(function ($) {
    $(() => {
        /* Cookie Policy */
        // Check cookie
        if (Cookies.get('cookiepolicy') !== 'active') $('#cookieAcceptBar').show();
        // Assign cookie on click
        $('#cookieAcceptBarConfirm').on('click', () => {
            Cookies.set('cookiepolicy', 'active', { expires: 31, path: '/' });
            $('#cookieAcceptBar').fadeOut();
        });
    });
})(jQuery);
