from prefect import task

@task(name='Transformar data de Linkedin')
def task_transform_link(offer_lists):
    offer_lists_transform = []
    for offer_list in offer_lists:
        title = offer_list['title']
        location = offer_list['location']
        url_value = offer_list['url_value']
        skill=offer_list['skill']
        offer_lists_transform.append({
            'title': title,
            'location': location,
            'url_value': url_value,
            'skill': skill
        })
    return offer_lists_transform