(function($) {
    $(function() {
        // CUSTOM SELECT
        $('select').each(function() {
            var selectId = $(this).attr('id');

            var disabled = $(this).hasClass('disabled');
            var redirect = $(this).hasClass('redirect');
            var withPicture = $(this).hasClass('with-picture');
            $(this).fadeOut(0);

            // IF AN OPTION IS SELECTED
            if ($('option.selected', this).length == 0) {
                var selected = $('option:selected', this).html();
            } else {
                var selected = $('option.selected', this).html();
            }

            if (disabled == true) var select = '<div class="select disabled">';
            else var select = '<div class="select">';
            select +=
                '<span class="label">' +
                selected +
                '</span>' +
                '<div class="arrow"><i class="fal fa-chevron-down"></i></div>' +
                '</div>';
            select += '<ul class="options" data-select-id="' + selectId + '">';

            $('option', this).each(function() {
                console.log($(this).val());
                if ($(this).prop('disabled') == true) {
                    var disabled = 'value disabled';
                } else {
                    var disabled =
                        'value value-' +
                        $(this)
                            .val()
                            .replace(' ', '_');
                }
                if ($(this).val() != -1) {
                    if (
                        redirect &&
                        $(this).data('href') != '' &&
                        $(this).data('href') != undefined
                    ) {
                        select +=
                            '<li class="' +
                            disabled +
                            '" data-value="' +
                            $(this).val() +
                            '"><a href="' +
                            $(this).data('href') +
                            '">' +
                            $(this)
                                .html()
                                .trim() +
                            '</a></li>';
                    } else {
                        if (withPicture) {
                            select +=
                                '<li class="' +
                                disabled +
                                '" data-value="' +
                                $(this).val() +
                                '" data-label="' +
                                $(this).data('label') +
                                '"><img src="' +
                                $(this).data('icon') +
                                '"><div>' +
                                $(this)
                                    .html()
                                    .trim() +
                                '<small>' +
                                $(this).data('remark') +
                                '</small></div></li>';
                        } else {
                            select +=
                                '<li class="' +
                                disabled +
                                '" data-value="' +
                                $(this).val() +
                                '">' +
                                $(this)
                                    .html()
                                    .trim() +
                                '</li>';
                        }
                    }
                }
            });
            // CLOSE IF USER CLICKS SOMEWHERE ELSE
            select +=
                "<script>$(document).mouseup(function (e) {var container = $('#" +
                selectId +
                "');if (!container.is(e.target) && container.has(e.target).length === 0) {$('.options').fadeOut(100);$('#" +
                selectId +
                " .select').removeClass('hover');}});</script>";

            $(this).wrap('<div class="own-select" id="' + $(this).attr('id') + '"></div>');
            $(this).removeAttr('id');
            $(this).after(select);

            // $(this).after('<div class="own-select">' + $(this).html() + select + '</div>');
        });

        $('.own-select .select').click(function() {
            // OWN-SELECT WITH-RADIOBUTTON DOES NOT COVER .SELECT SO IT DOES NOT LET .OPTION TO HIDE
            if (!$(this).hasClass('hover')) {
                $(this)
                    .parent()
                    .children('.options')
                    .fadeIn(100);
                $(this)
                    .parent()
                    .children('.select')
                    .addClass('hover');
                $(this)
                    .parent()
                    .children('.select img')
                    .addClass('opened');
                $(this)
                    .parent()
                    .find('.option-search')
                    .focus();
            } else {
                $(this)
                    .parent()
                    .children('.select')
                    .removeClass('hover');
                $(this)
                    .parent()
                    .children('.select img')
                    .removeClass('opened');
            }
        });

        // CLICKINK ON AN OPTION OF THE CUSTOM SELECT
        $('.own-select .options li').click(function() {
            $(this)
                .parent('.options')
                .find('li')
                .removeClass('selected');
            $('.with-radiobutton li').removeClass('selected');
            $(this).addClass('selected');
            var value = $(this).data('value');
            var selectId = $(this)
                .parents('.options')
                .data('select-id');

            // $(this).parent().parent().children('.select').removeClass('hover');
            $('.select').removeClass('hover');
            $(this)
                .parent('.options')
                .fadeOut(100);
            $('#' + selectId + ' select').val(value);
            $('#' + selectId + ' select').change();

            if ($('#' + selectId).hasClass('with-picture')) {
                $('#' + selectId + ' .label').html($(this).data('label'));
            } else {
                $('#' + selectId + ' .label').html($(this).text());
            }
        });

        // RESET SELECTED CUSTOM SELECT
        $('.own-select').bind('reset', function() {
            $('select', this).val(-1);
            $('.options .selected', this).removeClass('selected');
            $('.label', this).html($('select option:selected', this).html());
        });

        // IF ORIGINAL SELECT HAS SELECTED OPTION THEN REFRESH WILL UPDATE TJE CUSTOM BUILT SELECT
        $('.own-select').bind('refresh', function() {
            var selected = $('select option:selected', this).val();
            if (selected != undefined) {
                selected = selected.toString().replace(' ', '_');
            }
            $('.options .value-' + selected + '', this).addClass('selected');
            var label = $('.options .value-' + selected + '', this).text();
            $('.select .label', this).html(label);
        });

        $('.own-select').bind('rebuild', function() {
            var selectId = $(this).attr('id');
            var selected = $('select option:selected', this).val();
            if (selected != undefined) {
                selected = selected.toString().replace(' ', '_');
            }
            $('.options .value-' + selected + '', this).addClass('selected');
            var label = $('.options .value-' + selected + '', this).text();
            $('.select .label', this).html(label);

            $('select option', this).each(function() {
                if ($(this).prop('disabled') == true) {
                    var disabled = 'value disabled';
                } else {
                    var disabled =
                        'value value-' +
                        $(this)
                            .val()
                            .replace(' ', '_');
                }
                if ($(this).val() != -1) {
                    select +=
                        '<li class="' +
                        disabled +
                        '" data-value="' +
                        $(this).val() +
                        '">' +
                        $(this)
                            .html()
                            .trim() +
                        '</li>';
                }
            });
            $(this)
                .find('.options')
                .html(select);
        });
    });
})(jQuery);
