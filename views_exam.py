    return render(
        request,
        'app/index.html',
        {
            'site_name':site_name,
            'title':'Home Page',
            'year':datetime.now().year,
            'page':page_list,
            'page_active':page_active, #intデータ
            'page_last':page_last #intデータ
        }
    )
