# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481120279.59454
_enable_loop = True
_template_filename = '/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_post_header', 'html_sourcelink', 'html_title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

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


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('        <div class="metadata posttranslations translations">\n            <h3 class="posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h3>\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def html_title():
            return render_html_title(context)
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        def html_translations(post):
            return render_html_translations(context,post)
        __M_writer = context.writer()
        __M_writer('\n    <header>\n\n\n\n      ')
        __M_writer(str(html_title()))
        __M_writer('\n        <div class="metadata">\n            <p class="dateline"><a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('</time></a></p>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('                <p class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('\n')
        __M_writer('            ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n')
        if post.meta('link'):
            __M_writer('                    <p class="linkline"><a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('">')
            __M_writer(str(messages("Original site")))
            __M_writer('</a></p>\n')
        if post.description():
            __M_writer('                <meta name="description" itemprop="description" content="')
            __M_writer(filters.html_escape(str(post.description())))
            __M_writer('">\n')
        __M_writer('        </div>\n        ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n    </header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        <p class="sourceline"><a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(str(post.title()))
            __M_writer('</a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/post_header.tmpl", "uri": "post_header.tmpl", "line_map": {"132": 24, "133": 25, "134": 26, "135": 26, "136": 26, "137": 26, "138": 26, "151": 6, "144": 5, "150": 5, "23": 2, "152": 7, "153": 7, "26": 3, "155": 7, "156": 7, "29": 0, "34": 2, "35": 3, "36": 9, "37": 22, "38": 28, "39": 51, "154": 7, "45": 11, "54": 11, "55": 12, "56": 13, "57": 14, "58": 14, "59": 15, "60": 16, "61": 17, "62": 17, "63": 17, "64": 17, "65": 17, "66": 17, "67": 17, "68": 20, "74": 30, "162": 156, "89": 30, "90": 35, "91": 35, "92": 37, "93": 37, "94": 37, "95": 37, "96": 37, "97": 37, "98": 37, "99": 37, "100": 38, "101": 39, "102": 39, "103": 39, "104": 41, "105": 41, "106": 41, "107": 42, "108": 43, "109": 43, "110": 43, "111": 43, "112": 43, "113": 45, "114": 46, "115": 46, "116": 46, "117": 48, "118": 49, "119": 49, "125": 24}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
