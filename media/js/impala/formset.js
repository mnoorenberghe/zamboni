function updateTotalForms(prefix, inc) {
    var $totalForms = $('#id_' + prefix + '-TOTAL_FORMS'),
        inc = inc || 1,
        num = parseInt($totalForms.val(), 10) + inc;
    $totalForms.val(num);
    return num;
}


/**
 * zAutoFormset: handles Django formsets with autocompletion like a champ!
 * by cvan
 */

(function($) {

$.fn.zAutoFormset = function(o) {

    o = $.extend({
        delegate: document.body,   // Delegate (probably some nearby parent).

        forms: null,               // Where all the forms live (maybe a <ul>).

        extraForm: '.extra-form',  // Selector for element that contains the
                                   // HTML for extra-form template.

        prefix: 'form',            // Formset prefix (Django default: 'form').

        hiddenField: null,         // This is the name of a (hidden) field
                                   // that will contain the value of the
                                   // formPK for each newly added form.

        removeClass: 'remove',     // Class for button triggering form removal.

        formSelector: 'li',        // Selector for each form container.

        formPK: 'id',              // Primary key for initial forms.

        src: null,                 // Source URL of JSON search results.

        input: null,               // Input field for autocompletion search.

        searchField: 'q',          // Name of form field for search query.

        excludePersonas: true,     // Exclude Personas in search results?

        minSearchLength: 3,        // Minimum character length for queries.

        width: 300,                // Width (pixels) of autocomplete dropdown.

        addedCB: null,             // Callback for each new form added.

        removedCB: null,           // Callback for each form removed.

        autocomplete: null         // Custom handler you can provide to handle
                                   // autocompletion yourself.
    }, o);

    var $delegate = $(o.delegate),
        $forms = o.forms ? $delegate.find(o.forms) : $delegate,
        $extraForm = $delegate.find(o.extraForm),
        formsetPrefix = o.prefix,
        hiddenField = o.hiddenField,
        removeClass = o.removeClass,
        formSelector = o.formSelector,
        formPK = o.formPK,
        src = o.src || $delegate.attr('data-src'),
        $input = o.input ? $(o.input) : $delegate.find('input.autocomplete'),
        searchField = o.searchField,
        excludePersonas = o.excludePersonas,
        minLength = o.minSearchLength,
        width = o.width,
        addedCB = o.addedCB,
        removedCB = o.removedCB,
        autocomplete = o.autocomplete;

    function findItem(item) {
        if (item) {
            var $item = $forms.find('[name$=-' + hiddenField + '][value=' + item[formPK] + ']');
            if ($item.length) {
                var $f = $item.closest(formSelector);
                return {'exists': true, 'visible': $f.is(':visible'), 'item': $f};
            }
        }
        return {'exists': false, 'visible': false};
    }

    function clearInput() {
        $input.val('');
        $input.removeAttr('data-item');
    }

    function added() {
        var item = JSON.parse($input.attr('data-item'));

        // Check if this item has already been added.
        var dupe = findItem(item);
        if (dupe.exists) {
            if (!dupe.visible) {
                // Undelete the item.
                var $item = dupe.item;
                $item.find('input[name$=-DELETE]').removeAttr('checked');
                $item.slideDown();
            }
            clearInput();
            return;
        }

        clearInput();

        var formId = updateTotalForms(formsetPrefix, 1) - 1,
            emptyForm = $extraForm.html().replace(/__prefix__/g, formId);

        var $f;
        if (addedCB) {
            $f = addedCB(emptyForm, item);
        } else {
            $f = $(f);
        }

        $f.hide().appendTo($forms).slideDown();

        // Update hidden field.
        $forms.find(formSelector + ':last [name$=-' + hiddenField + ']')
              .val(item[formPK]);
    }

    function removed(el) {
        el.slideUp();
        // Mark as deleted.
        el.find('input[name$=-DELETE]').attr('checked', true);

        if (removedCB) {
            removedCB(el);
        }

        // If this was not an initial form (i.e., an extra form), delete the
        // form and decrement the TOTAL_FORMS count.
        if (!el.find('input[name$=-' + formPK + ']').length) {
            el.remove();
            updateTotalForms(formsetPrefix, -1);
        }
    }

    if (autocomplete) {
        autocomplete();
    } else {
        $input.autocomplete({
            minLength: minLength,
            width: width,
            source: function(request, response) {
                var d = {};
                d[searchField] = request.term;
                if (excludePersonas) {
                    d['exclude_personas'] = true;
                }
                $.getJSON(src, d, response);
            },
            focus: function(event, ui) {
                event.preventDefault();
                $input.val(ui.item.label);
            },
            select: function(event, ui) {
                event.preventDefault();
                if (ui.item) {
                    $input.val(ui.item.label);
                    $input.attr('data-item', JSON.stringify(ui.item));
                    added();
                }
            }
        }).data('autocomplete')._renderItem = function(ul, item) {
            if (!findItem(item).visible) {
                var $a = $(format('<a><img src="{0}">{1}</a>',
                                  [item.icon, item.label]));
                return $('<li>').data('item.autocomplete', item)
                                .append($a).appendTo(ul);
            }
        };
    }

    $delegate.delegate('.' + removeClass, 'click', _pd(function() {
        removed($(this).closest(formSelector));
    }));

};

})(jQuery);