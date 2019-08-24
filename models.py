def transform_post(post):
    """Transforms post data
    
    Arguments:
        post {dict} -- Post data
    """
    return {
        'id': post['id'],
        'title': post['title'],
        'url': post['url'],
        'image': post['feature_image'],
        'summary': post['custom_excerpt'] \
            if post['custom_excerpt'] else post['excerpt']
    }
