# A list of our CSS and JS assets for jingo-minify.

CSS = {
    'mkt/devreg': (
        # Contains reset, clearfix, etc.
        'css/devreg/base.css',

        # Base styles (body, breadcrumbs, islands, columns).
        'css/devreg/base.less',
        'css/devreg/breadcrumbs.less',

        # Typographical styles (font treatments, headings).
        'css/devreg/typography.less',

        # Header (aux-nav, masthead, site-nav).
        'css/devreg/header.less',

        # Item rows (used on Dashboard).
        'css/devreg/listing.less',
        'css/devreg/paginator.less',

        # Buttons (used for paginator, "Edit" buttons, Refunds page).
        'css/devreg/buttons.less',

        # Popups, Modals, Tooltips.
        'css/devreg/devhub-popups.less',
        'css/devreg/tooltips.less',

        # L10n menu ("Localize for ...").
        'css/devreg/l10n.less',

        # Forms (used for tables on "Manage ..." pages).
        'css/common/forms.less',
        'css/devreg/devhub-forms.less',

        # Landing page
        'css/devreg/landing.less',

        # "Manage ..." pages.
        'css/devreg/manage.less',
        'css/devreg/prose.less',
        'css/devreg/authors.less',
        'css/devreg/in-app-config.less',
        'css/devreg/paypal.less',
        'css/devreg/refunds.less',
        'css/devreg/status.less',

        # Image Uploads (used for "Edit Listing" Images and Submission).
        'css/devreg/media.less',
        'css/common/invisible-upload.less',

        # Submission.
        'css/devreg/submit-progress.less',
        'css/devreg/submit-terms.less',
        'css/devreg/submit-manifest.less',
        'css/devreg/submit-details.less',
        'css/devreg/validation.less',

        # Developer Log In / Registration.
        'css/devreg/login.less',

        # Footer.
        'css/devreg/footer.less',
    ),
    'mkt/devreg-legacy': (
        'css/devreg-legacy/developers.less',  # Legacy galore.
    ),
    'mkt/reviewers': (
        'css/mkt/reviewers.less',
    ),
    'mkt/consumer': (
        'css/mkt/reset.less',
        'css/mkt/typography.less',
        'css/mkt/site.less',
        'css/common/invisible-upload.less',
        'css/common/forms.less',
        'css/mkt/forms.less',
        'css/mkt/header.less',
        'css/mkt/breadcrumbs.less',
        'css/mkt/buttons.less',
        'css/mkt/detail.less',
        'css/mkt/slider.less',
        'css/mkt/promo-grid.less',
        'css/mkt/overlay.less',
        'css/mkt/search.less',
        'css/mkt/paginator.less',
        'css/mkt/suggestions.less',
        'css/mkt/support.less',
        'css/mkt/account.less',
        'css/mkt/account-purchases.less',
        'css/mkt/home.less',
        'css/mkt/login.less',
        'css/mkt/purchase.less',
        'css/devreg/l10n.less',
        'css/impala/lightbox.less',
        'css/mkt/lightbox.less',
        'css/mkt/browse.less',
    ),
    'mkt/ecosystem': (
        'css/ecosystem/landing.less',
        'css/ecosystem/footer.less',
	),
    'mkt/in-app-payments': (
        'css/mkt/reset.less',
        'css/mkt/typography.less',
        'css/mkt/buttons.less',
        'css/mkt/in-app-payments.less',
    ),
    'mkt/stats': (
        'css/mkt/stats.less',
    ),
}

JS = {
    'mkt/devreg': (
        'js/lib/jquery-1.6.4.js',
        'js/lib/webtrends.js',
        'js/lib/underscore.js',
        'js/zamboni/browser.js',
        'js/amo2009/addons.js',
        'js/common/tracking.js',
        'js/devreg/init.js',  # This one excludes buttons initialization, etc.
        'js/impala/capabilities.js',
        'js/lib/format.js',
        'js/lib/jquery.cookie.js',
        'js/zamboni/storage.js',
        'js/zamboni/tabs.js',

        # jQuery UI.
        'js/lib/jquery-ui/jquery.ui.core.js',
        'js/lib/jquery-ui/jquery.ui.position.js',
        'js/lib/jquery-ui/jquery.ui.widget.js',
        'js/lib/jquery-ui/jquery.ui.mouse.js',
        'js/lib/jquery-ui/jquery.ui.autocomplete.js',
        'js/lib/jquery-ui/jquery.ui.datepicker.js',
        'js/lib/jquery-ui/jquery.ui.sortable.js',

        'js/zamboni/truncation.js',
        'js/zamboni/helpers.js',
        'js/zamboni/global.js',
        'js/zamboni/l10n.js',
        'js/zamboni/debouncer.js',

        # Users.
        'js/zamboni/users.js',

        # Forms.
        'js/impala/forms.js',

        # Login.
        'js/zamboni/browserid_support.js',
        'js/impala/login.js',

        # Fix-up outgoing links.
        'js/zamboni/outgoing_links.js',

        # Stick.
        'js/lib/stick.js',

        # Developer Hub-specific scripts.
        'js/zamboni/truncation.js',
        'js/common/upload-image.js',

        # New stuff.
        'js/devreg/devhub.js',
        'js/devreg/submit-details.js',

        # Specific stuff for making payments nicer.
        'js/devreg/paypal.js',
        'js/zamboni/validator.js',
    ),
    'mkt/consumer': (
        'js/lib/jquery-1.7.1.js',
        'js/lib/webtrends.js',
        'js/lib/underscore.js',
        'js/lib/format.js',
        'js/common/tracking.js',
        'js/mkt/utils.js',
        'js/zamboni/browser.js',
        'js/mkt/init.js',
        'js/mkt/browserid.js',
        'js/zamboni/truncation.js',
        'js/common/keys.js',
        'js/mkt/capabilities.js',
        'js/mkt/fragments.js',
        'js/mkt/overlay.js',
        'js/mkt/slider.js',
        'js/mkt/login.js',
        'js/mkt/install.js',
        'js/mkt/payments.js',
        'js/mkt/buttons.js',
        'js/mkt/search.js',
        'js/mkt/apps.js',
        'js/zamboni/outgoing_links.js',
        'js/common/upload-image.js',

        # Search suggestions.
        'js/impala/ajaxcache.js',
        'js/impala/suggestions.js',

        # Account settings.
        'js/mkt/account.js',

        # Detail page.
        'js/mkt/detail.js',
        'js/mkt/lightbox.js',

        # Stick.
        'js/lib/stick.js',
    ),
    'mkt/stats': (
        'js/zamboni/storage.js',
        'js/mkt/modal.js',
        'js/lib/jquery-datepicker.js',
        'js/lib/highcharts.src.js',
        'js/impala/stats/csv_keys.js',
        'js/impala/stats/helpers.js',
        'js/impala/stats/dateutils.js',
        'js/impala/stats/manager.js',
        'js/impala/stats/controls.js',
        'js/impala/stats/overview.js',
        'js/impala/stats/topchart.js',
        'js/impala/stats/chart.js',
        'js/impala/stats/table.js',
        'js/impala/stats/stats.js',
    ),
    'mkt/in-app-payments': (
        'js/lib/jquery-1.7.1.js',
        'js/mkt/inapp_payments.js',
        'js/mkt/browserid.js',
        'js/mkt/login.js',
    ),
}
