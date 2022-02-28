from transliterate import slugify


def slug_generator(title):
    slug = title.lower()
    slug = slugify(slug)
    return slug


#todo: fix generator