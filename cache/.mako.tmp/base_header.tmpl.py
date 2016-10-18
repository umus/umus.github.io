# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1476755277.7352343
_enable_loop = True
_template_filename = '/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translation_header', 'html_navigation_links', 'html_header', 'html_site_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <div id="toptranslations">\n            <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav id="menu">\n    <ul>\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <li> ')
                __M_writer(str(text))
                __M_writer('\n            <ul>\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('                    <li class="active"><a href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a></li>\n')
                    else:
                        __M_writer('                    <li><a href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a></li>\n')
                __M_writer('            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a></li>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </ul>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_translation_header():
            return render_html_translation_header(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_site_title():
            return render_html_site_title(context)
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <header id="header">\n        ')
        __M_writer(str(html_site_title()))
        __M_writer('\n        ')
        __M_writer(str(html_translation_header()))
        __M_writer('\n        ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
        if search_form:
            __M_writer('            <div class="searchform" role="search">\n                ')
            __M_writer(str(search_form))
            __M_writer('\n            </div>\n')
        __M_writer('    </header>\n    ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <h1 id="brand"><a href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('" title="')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('" rel="home">\n')
        if logo_url:
            __M_writer('        <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="@" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('        ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('\n')
        __M_writer('    </a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"23": 2, "26": 0, "33": 2, "34": 16, "35": 28, "36": 57, "37": 66, "43": 59, "53": 59, "54": 60, "55": 61, "56": 62, "57": 62, "58": 63, "59": 63, "65": 30, "79": 30, "80": 33, "81": 34, "82": 35, "83": 35, "84": 35, "85": 37, "86": 38, "87": 39, "88": 39, "89": 39, "90": 39, "91": 39, "92": 39, "93": 39, "94": 40, "95": 41, "96": 41, "97": 41, "98": 41, "99": 41, "100": 44, "101": 45, "102": 46, "103": 47, "104": 47, "105": 47, "106": 47, "107": 47, "108": 47, "109": 47, "110": 48, "111": 49, "112": 49, "113": 49, "114": 49, "115": 49, "116": 53, "117": 53, "118": 53, "119": 54, "120": 54, "126": 4, "140": 4, "141": 6, "142": 6, "143": 7, "144": 7, "145": 8, "146": 8, "147": 9, "148": 10, "149": 11, "150": 11, "151": 14, "152": 15, "153": 15, "159": 18, "171": 18, "172": 19, "173": 19, "174": 19, "175": 19, "176": 20, "177": 21, "178": 21, "179": 21, "180": 23, "181": 24, "182": 25, "183": 25, "184": 25, "185": 27, "191": 185}, "source_encoding": "utf-8", "uri": "base_header.tmpl", "filename": "/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/base_header.tmpl"}
__M_END_METADATA
"""
