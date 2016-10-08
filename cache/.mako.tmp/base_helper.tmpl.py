# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1475888202.543145
_enable_loop = True
_template_filename = '/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_stylesheets', 'html_headstart', 'html_feedlinks', 'html_translations']


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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
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


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        url_replacer = context.get('url_replacer', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        is_rtl = context.get('is_rtl', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
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


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
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


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 67, "23": 71, "24": 92, "25": 115, "26": 125, "32": 69, "37": 69, "38": 70, "39": 70, "45": 73, "53": 73, "54": 74, "55": 75, "56": 76, "57": 77, "58": 78, "59": 80, "60": 81, "61": 84, "62": 85, "63": 88, "64": 89, "70": 3, "98": 3, "99": 6, "100": 7, "101": 8, "102": 10, "103": 11, "104": 13, "105": 14, "106": 15, "107": 17, "108": 18, "109": 21, "110": 21, "111": 21, "112": 24, "113": 25, "114": 25, "115": 25, "116": 27, "117": 28, "118": 28, "119": 28, "120": 30, "121": 31, "122": 32, "123": 32, "124": 32, "125": 33, "126": 34, "127": 34, "128": 34, "129": 34, "130": 34, "131": 36, "132": 37, "133": 37, "134": 38, "135": 38, "136": 39, "137": 39, "138": 40, "139": 40, "140": 42, "141": 43, "142": 44, "143": 44, "144": 44, "145": 44, "146": 44, "147": 44, "148": 44, "149": 47, "150": 48, "151": 49, "152": 49, "153": 49, "154": 51, "155": 52, "156": 53, "157": 53, "158": 53, "159": 55, "160": 56, "161": 56, "162": 56, "163": 58, "164": 59, "165": 59, "166": 60, "167": 61, "168": 62, "169": 63, "170": 63, "171": 63, "172": 65, "173": 66, "174": 66, "180": 94, "191": 94, "192": 95, "193": 96, "194": 96, "195": 96, "196": 97, "197": 98, "198": 99, "199": 100, "200": 100, "201": 100, "202": 100, "203": 100, "204": 102, "205": 103, "206": 103, "207": 103, "208": 106, "209": 107, "210": 108, "211": 109, "212": 109, "213": 109, "214": 109, "215": 109, "216": 111, "217": 112, "218": 112, "219": 112, "225": 117, "235": 117, "236": 119, "237": 120, "238": 121, "239": 121, "240": 121, "241": 121, "242": 121, "243": 121, "244": 121, "245": 124, "251": 245}}
__M_END_METADATA
"""
