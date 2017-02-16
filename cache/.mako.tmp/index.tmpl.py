# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487216966.7286203
_enable_loop = True
_template_filename = '/home/aleph/PROG/PIT/nikola/lib/python3.5/site-packages/nikola/data/themes/umus/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content_header', 'content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        front_index_header = context.get('front_index_header', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
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
        helper = _mako_get_namespace(context, 'helper')
        comments = _mako_get_namespace(context, 'comments')
        date_format = context.get('date_format', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context)
        index_teasers = context.get('index_teasers', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content_header():
            return render_content_header(context)
        front_index_header = context.get('front_index_header', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
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


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"128": 26, "129": 26, "130": 28, "131": 30, "132": 31, "133": 32, "134": 33, "135": 35, "136": 38, "137": 39, "138": 39, "139": 40, "140": 40, "141": 41, "142": 41, "148": 6, "23": 2, "26": 3, "158": 6, "159": 7, "32": 0, "161": 8, "162": 9, "163": 9, "164": 9, "170": 164, "54": 2, "55": 3, "56": 4, "61": 11, "160": 7, "66": 42, "72": 14, "83": 13, "99": 13, "104": 14, "105": 15, "106": 16, "107": 16, "108": 16, "109": 18, "110": 19, "111": 20, "112": 20, "113": 20, "114": 22, "115": 22, "116": 22, "117": 22, "118": 24, "119": 24, "120": 24, "121": 24, "122": 24, "123": 24, "124": 24, "125": 24, "126": 25, "127": 26}, "filename": "/home/aleph/PROG/PIT/nikola/lib/python3.5/site-packages/nikola/data/themes/umus/templates/index.tmpl"}
__M_END_METADATA
"""
