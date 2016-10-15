# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1476510808.0628898
_enable_loop = True
_template_filename = '/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_translations', 'html_feedlinks', 'html_headstart', 'html_stylesheets']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        theme_color = context.get('theme_color', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        title = context.get('title', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        use_cdn = context.get('use_cdn', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta content="')
        __M_writer(str(theme_color))
        __M_writer('" name="theme-color">\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 67, "23": 71, "24": 92, "25": 115, "26": 125, "32": 69, "37": 69, "38": 70, "39": 70, "45": 117, "55": 117, "56": 119, "57": 120, "58": 121, "59": 121, "60": 121, "61": 121, "62": 121, "63": 121, "64": 121, "65": 124, "71": 94, "82": 94, "83": 95, "84": 96, "85": 96, "86": 96, "87": 97, "88": 98, "89": 99, "90": 100, "91": 100, "92": 100, "93": 100, "94": 100, "95": 102, "96": 103, "97": 103, "98": 103, "99": 106, "100": 107, "101": 108, "102": 109, "103": 109, "104": 109, "105": 109, "106": 109, "107": 111, "108": 112, "109": 112, "110": 112, "116": 3, "144": 3, "145": 6, "146": 7, "147": 8, "148": 10, "149": 11, "150": 13, "151": 14, "152": 15, "153": 17, "154": 18, "155": 21, "156": 21, "157": 21, "158": 24, "159": 25, "160": 25, "161": 25, "162": 27, "163": 28, "164": 28, "165": 28, "166": 30, "167": 31, "168": 32, "169": 32, "170": 32, "171": 33, "172": 34, "173": 34, "174": 34, "175": 34, "176": 34, "177": 36, "178": 37, "179": 37, "180": 38, "181": 38, "182": 39, "183": 39, "184": 40, "185": 40, "186": 42, "187": 43, "188": 44, "189": 44, "190": 44, "191": 44, "192": 44, "193": 44, "194": 44, "195": 47, "196": 48, "197": 49, "198": 49, "199": 49, "200": 51, "201": 52, "202": 53, "203": 53, "204": 53, "205": 55, "206": 56, "207": 56, "208": 56, "209": 58, "210": 59, "211": 59, "212": 60, "213": 61, "214": 62, "215": 63, "216": 63, "217": 63, "218": 65, "219": 66, "220": 66, "226": 73, "234": 73, "235": 74, "236": 75, "237": 76, "238": 77, "239": 78, "240": 80, "241": 81, "242": 84, "243": 85, "244": 88, "245": 89, "251": 245}, "source_encoding": "utf-8", "filename": "/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/base_helper.tmpl"}
__M_END_METADATA
"""
