def global_context(request):
    Fake_Db_projects=[
     f"https://picsum.photos/id/{id}/100/80" for id in range(21,29)
     ]
    return dict(
        Fake_Db_projects=Fake_Db_projects,
    )