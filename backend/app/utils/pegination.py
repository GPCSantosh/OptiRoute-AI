from math import ceil


def paginate(
    page: int,
    page_size: int,
    total: int,
):

    return {

        "page": page,

        "page_size": page_size,

        "total": total,

        "pages": ceil(total / page_size),
    }