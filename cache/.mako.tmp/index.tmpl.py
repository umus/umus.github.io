# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481273215.471791
_enable_loop = True
_template_filename = '/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content_header', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        index_teasers = context.get('index_teasers', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        pagekind = context.get('pagekind', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_file = context.get('index_file', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_teasers = context.get('index_teasers', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context)
        pagekind = context.get('pagekind', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        posts = context.get('posts', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        def content_header():
            return render_content_header(context)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(str(post.title()))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"128": 16, "129": 16, "130": 16, "131": 18, "132": 19, "133": 20, "134": 20, "135": 20, "136": 22, "137": 22, "138": 22, "139": 22, "140": 24, "141": 24, "142": 24, "143": 24, "144": 24, "145": 24, "146": 24, "147": 24, "148": 25, "149": 26, "150": 26, "23": 3, "152": 28, "153": 30, "26": 2, "155": 32, "156": 33, "154": 31, "158": 38, "159": 39, "32": 0, "161": 40, "162": 40, "163": 41, "164": 41, "170": 164, "157": 35, "54": 2, "55": 3, "56": 4, "151": 26, "61": 11, "160": 39, "66": 42, "72": 6, "82": 6, "83": 7, "84": 7, "85": 8, "86": 9, "87": 9, "88": 9, "94": 14, "105": 13, "121": 13, "126": 14, "127": 15}, "filename": "/home/aleph/PROG/PIT/nikola/lib/python3.4/site-packages/nikola/data/themes/umus/templates/index.tmpl"}
__M_END_METADATA
"""
